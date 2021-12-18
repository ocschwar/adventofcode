import init.data.nat
import init.data.to_string
import data.set
import data.list.basic
import data.bool
import data.buffer.parser
#check prod.mk
open parser
open io

@[derive  inhabited ]
structure position :=
(distance : ℕ)
(depth : ℕ)
(aim : ℤ ) 
@[derive inhabited]
inductive comd : Type
| up : comd
| down : comd
| forward : comd
@[derive inhabited]
structure instruction := 
(comd : comd ) 
(length : ℕ  )
# 

def mkstr  (p:position): string := 
  (to_string (position.depth p)) ++ ", "  ++ to_string(position.distance p)


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
     | ordering.gt := (position.depth p )+ ((position.aim p) * (instruction.length i:ℤ ))
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
      | comd.down := (position.aim p)- (instruction.length i))