# num_arrays = int(input("Шумораи массивҳоро ворид кунед (ҳадди аққал 3): "))
arrays = []
sums = []

array_config = {
    0: ("Таъминкунандагон ва ҳаҷми захираи онҳо", "A"),
    1: ("Истеъмолкунандагон ва ҳаҷми талаботи онҳо", "B"),
    2: ("Шумораи хоначаҳо", "X")
}

# Воридкунии маълумот
for i in range(3):
    name, prefix = array_config[i]
    print(f"\n{name}")

    if i < 2:
        size = int(input(f"Шумораи элементҳои {prefix}-ро ворид кунед: "))
        current_array = [int(input(f"{prefix}{j + 1}: ")) for j in range(size)]
    else:
        size_A = len(arrays[0])
        size_B = len(arrays[1])
        required_size = size_A * size_B
        print(f"Лозим аст {required_size} элементҳо ворид шаванд:")
        current_array = [int(input(f"X{k + 1}: ")) for k in range(required_size)]

    arrays.append(current_array)
    sums.append(sum(current_array))

# Санҷиши баробарии маҷмӯъҳо
result = "Инвентаризатсия барои корбарон кофӣ аст" if sums[0] == sums[1] else "Захира ба корбарон намерасад"

# Чоп кардани ҷадвал
print("\n" + "=" * 50)
print(f"Натиҷа: {result}")
print("=" * 50)

# Тартиб додани ҷадвали ниҳоӣ
if result.startswith("Инвентаризатсия барои корбарон кофӣ аст"):
    a = arrays[0].copy()
    b = arrays[1].copy()
    c = arrays[2]

    # Эҷоди матритсаи тақсимот бо усули кунҷи шимолу ғарбӣ
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

    # Чоп кардани матритсаи тақсимот
    print("\nМатритсаи ҷамъбастии тақсимот:")
    col_width = max(len(f"B{j + 1}:{val}") for j, val in enumerate(arrays[1])) + 4

    # Сарлавҳаи ҷадвал
    header = " " * 10
    for j, val in enumerate(arrays[1]):
        header += f"B{j + 1}:{val}".center(col_width)
    print(header)
    print("-" * len(header))

    # Қисми ҷисми ҷадвал
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

    # Ҳисобкунӣ ва чопи маҷмӯъи ҳосилҳо
    print("\nҲисоб кардани маблағи умумӣ:")
    total_sum = 0
    size_B = len(arrays[1])
    step = 1
    ҳосилҳои_ғайринулӣ = []

    for i in range(len(distribution)):
        for j in range(len(distribution[i])):
            маҷмӯъи_қаблӣ = total_sum
            allocated = distribution[i][j]
            c_index = i * size_B + j
            c_val = c[c_index]
            ҳосил = allocated * c_val

            total_sum += ҳосил

            хабар = f"{step}) A{i + 1}B{j + 1}: ({allocated}) * {c_val} = {ҳосил}"
            хабар += f" → Маҷмӯъи ҷорӣ: {маҷмӯъи_қаблӣ} + {ҳосил} = {total_sum}"
            print(хабар)

            if ҳосил != 0:
                ҳосилҳои_ғайринулӣ.append(str(ҳосил))

            step += 1

    if ҳосилҳои_ғайринулӣ:
        ибораи_маҷмӯъӣ = " + ".join(ҳосилҳои_ғайринулӣ)
        print(f"\nМаҷмӯъи умумии ниҳоӣ: {ибораи_маҷмӯъӣ} = {total_sum}")
    else:
        print(f"\nМаҷмӯъи умумии ниҳоӣ: 0")

