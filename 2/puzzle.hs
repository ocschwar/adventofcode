module Puzzle where
import System.IO
import Data.List
import Prelude

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
dist' x =  ( fst x - snd x )

match' :: [Int] -> Int -> Int
match' x y  = y * sum [ if xx == y then 1  else 0| xx <- x ]

deriv' :: [Int] -> [Int]
deriv' x = map dist' (zip (tail x) (init x))

safe_report :: [Int] -> Bool
safe_report x = do
  let d = deriv' x
  let dirs = (maximum(d) < 0) || minimum(d) > 0
  let m = map abs d
  maximum(m)<4 && dirs

safe_level x = do
  let s = safe_report x
  if s then 
    True
  else False



main = do
  let list = []
  handle <- openFile "input.txt" ReadMode
  contents <- hGetContents handle
  let content_lines = lines contents
  let w = map words content_lines
  let nums = map mkintlist w
  let safe = map safe_report nums
  let s = sum [ if xx then 1  else 0 | xx <- safe]
  print(s)




