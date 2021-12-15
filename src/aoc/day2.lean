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

def word : parser string := many_char (sat char.is_alpha)

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

def map {α β : Type} (f : α → β) : list α → list β | [] := []
| (x :: xs) := f x :: map xs

structure position :=
(distance : ℕ)
(depth : ℕ)

def main : io unit :=
  do dayinput ← parse_file "day2.txt"  (many (word number <* ch '\n')) ,
