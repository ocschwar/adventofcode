import system.io
import .common data.list.basic

open char
open list
open io

def map {α β : Type} (f : α → β) : list α → list β | [] := []
| (x :: xs) := f x :: map xs

def bool_to_nat ( b: list bool):  list ℕ  := (if b then 1 else 0 )

  
def cnt_true  (b: list bool) :  ℕ :=
  sum bool_to_nat b


def main : io unit :=
  do   r ← fs.read_file "day1.txt",
  put_str_ln "What is your name? ",
  put_str r.to_string
--  put_str_ln "test",
--  a ← monad_io.open
--  r ← system.io.open {"day1.txt"} 