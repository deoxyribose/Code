import Data.Char

fact n = foldl (*) 1 [2..n]
sum $ map digitToInt (show (fact 100))