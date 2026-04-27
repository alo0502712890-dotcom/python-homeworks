# ідея проекту = CRM для управління задачами

# Основні сутності:
# 1. User (Користувач)
# виконавець або менеджер
# має ім’я та роль

# 2. Project (Проєкт)
# належить замовнику
# містить список задач

# 3. Task (Задача)
# має назву, статус
# прив’язана до проєкту
# має виконавця (User)


#  Зв’язки:
# Project → Task (один до багатьох)
# User → Task (один до багатьох)

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role  # admin / manager / worker

    def __str__(self):
        return f"{self.name} ({self.role})"


class Task:
    def __init__(self, title, assigned_to):
        self.title = title
        self.status = "todo"
        self.assigned_to = assigned_to  # зв’язок з User

    def change_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}, Assigned to: {self.assigned_to.name}"


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []  # список задач

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks_count(self):
        return len(self.tasks)

    def __str__(self):
        return f"Project: {self.name}, Tasks: {len(self.tasks)}"