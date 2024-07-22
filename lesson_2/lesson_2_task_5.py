def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Некорректный номер месяца"

# Примеры использования функции
print(month_to_season(2))  # Вывод: Зима
print(month_to_season(4))  # Вывод: Весна
print(month_to_season(7))  # Вывод: Лето
print(month_to_season(10)) # Вывод: Осень
print(month_to_season(13)) # Вывод: Некорректный номер месяца