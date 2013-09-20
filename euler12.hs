
triangle n = sum [1..n]
-- take 10 $ map triangle [1..]

factors n = (length $ filter (\m -> n `mod` m  == 0) [1..(quot n 2)]) + 1
firstoverhundered = triangle $ length $ takeWhile (<= 100) $ map (factors . triangle) [1..]
