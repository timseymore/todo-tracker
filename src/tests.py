# noinspection PyUnresolvedReferences
from todo import ToDo, Task, ToDoTracker

# Test Objects
TEST_TRACKER = ToDoTracker()

TEST_TASK_1 = Task("Task 1")
TEST_TASK_2 = Task("Task 2")
TEST_TASK_3 = Task("Task 3")

TEST_TODO_1 = ToDo("ToDo 1")
TEST_TODO_2 = ToDo("ToDo 2")
TEST_TODO_3 = ToDo("ToDo 3")
TEST_TODO_4 = ToDo("ToDo 4")
TEST_TODO_5 = ToDo("ToDo 5")


class Test:
    @staticmethod
    def check_expect(actual, expected, message=""):
        print("Test: " + message)
        if actual == expected:
            print("Test Passed")
        else:
            print("Test Failed: Expected: " + str(expected) + " Actual: " + str(actual))


t = Test()


# TO-DO TESTS

TEST_TODO_1.set_date("01-02-1234")
t.check_expect(TEST_TODO_1.get_date(), "01-02-1234", "ToDo.set_date('01-02-1234')")

TEST_TODO_2.set_date("12-31-9999")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('12-31-9999')")

TEST_TODO_2.set_date("13-31-9999")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('13-31-9999') month out of bounds")

TEST_TODO_2.set_date("12-32-9999")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('12-32-9999') day out of bounds")

TEST_TODO_2.set_date("12-31-09999")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('12-31-09999') year length too long")

TEST_TODO_2.set_date("1-31-9999")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('1-31-9999') month length too short")

TEST_TODO_1.set_location("here")
t.check_expect(TEST_TODO_1.get_location(), "here", "ToDo.set_location('here')")

t.check_expect(TEST_TODO_1.get_description(), "ToDo 1 on 01-02-1234 @ here", "ToDo.get_description()")

TEST_TODO_1.set_date("")
t.check_expect(TEST_TODO_1.get_description(), "ToDo 1 @ here", "ToDo.set_date(''), ToDo.get_description()")

TEST_TODO_1.set_location("")
t.check_expect(TEST_TODO_1.get_description(), "ToDo 1", "ToDo.set_location(''), ToDo.get_description()")

t.check_expect(TEST_TODO_1.get_complete(), False, "ToDo.get_complete() -> False")
TEST_TODO_1.set_complete()
t.check_expect(TEST_TODO_1.get_complete(), True, "ToDo.set_complete(), ToDo.get_complete -> True")


# TASK TESTS

t.check_expect(TEST_TASK_1.num_subs(), 0, "Task.num_subs() -> 0")

t.check_expect(TEST_TASK_1.contains(TEST_TODO_3), False, "Task.contains() - False, empty")

TEST_TASK_1.add_doable(TEST_TODO_1)
t.check_expect(TEST_TASK_1.get_subs()[0], TEST_TODO_1, "Task.add_doable() - empty, add one")

TEST_TASK_1.add_doable(TEST_TODO_2)
t.check_expect(TEST_TASK_1.get_subs()[1], TEST_TODO_2, "Task.add_doable() - not empty, add new")

TEST_TASK_1.add_doable(TEST_TODO_1)
t.check_expect(TEST_TASK_1.num_subs(), 2, "Task.add_doable() -> ERROR: existing, Task.num_subs() -> 2")
t.check_expect(TEST_TASK_1.contains(TEST_TODO_1), True, "Task.contains() -> True")

TEST_TASK_1.remove_doable(TEST_TODO_1.get_description())
t.check_expect(TEST_TASK_1.contains(TEST_TODO_1), False,
               "Task.remove_doable() : contains = true, Task.contains() -> False, not empty")
