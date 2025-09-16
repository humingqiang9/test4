-- Function to calculate the area of a circle
function calculateCircleArea(radius)
    -- Check if radius is valid
    if radius < 0 then
        error("Radius cannot be negative")
    end
    
    -- Using the formula: Area = π * radius^2
    local area = math.pi * radius * radius
    return area
end

-- Example usage:
-- local area = calculateCircleArea(5)
-- print("Area of circle with radius 5 is: " .. area)