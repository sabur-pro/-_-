# -_-

```markdown
# 🚀 Транспортная задача: оптимизация распределения ресурсов

Проект реализует алгоритм решения транспортной задачи с визуализацией результатов в табличном формате.

## 🌟 Особенности
- Динамическое создание массивов данных
- Автоматическая проверка баланса ресурсов
- Метод северо-западного угла для распределения
- Визуализация результатов в таблицах

## ⚙️ Требования
- Python 3.8+

## 🏃 Запуск
```bash
python transport_problem.py
```

## 🧮 Пример работы
### Входные данные:
```
Введите количество массивов: 3
Запас 1: 2 элемента (5, 5)
Потребитель 2: 3 элемента (3, 4, 3)
C 3: 6 элементов (2, 3, 1, 7, 4, 9)
```

### Результат:
```markdown
==================================================
Результат: Запас хватает пользователям
==================================================

| Название       | Элементы          | Сумма |
|----------------|-------------------|-------|
| Запас 1        | 5, 5             | 10    |
| Потребитель 2  | 3, 4, 3          | 10    |

Итоговая матрица:
|        | B1:3 | B2:4 | B3:3 |
|--------|------|------|------|
| A1:5   | (3)2 | (2)3 | 1    |
| A2:5   | 7    | (4)4 | (3)9 |
```

## 📋 Логика работы
1. Ввод данных:
   - Массив A (поставщики)
   - Массив B (потребители)
   - Матрица стоимости C

2. Проверка баланса:
   ```python
   if sum(A) == sum(B):
       print("Баланс соблюден")
   ```

3. Распределение ресурсов методом северо-западного угла.

## 📄 Лицензия
MIT License. Подробности в [LICENSE](LICENSE).
```
