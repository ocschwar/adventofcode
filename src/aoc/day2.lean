import init.data.nat
import init.data.to_string
import data.set
import data.list.basic
import data.bool
import data.buffer.parser
#check prod.mk
open parser
open io

def number : parser ℕ :=
string.to_nat <$> many_char1 (sat char.is_digit)

def signed_number : parser ℤ :=
ch '+' >> (int.of_nat <$> number) <|>
ch '-' >> ((λ x:ℕ, -x) <$> number)

def letter : parser char := sat char.is_lower
def Letter : parser char := sat char.is_upper

def word : parser string := many_char (sat char.is_alpha)

@[derive inhabited ]
structure position :=
(distance : ℕ)
(depth : ℕ)
(aim : ℤ ) 

def mkstr  (p:position): string := 
  (to_string (position.depth p)) ++ ", "  ++ to_string(position.distance p)
@[derive inhabited]
inductive comd : Type
| up : comd
| down : comd
| forward : comd

def token : parser comd := 
(str "up " $> comd.up) <|> 
(str "down " $> comd.down) <|> 
(str "forward " $> comd.forward)

@[derive inhabited]
structure instruction := 
(comd : comd ) 
(length : ℕ  )

def given_inst : parser instruction := 
  instruction.mk <$> token <*> number



def go {α} (file : string) (p : parser α) (m : α → option string) : io unit :=
do s ← io.fs.read_file file,
  sum.inr a ← return $ run p s,
  some str ← return $ m a,
  trace str (return ())

--#check 

def parse_lines {α} (h : io.handle) (p : parser α) : io (list α) :=
io.iterate [] (λ parsed,
  do done ← io.fs.is_eof h,
     if done
     then return none
     else do s ← io.fs.get_line h,
             sum.inr a ← return $ run p s,
             return $ some $ parsed ++ [a])

def parse_file {α} (file : string) (p : parser α) : io (list α) :=
  do h ← io.mk_file_handle file io.mode.read ff,
     parse_lines h p

def map {α β : Type} (f : α → β) : list α → list β | [] := []
| (x :: xs) := f x :: map xs

#eval (-2:ℤ )* (1:ℕ )

def move_position (p:position) (i:instruction ) : position :=
  position.mk ((position.distance p)+ 
  (match (instruction.comd i) with 
     comd.forward :=  ↑  ( instruction.length i)  ,
     comd.up := 0 ,
     comd.down := 0
  end 
  ))
  (0 + 
   (match (instruction.comd i) with 
     comd.forward :=  match cmp (position.aim p) 0 with 
     | ordering.eq := 0 
     | ordering.gt := (position.depth p )+ ((position.aim p) * (instruction.length i))
     | ordering.lt := (match (position.depth p) ((-position.aim p) * (instruction.length i)) with 
        |ordering.gt := 0 
        | ordering.eq := 0         
        | ordering.lt := 0 
        end )       
      end
      |comd.up:= 0
      |comd.down:= 0
      end))
      (match (instruction.comd i) with 
      | comd.forward := (position.aim p )
      | comd.up := (position.aim p)+ (instruction.length i)
      | comd.down := (position.aim p)- (instruction.length i)
/-   ))((match (instruction.comd i) with 
     comd.forward := (position.aim p ),-- + (position.aim p )* (instruction.length i),
     comd.up :=  (position.aim p ) - (instruction.length i),
     comd.down := (position.depth p )+ (instruction.length i)
     end ))
-/
-- todo: function that takes an instruction and a position and puts out a 
def voyage : list instruction → position → position 
| [] p := p 
| (i::l) p := voyage l (move_position p i )

def main : io unit :=
  do dayinput ← parse_file "day2.txt" (many (given_inst <* ch '\n')) ,
  put_str_ln (to_string ( list.length dayinput)),
  let dd : list instruction := map list.head dayinput,
  let pp :position := voyage dd (position.mk 0 0 ),
  put_str_ln (mkstr pp )

--variable zzz : ℤ 
--variable yy : ℕ 
--variable xx : ℕ --, zzz : ℤ 
--#eval  (1:ℕ ) + ↑ ( (-2:ℤ)*↑ (1:ℕ ):ℤ ):ℕ 
--#check (-2:ℤ)*(1:ℕ )
--#check (2:ℕ )* (↑ (2:ℤ ):ℕ )
