PERFECT_HEIGHT = 170
COEF = 1.3

# Вычисление нового роста, если реальный рост больше 170 см
def calculate_big(length):
    coef = (length - PERFECT_HEIGHT) / COEF
    new_length = length - coef
    return new_length

# Вычисление нового роста, если реальный рост меньше 170 см
def calculate_small(length):
    coef = (PERFECT_HEIGHT - length) / COEF
    new_length = length + coef
    return new_length

# Вычисление нового веса
def calculate_weight(new_length):
    new_weight = (new_length / 100) ** 2
    print(f"Средний вес: {round(float(new_weight * 24.99))}\n")

# Ввод реального роста
length = float(input("Введите длину тела реального животного: "))
# Вызов необходимой функции
if length > PERFECT_HEIGHT:
    new_length = calculate_big(length)
elif length < PERFECT_HEIGHT:
    new_length = calculate_small(length)
else:
    new_length = PERFECT_HEIGHT
print(f"Средний рост: {round(float(new_length))}")
# Вызов функции расчета веса
calculate_weight(new_length)
