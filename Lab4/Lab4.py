import os
import csv

# Имя файла по умолчанию
DEFAULT_FILENAME = "schedule.csv"

# Поля записи
FIELDS = [
    "week_type",    # Неделя: 'над чертой' / 'под чертой'
    "day_of_week",  # День недели
    "subject",      # Предмет
    "pair_number",  # Номер пары
    "lesson_type",  # Тип занятия (лекция, практика)
    "teacher"       # ФИО преподавателя
]

def print_menu():
    """Вывод главного меню."""
    print("\n--- Расписание занятий ---")
    print("1. Выбрать файл для работы")
    print("2. Инициализировать базу данных (создать/перезаписать)")
    print("3. Просмотреть все записи")
    print("4. Добавить запись")
    print("5. Удалить запись по номеру")
    print("6. Поиск по одному полю")
    print("7. Поиск по двум полям")
    print("8. Удалить все записи по заданному предмету")
    print("9. Заменить день недели и пару для заданного предмета")
    print("10. Вывести все сведения о лекционных занятиях")
    print("0. Выход")
    return input("Выберите действие: ")

def select_file():
    """Выбор файла базы данных."""
    filename = input("Введите имя файла (по умолчанию 'schedule.csv'): ")
    if not filename:
        filename = DEFAULT_FILENAME
    if not os.path.exists(filename):
        print(f"Файл '{filename}' не существует. Его можно создать через пункт 2.")
    return filename

def init_database(filename):
    """
    Инициализация базы данных.
    Создает новый файл или перезаписывает существующий (с заголовками полей).
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(FIELDS)
        print(f"База данных '{filename}' успешно инициализирована.")
    except Exception as e:
        print(f"Ошибка при инициализации: {e}")

def read_all_records(filename):
    """
    Чтение всех записей из файла.
    Возвращает список словарей (каждый словарь – одна запись).
    """
    records = []
    if not os.path.exists(filename):
        print(f"Файл '{filename}' не найден.")
        return records
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            # Пропускаем заголовок
            try:
                next(reader)
            except StopIteration:
                return records
            for row in reader:
                if len(row) == len(FIELDS):
                    record = {FIELDS[i]: row[i] for i in range(len(FIELDS))}
                    records.append(record)
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
    return records

def write_all_records(filename, records):
    """
    Запись списка словарей обратно в CSV файл.
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(FIELDS)
            for rec in records:
                writer.writerow([rec[field] for field in FIELDS])
    except Exception as e:
        print(f"Ошибка записи файла: {e}")

def print_records(records):
    """Красивый вывод списка записей в виде таблицы."""
    if not records:
        print("Нет записей для отображения.")
        return
    # Вычисляем ширину столбцов
    col_widths = {field: len(field) for field in FIELDS}
    for rec in records:
        for field in FIELDS:
            col_widths[field] = max(col_widths[field], len(str(rec[field])))
    # Заголовок
    header = " | ".join(f"{field:{col_widths[field]}}" for field in FIELDS)
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    # Данные
    for idx, rec in enumerate(records, 1):
        row_str = " | ".join(f"{rec[field]:{col_widths[field]}}" for field in FIELDS)
        print(f"{idx}: {row_str}")
    print("-" * len(header))

def add_record(filename):
    """Добавление новой записи в файл."""
    print("Введите данные новой записи:")
    record = {}
    for field in FIELDS:
        value = input(f"{field}: ")
        record[field] = value
    try:
        # Добавляем в конец файла
        with open(filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([record[field] for field in FIELDS])
        print("Запись добавлена.")
    except Exception as e:
        print(f"Ошибка добавления: {e}")

def delete_record_by_number(filename):
    """Удаление записи по её порядковому номеру."""
    records = read_all_records(filename)
    if not records:
        return
    print_records(records)
    try:
        num = int(input("Введите номер записи для удаления: "))
        if 1 <= num <= len(records):
            del records[num - 1]
            write_all_records(filename, records)
            print("Запись удалена.")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Ошибка: введите целое число.")

def search_single_field(filename):
    """Поиск записей, где значение в выбранном поле равно заданному."""
    print("Доступные поля:")
    for i, field in enumerate(FIELDS, 1):
        print(f"{i}. {field}")
    try:
        choice = int(input("Выберите номер поля: "))
        if 1 <= choice <= len(FIELDS):
            field = FIELDS[choice - 1]
            value = input(f"Введите значение для поля '{field}': ")
            records = read_all_records(filename)
            results = [rec for rec in records if rec[field] == value]
            print(f"\nРезультаты поиска ({len(results)}):")
            print_records(results)
        else:
            print("Неверный номер поля.")
    except ValueError:
        print("Ошибка: введите число.")

def search_two_fields(filename):
    """Поиск записей, которые удовлетворяют двум условиям одновременно."""
    print("Выберите первое поле:")
    for i, field in enumerate(FIELDS, 1):
        print(f"{i}. {field}")
    try:
        choice1 = int(input("Номер первого поля: "))
        if 1 <= choice1 <= len(FIELDS):
            field1 = FIELDS[choice1 - 1]
            value1 = input(f"Введите значение для '{field1}': ")
            print("\nВыберите второе поле:")
            for i, field in enumerate(FIELDS, 1):
                print(f"{i}. {field}")
            choice2 = int(input("Номер второго поля: "))
            if 1 <= choice2 <= len(FIELDS):
                field2 = FIELDS[choice2 - 1]
                value2 = input(f"Введите значение для '{field2}': ")
                records = read_all_records(filename)
                results = [rec for rec in records if rec[field1] == value1 and rec[field2] == value2]
                print(f"\nРезультаты поиска ({len(results)}):")
                print_records(results)
            else:
                print("Неверный номер второго поля.")
        else:
            print("Неверный номер первого поля.")
    except ValueError:
        print("Ошибка: введите число.")

def delete_by_subject(filename):
    """Удаление всех записей с заданным предметом."""
    subject = input("Введите название предмета для удаления: ")
    records = read_all_records(filename)
    new_records = [rec for rec in records if rec["subject"] != subject]
    deleted = len(records) - len(new_records)
    write_all_records(filename, new_records)
    print(f"Удалено записей: {deleted}")

def replace_day_and_pair(filename):
    """Замена дня недели и номера пары для заданного предмета."""
    subject = input("Введите предмет, для которого нужно заменить день и пару: ")
    print("Сначала укажите СТАРЫЕ значения, чтобы найти конкретные записи.")
    old_day = input("Старый день недели: ")
    old_pair = input("Старый номер пары: ")
    new_day = input("Новый день недели: ")
    new_pair = input("Новый номер пары: ")
    records = read_all_records(filename)
    changed = 0
    for rec in records:
        if rec["subject"] == subject and rec["day_of_week"] == old_day and rec["pair_number"] == old_pair:
            rec["day_of_week"] = new_day
            rec["pair_number"] = new_pair
            changed += 1
    write_all_records(filename, records)
    print(f"Заменено записей: {changed}")

def show_lectures(filename):
    """Вывод всех лекционных занятий."""
    records = read_all_records(filename)
    lectures = [rec for rec in records if rec["lesson_type"].lower() == "лекция"]
    print(f"\nЛекционные занятия ({len(lectures)}):")
    print_records(lectures)

def main():
    """Главная функция программы."""
    filename = DEFAULT_FILENAME  # Файл по умолчанию
    # Проверяем, есть ли файл
    if not os.path.exists(filename):
        print(f"Файл '{filename}' не найден. Вы можете его инициализировать (пункт 2).")

    while True:
        choice = print_menu()
        if choice == '1':
            filename = select_file()
        elif choice == '2':
            init_database(filename)
        elif choice == '3':
            records = read_all_records(filename)
            print_records(records)
        elif choice == '4':
            add_record(filename)
        elif choice == '5':
            delete_record_by_number(filename)
        elif choice == '6':
            search_single_field(filename)
        elif choice == '7':
            search_two_fields(filename)
        elif choice == '8':
            delete_by_subject(filename)
        elif choice == '9':
            replace_day_and_pair(filename)
        elif choice == '10':
            show_lectures(filename)
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()