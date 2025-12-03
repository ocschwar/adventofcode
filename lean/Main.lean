import Hello


-- partial def dump (stream : IO.FS.Stream) : IO Unit := do
--   let buf ← stream.read bufsize 
--   if buf.isEmpty then
--     pure ()
--   else 
--     let mut s ← String.ofByteArray buf 
--     let lines := s.splitOn '\n'  
    
--     pure ()

#check String.ofByteArray 
#check IO.FS.Stream.read 
#check IO.FS.readFile
def main (args : List String) : IO UInt32  :=
  match args with
  | [] => do
    IO.println s!"Hello, FOOBAR {hello}!" 
    pure 1 
  | filename :: args => do
    let s:String  ← IO.FS.readFile filename 
    let lines := String.splitToList s (. == '\n')     
    
    pure 0               
