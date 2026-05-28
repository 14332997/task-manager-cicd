import unittest
from io import StringIO
import sys
from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):

    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        task = Task("Test task")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)
        self.assertEqual(self.pool.tasks[0].title, "Test task")
        self.assertEqual(self.pool.tasks[0].status, "ToDo")

    def test_get_open_tasks(self):
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()
        self.assertTrue(len(open_tasks) > 0)
        for task in open_tasks:
            self.assertEqual(task.status, "ToDo")

    def test_get_done_tasks(self):
        self.pool.populate()
        done_tasks = self.pool.get_done_tasks()
        self.assertTrue(len(done_tasks) > 0)
        for task in done_tasks:
            self.assertEqual(task.status, "Done")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskPool)

    output = StringIO()
    runner = unittest.TextTestRunner(stream=output, verbosity=2)
    result = runner.run(suite)

    lines = output.getvalue().splitlines()

    for line in lines:
        if "... ok" in line:
            print(line)

    if result.wasSuccessful():
        print("All tests passed.")
    else:
        print("Some tests failed.")
        sys.exit(1)
