module Puzzle where
import System.IO
import Data.List 

mkint :: String -> Int
mkint = \x -> read x :: Int

mkintlist :: [String] -> [Int]
mkintlist = \x -> map mkint x 

head' :: [a] -> a
head' [] = error "Can't call head on an empty list, dummy!"
head' (x:_) = x

scnd' :: [a] -> a
scnd' [] = error "Can't call head on an empty list, dummy!"
scnd' (_:y) = head' y

dist' :: (Int,Int) -> Int
dist' x = abs ( fst x - snd x )

match' :: [Int] -> Int -> Int
match' x y  = do
  let z = [ if xx == y then 1  else 0| xx <- x ]
  let zz = y* sum z 
  zz
--match' (x:_) 



main_1 = do
  let list = []
  handle <- openFile "input.txt" ReadMode
  contents <- hGetContents handle
  let content_lines = lines contents
  -- words - the haskell split 
  let pairs = map words content_lines
  let nums = map mkintlist pairs
  let a = Data.List.sort (map head' nums)
  let b = Data.List.sort (map scnd' nums)
  let c = zip a b
  let d = map dist' c 
  let e =  Data.List.sum d -- reduce (+) d
  print e

main = do
  let list = []
  handle <- openFile "input.txt" ReadMode
  contents <- hGetContents handle
  let content_lines = lines contents
  -- words - the haskell split 
  let pairs = map words content_lines
  let nums = map mkintlist pairs
  let a = Data.List.sort (map head' nums)
  let b = Data.List.sort (map scnd' nums)
  let e = map (\x -> match' b x) a 
  print (sum e) 
