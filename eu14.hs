collatz :: (Integral a) => a -> a
collatz n
	| odd(n) = 3*n + 1
	| otherwise = quot n 2

chain n = takeWhile (/= 1) (iterate collatz n)

answer = (maximum (map (length . chain) [10^1..(10^4)-1])) + 1

-- Spørg Søren om man kan parallelisere map'en