num_arrays = int(input("Введите количество массивов (минимум 3): "))
arrays = []
sums = []

array_config = {
    0: ("Запас", "A"),
    1: ("Потребитель", "B"),
    2: ("C", "X")
}

# Ввод данных
for i in range(3):
    name, prefix = array_config[i]
    print(f"\n{name} {i + 1}:")

    if i < 2:
        size = int(input("Введите количество элементов: "))
        current_array = [int(input(f"{prefix}{j + 1}: ")) for j in range(size)]
    else:
        size_A = len(arrays[0])
        size_B = len(arrays[1])
        required_size = size_A * size_B
        print(f"Требуется ввести {required_size} элементов:")
        current_array = [int(input(f"X{k + 1}: ")) for k in range(required_size)]

    arrays.append(current_array)
    sums.append(sum(current_array))

# Проверка равенства сумм
result = "Запас хватает пользователям" if sums[0] == sums[1] else "Запас не хватает"

# Вывод таблицы
print("\n" + "=" * 50)
print(f"Результат: {result}")
print("=" * 50)

# Форматирование итоговой таблицы
if result.startswith("Запас хватает"):
    a = arrays[0].copy()
    b = arrays[1].copy()
    c = arrays[2]

    # Создаем матрицу распределения методом северо-западного угла
    distribution = []
    c_idx = 0
    for i in range(len(a)):
        row = []
        for j in range(len(b)):
            if a[i] == 0 or b[j] == 0:
                row.append(0)
                c_idx += 1
                continue

            allocated = min(a[i], b[j])
            row.append(allocated)
            a[i] -= allocated
            b[j] -= allocated
            c_idx += 1
        distribution.append(row)

    print("\nИтоговая матрица распределения:")
    col_width = max(len(f"B{j + 1}:{val}") for j, val in enumerate(arrays[1])) + 4

    # Шапка таблицы
    header = " " * 10
    for j, val in enumerate(arrays[1]):
        header += f"B{j + 1}:{val}".center(col_width)
    print(header)
    print("-" * len(header))

    # Тело таблицы
    c_idx = 0
    for i, dist_row in enumerate(distribution):
        row_str = f"A{i + 1}:{arrays[0][i]}".ljust(10)
        for j, allocated in enumerate(dist_row):
            c_val = c[c_idx]
            display = f"({allocated}){c_val}" if allocated > 0 else f"{c_val}"
            row_str += display.center(col_width)
            c_idx += 1
        print(row_str)
    print("-" * len(header))