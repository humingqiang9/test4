-- 学生成绩表
local student_scores = {
    ["Alice"] = { math = 95, english = 87, science = 92 },
    ["Bob"] = { math = 78, english = 82, science = 85 },
    ["Charlie"] = { math = 90, english = 93, science = 88 },
    ["Diana"] = { math = 85, english = 89, science = 91 }
}

-- 计算每个学生的平均分
for name, scores in pairs(student_scores) do
    local total = 0
    local count = 0
    for subject, score in pairs(scores) do
        total = total + score
        count = count + 1
    end
    local average = total / count
    print(name .. "'s average score is: " .. string.format("%.2f", average))
end

return student_scores