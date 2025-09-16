-- Функция для вычисления площади круга
-- Принимает радиус в качестве аргумента
function calculate_circle_area(radius)
    -- Проверка, что радиус положительный
    if radius <= 0 then
        return nil, "Радиус должен быть положительным числом"
    end
    
    -- Вычисление площади круга
    local area = math.pi * radius * radius
    
    -- Возврат результата
    return area
end

-- Пример использования функции
local radius = 5
local area, error = calculate_circle_area(radius)

if area then
    print("Площадь круга с радиусом " .. radius .. " равна " .. area)
else
    print("Ошибка: " .. error)
end