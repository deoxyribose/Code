let fibs = 0 : scanl (+) 1 fibs
sum [fib | fib <- fibs, even fib, fib < 4*10^6]