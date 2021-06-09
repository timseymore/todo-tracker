# noinspection PyUnresolvedReferences
from todo import ToDo, Task, ToDoTracker


class TestObject:
    TEST_TRACKER = ToDoTracker()

    TEST_TASK_1 = Task("Task 1")
    TEST_TASK_2 = Task("Task 2")
    TEST_TASK_3 = Task("Task 3")

    TEST_TODO_1 = ToDo("ToDo 1")
    TEST_TODO_2 = ToDo("ToDo 2")
    TEST_TODO_3 = ToDo("ToDo 3")
    TEST_TODO_4 = ToDo("ToDo 4")
    TEST_TODO_5 = ToDo("ToDo 5")


class Tester:
    @staticmethod
    def check_expect(actual, expected, message=""):
        if actual != expected:
            print(message + "FAILED: Expected: " + str(expected) + " Actual: " + str(actual))
            return False
        else:
            return True


class TestCase:
    def __init__(self):
        self.result = False
        self.wasRun = False
        self.testObject = None

    def setup(self):
        self.result = False
        self.wasRun = False
        self.testObject = TestObject()

    def teardown(self):
        self.testObject = None

    def run(self):
        self.setup()
        self.wasRun = True
        self.teardown()


# TO-DO TESTS

# get_date() / set_date() tests

Tester.check_expect(TestObject.TEST_TODO_1.get_date(), "", "ToDo.get_date() - Default date")

TestObject.TEST_TODO_1.set_date(101)
Tester.check_expect(TestObject.TEST_TODO_1.get_date(), "", "ToDo.set_date(101) - invalid argument type given")

TestObject.TEST_TODO_1.set_date("01-01-0001")
Tester.check_expect(TestObject.TEST_TODO_1.get_date(), "01-01-0001", "ToDo.get_date() - valid lower bounds")

TestObject.TEST_TODO_1.set_date("06-15-5432")
Tester.check_expect(TestObject.TEST_TODO_1.get_date(), "06-15-5432", "ToDo.set_date- valid middle / change previous")

TestObject.TEST_TODO_2.set_date("12-31-9999")
Tester.check_expect(TestObject.TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('12-31-9999') - valid upper bounds")


# set_location() tests
TestObject.TEST_TODO_1.set_location("here")
Tester.check_expect(TestObject.TEST_TODO_1.get_location(), "here", "ToDo.set_location('here') - valid")

# get_description tests
Tester.check_expect(TestObject.TEST_TODO_1.get_description(), "ToDo 1 on 06-15-5432 @ here", "ToDo.get_description()")

TestObject.TEST_TODO_1.set_date("")
Tester.check_expect(TestObject.TEST_TODO_1.get_description(), "ToDo 1 @ here", "ToDo.set_date, ToDo.get_description()")

TestObject.TEST_TODO_1.set_location("")
Tester.check_expect(TestObject.TEST_TODO_1.get_description(), "ToDo 1", "ToDo.set_location, ToDo.get_description()")

# get_complete set_complete tests
Tester.check_expect(TestObject.TEST_TODO_1.get_complete(), False, "ToDo.get_complete() -> False")
TestObject.TEST_TODO_1.set_complete()
Tester.check_expect(TestObject.TEST_TODO_1.get_complete(), True, "ToDo.set_complete(), ToDo.get_complete -> True")


# TASK TESTS
Tester.check_expect(TestObject.TEST_TASK_1.num_subs(), 0, "Task.num_subs() -> 0")

Tester.check_expect(TestObject.TEST_TASK_1.contains(TestObject.TEST_TODO_3), False, "Task.contains() - False, empty")

TestObject.TEST_TASK_1.add_doable(TestObject.TEST_TODO_1)
Tester.check_expect(TestObject.TEST_TASK_1.get_subs()[0], TestObject.TEST_TODO_1, "Task.add_doable() - empty, add one")

TestObject.TEST_TASK_1.add_doable(TestObject.TEST_TODO_2)
Tester.check_expect(TestObject.TEST_TASK_1.get_subs()[1], TestObject.TEST_TODO_2,
                    "Task.add_doable - not empty, add new")

TestObject.TEST_TASK_1.add_doable(TestObject.TEST_TODO_1)
Tester.check_expect(TestObject.TEST_TASK_1.num_subs(), 2, "Task.add_doable() -> ERROR: existing, Task.num_subs() -> 2")
Tester.check_expect(TestObject.TEST_TASK_1.contains(TestObject.TEST_TODO_1), True, "Task.contains() -> True")

TestObject.TEST_TASK_1.remove_doable(TestObject.TEST_TODO_1.get_description())
Tester.check_expect(TestObject.TEST_TASK_1.contains(TestObject.TEST_TODO_1), False,
                    "Task.remove_doable() : contains = true, Task.contains() -> False, not empty")
