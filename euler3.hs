minus (x:xs) (y:ys) = case (compare x y) of 
          LT -> x : minus  xs  (y:ys)
          EQ ->     minus  xs     ys 
          GT ->     minus (x:xs)  ys
minus  xs     _     = xs

primesToG m = 2 : sieve [3,5..m]  where
    sieve (p:xs) 
       | p*p > m = p : xs
       | True    = p : sieve (xs `minus` [p*p,p*p+2*p..])

decompose :: Int -> [Int]
decompose 1 = [1]
decompose n = [m | m <- primesToG n, n `mod` m == 0]