-- Function to calculate the area of a circle
-- @param radius The radius of the circle
-- @return The area of the circle
function calculate_circle_area(radius)
    -- Using the mathematical constant pi
    local pi = math.pi
    -- Calculate the area using the formula A = π * r^2
    local area = pi * radius * radius
    return area
end

-- Example usage:
-- local area = calculate_circle_area(5)
-- print("The area of the circle is: " .. area)