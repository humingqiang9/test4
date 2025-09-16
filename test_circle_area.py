import math

def calculate_circle_area(radius):
    """
    Функция для вычисления площади круга.
    Принимает радиус в качестве аргумента.
    """
    if radius <= 0:
        return None, "Радиус должен быть положительным числом"
    
    # Вычисление площади круга
    area = math.pi * radius * radius
    
    return area

# Пример использования функции
radius = 5
area = calculate_circle_area(radius)

if area:
    print(f"Площадь круга с радиусом {radius} равна {area}")
else:
    print("Ошибка: Радиус должен быть положительным числом")