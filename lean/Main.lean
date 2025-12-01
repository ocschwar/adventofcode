import Hello

--def main : IO Unit :=
--  IO.println s!"Hello, FOOBAR {hello}!"

def main (args : List String) : IO UInt32  :=
  match args with
  | [] => do
    IO.println s!"Hello, FOOBAR {hello}!" 
    pure 1 
  | _ =>  do
      IO.println s!"Hello, BAZZ {hello}!" 
      pure 0
