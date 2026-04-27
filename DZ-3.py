# Створити клас CourseModule з полями title, duration_hours, practice_tasks.
#
# Потрібно реалізувати:
#
# 1- __str__() - короткий опис модуля для користувача.
# 2- __repr__() - технічне представлення об'єкта для відладки.
# 3- __len__() - кількість практичних завдань у модулі.
# 4- __add__(other) - сумарну тривалість двох модулів.
# 5- __eq__(other) - порівняння модулів за кількістю практичних завдань.
# 6- __lt__(other) - порівняння модулів за тривалістю,
# щоб можна було використовувати sorted().

class CourseModule:
    def __init__(self, title, duration_hours, practice_tasks):
        self.title = title
        self.duration_hours = duration_hours
        self.practice_tasks = practice_tasks

    # 1
    def __str__(self):
        return f"Module: {self.title} ({self.duration_hours}h, {len(self)} tasks)"

    # 2
    def __repr__(self):
        return (f"CourseModule(title='{self.title}', "
                f"duration_hours={self.duration_hours}, "
                f"practice_tasks={self.practice_tasks})")

    # 3
    def __len__(self):
        return len(self.practice_tasks)

    # 4
    def __add__(self, other):
        return self.duration_hours + other.duration_hours

    # 5
    def __eq__(self, other):
        return len(self) == len(other)

    # 6
    def __lt__(self, other):
        return self.duration_hours < other.duration_hours


module1 = CourseModule(
    "Python основи",
    3,
    ["Типи даних", "Основні функції", "Основні цикли "]
)

module2 = CourseModule(
    "Розширені основи",
    6,
    ["Списки", "Кортежі", "Словники", "Множини"]
)

module3 = CourseModule(
    "OOP",
    4,
    ["Класи", "Наслідування", "Поліморфізм"]
)


# repr
print(repr(module1))

# len
print(len(module1))

# додавання
print(module1 + module2)

# порівняння
print(module1 == module2)
print(module1 < module3)

# сортування
modules = [module1, module2, module3]
sorted_modules = sorted(modules)

print(sorted_modules)