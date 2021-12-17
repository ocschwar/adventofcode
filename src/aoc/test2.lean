import init.data.nat
import init.data.to_string
import data.set
import data.list.basic
import data.bool
import data.buffer.parser
#check prod.mk
open parser
open io

structure position :=
(distance : ℕ)
(depth : ℕ)
inductive comd : Type
| up : comd
| down : comd
| forward : comd

def token : parser comd := 
(str "up " $> comd.up) <|> 
(str "down " $> comd.down) <|> 
(str "forward " $> comd.forward)


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

#check parse_file "test2.txt" (many (token <* ch '\n'))

def main : io unit :=
  do dayinput ← parse_file "test2.txt"  (many (token <* ch '\n')) ,
  let dd :list comd := map list.head dayinput,
  put_str_ln (to_string dd),
  put_str_ln "done" 
