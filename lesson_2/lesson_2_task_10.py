def bank(X, Y):
    for _ in range(Y):
        X += X * 0.10
    return X

# Пример использования функции
first_deposit = 1000
years = 5

final_amount = bank(first_deposit, years)

print(f"Сумма на счету спустя {years} лет: {final_amount:.2f} рублей")