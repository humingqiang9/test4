-- student_grades.lua
-- 定义一个存储学生成绩的表
local student_grades = {
    Alice = { math = 95, science = 87, english = 92 },
    Bob = { math = 78, science = 85, english = 80 },
    Charlie = { math = 90, science = 93, english = 88 },
    Diana = { math = 85, science = 82, english = 90 }
}

-- 计算单个学生的平均分
local function calculate_average(grades)
    local sum = 0
    local count = 0
    for _, grade in pairs(grades) do
        sum = sum + grade
        count = count + 1
    end
    return sum / count
end

-- 打印所有学生的成绩和平均分
print("学生成绩及平均分:")
for student, grades in pairs(student_grades) do
    local avg = calculate_average(grades)
    print(student .. ":")
    for subject, grade in pairs(grades) do
        print("  " .. subject .. ": " .. grade)
    end
    print("  平均分: " .. string.format("%.2f", avg))
    print("---")
end