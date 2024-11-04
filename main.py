from collections import defaultdict

def parse_work_hours(records: list[str]) -> None:
    """Функция парсинга отработанных часов"""
    worker_hours = defaultdict(list)

    for record in records:
        # Разделяем строку на имя и количество часов
        worker_name, work_hours = record.rsplit(' ', 1)
        work_hours = int(work_hours)

        # Добавляем часы в список для соответствующего работника
        worker_hours[worker_name].append(work_hours)

    for worker_name, work_hours in worker_hours.items():
        hours_str = ", ".join(map(str, work_hours))
        print(f"{worker_name}: {hours_str}; sum: {sum(work_hours)}")

records = [
    "Андрей 9",
    "Василий 11",
    "Роман 7",
    "X Æ A-12 45",
    "Иван Петров 3",
    "Андрей 6",
    "Роман 11"
]

if __name__ == '__main__':
    parse_work_hours(records)
