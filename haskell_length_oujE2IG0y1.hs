-- 递归计算列表长度的Haskell函数

-- 基本情况：空列表的长度为0
length' :: [a] -> Int
length' [] = 0
-- 递归情况：列表的长度等于1加上其余部分的长度
length' (_:xs) = 1 + length' xs

-- 示例用法
main :: IO ()
main = do
    let list1 = [1, 2, 3, 4, 5]
    let list2 = ["a", "b", "c"]
    let list3 = [] :: [Int]
    
    putStrLn $ "列表 [1, 2, 3, 4, 5] 的长度是: " ++ show (length' list1)
    putStrLn $ "列表 [\"a\", \"b\", \"c\"] 的长度是: " ++ show (length' list2)
    putStrLn $ "空列表的长度是: " ++ show (length' list3)