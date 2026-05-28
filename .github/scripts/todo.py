class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = False
        self.status = status

        if status == "Done":
            self.completed = True

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        task1 = Task("Set up GitHub repository")
        task2 = Task("Create Python task manager")
        task3 = Task("Write unit tests")
        task4 = Task("Build Docker container")
        task5 = Task("Run CI workflow")
        task6 = Task("Update index.html report")

        task1.mark_completed()
        task2.mark_completed()
        task3.mark_completed()

        self.tasks = [task1, task2, task3, task4, task5, task6]

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]


def main():
    pool = TaskPool()
    pool.populate()

    todo_tasks = pool.get_open_tasks()
    done_tasks = pool.get_done_tasks()

    print("ToDo Tasks:")
    for task in todo_tasks:
        print(task.title)

    print("\nDone Tasks:")
    for task in done_tasks:
        print(task.title)


if __name__ == "__main__":
    main()
