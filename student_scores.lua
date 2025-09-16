-- 学生成绩表
local student_scores = {
    Alice = 85,
    Bob = 92,
    Charlie = 78,
    Diana = 96,
    Edward = 88
}

-- 计算平均分的函数
local function calculate_average(scores)
    local total = 0
    local count = 0
    for name, score in pairs(scores) do
        total = total + score
        count = count + 1
    end
    if count == 0 then
        return 0 -- 避免除以零
    end
    return total / count
end

-- 计算并打印平均分
local average_score = calculate_average(student_scores)
print("学生平均分: " .. average_score)