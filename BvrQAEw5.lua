-- Function to calculate the area of a circle
function calculate_circle_area(radius)
    -- Check if radius is a positive number
    if type(radius) ~= "number" or radius <= 0 then
        error("Radius must be a positive number")
    end
    
    -- Calculate area using the formula A = π * r^2
    local area = math.pi * radius * radius
    return area
end

-- Example usage:
-- print(calculate_circle_area(5))  -- Should output approximately 78.54