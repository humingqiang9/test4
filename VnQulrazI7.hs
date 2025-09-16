-- 递归计算列表长度的Haskell函数

-- 函数类型签名：接受任意类型的列表，返回Int
length' :: [a] -> Int
-- 基本情况：空列表的长度为0
length' [] = 0
-- 递归情况：列表的长度等于1加上其余部分的长度
length' (_:xs) = 1 + length' xs

-- 示例用法
main :: IO ()
main = do
    let list1 = [1, 2, 3, 4, 5]
    let list2 = ["a", "b", "c"]
    let list3 = [] :: [Int]
    
    putStrLn $ "列表1 [1, 2, 3, 4, 5] 的长度是: " ++ show (length' list1)
    putStrLn $ "列表2 [\"a\", \"b\", \"c\"] 的长度是: " ++ show (length' list2)
    putStrLn $ "列表3 [] 的长度是: " ++ show (length' list3)
    
    putStrLn ""
    putStrLn "函数说明："
    putStrLn "1. length' :: [a] -> Int - 函数接受任意类型的列表并返回整数"
    putStrLn "2. length' [] = 0 - 基本情况：空列表长度为0"
    putStrLn "3. length' (_:xs) = 1 + length' xs - 递归情况：头部元素(1) + 尾部列表的长度"
    putStrLn "   其中 '_' 表示忽略头部元素的值，'xs' 是剩余的列表"