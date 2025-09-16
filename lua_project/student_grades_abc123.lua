-- Student grades data
local student_grades = {
    ["Alice"] = { math = 95, science = 87, english = 92 },
    ["Bob"] = { math = 78, science = 85, english = 80 },
    ["Charlie"] = { math = 92, science = 90, english = 88 },
    ["Diana"] = { math = 89, science = 94, english = 91 }
}

-- Function to calculate the average grade for a student
local function calculate_average(grades)
    local sum = 0
    local count = 0
    for _, grade in pairs(grades) do
        sum = sum + grade
        count = count + 1
    end
    if count == 0 then
        return 0 -- Avoid division by zero
    end
    return sum / count
end

-- Calculate and print average for each student
print("Student Grade Averages:")
for student, grades in pairs(student_grades) do
    local average = calculate_average(grades)
    print(student .. ": " .. string.format("%.2f", average))
end

-- Example of calculating overall class average for a subject
local function calculate_subject_average(subject)
    local sum = 0
    local count = 0
    for _, grades in pairs(student_grades) do
        if grades[subject] then
            sum = sum + grades[subject]
            count = count + 1
        end
    end
    if count == 0 then
        return 0
    end
    return sum / count
end

print("\nClass Subject Averages:")
print("Math: " .. string.format("%.2f", calculate_subject_average("math")))
print("Science: " .. string.format("%.2f", calculate_subject_average("science")))
print("English: " .. string.format("%.2f", calculate_subject_average("english")))

return student_grades