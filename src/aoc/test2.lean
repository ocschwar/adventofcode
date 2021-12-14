import init.data.nat
import init.data.to_string
import data.set
import data.list.basic
import data.bool
import data.buffer.parser

open parser
open io

def number : parser ℕ :=
string.to_nat <$> many_char1 (sat char.is_digit)

def signed_number : parser ℤ :=
ch '+' >> (int.of_nat <$> number) <|>
ch '-' >> ((λ x:ℕ, -x) <$> number)

def letter : parser char := sat char.is_lower
def Letter : parser char := sat char.is_upper



/- cribbed from io.fs.read_to_end and modified -/
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


def bool_to_nat : bool → ℕ 
| tt := 1 
| _ := 0 



def map {α β : Type} (f : α → β) : list α → list β | [] := []
| (x :: xs) := f x :: map xs


def sgn_diff_depth :(  list ℕ ) → ℕ    →  (list bool ) 
  | [] a  := []
  | (b :: l) a := (b > a) :: sgn_diff_depth l b

  
def cnt_true  (b: list bool) :  ℕ :=
  (list.map bool_to_nat b).sum 

#eval parse_file "day1.txt"  (many (number <* ch '\n')) 

def main : io unit :=
  do dayinput ← parse_file "day1.txt"  (many (number <* ch '\n')) ,
  --put_str (to_string dayinput),
  let dd : list ℕ := map list.head dayinput,
  put_str (to_string dd),
  put_str (to_string (sgn_diff_depth dd 200 )),
  let ds:ℕ  := (cnt_true(sgn_diff_depth dd  200)),
  put_str (to_string ds) 
