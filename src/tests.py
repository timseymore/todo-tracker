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
        print()
        print("Test: " + message + ": ", end="")
        if actual != expected:
            print("FAILED: Expected: " + str(expected) + " Actual: " + str(actual))
        else:
            print("PASSED")


# TO-DO TESTS

# get_date() / set_date() tests

Test.check_expect(TEST_TODO_1.get_date(), "", "ToDo.get_date() - Default date")

TEST_TODO_1.set_date(101)
Test.check_expect(TEST_TODO_1.get_date(), "", "ToDo.set_date(101) - invalid argument type given")

TEST_TODO_1.set_date("01-01-0001")
Test.check_expect(TEST_TODO_1.get_date(), "01-01-0001",
                  "ToDo.set_date('01-01-0001') ToDo.get_date() - valid lower bounds")

TEST_TODO_1.set_date("06-15-5432")
Test.check_expect(TEST_TODO_1.get_date(), "06-15-5432", "ToDo.set_date('06,15,5432') - valid middle / change previous")

TEST_TODO_2.set_date("12-31-9999")
Test.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('12-31-9999') - valid upper bounds")


# set_location() tests
TEST_TODO_1.set_location("here")
Test.check_expect(TEST_TODO_1.get_location(), "here", "ToDo.set_location('here') - valid")

Test.check_expect(TEST_TODO_1.get_description(), "ToDo 1 on 06-15-5432 @ here", "ToDo.get_description()")

TEST_TODO_1.set_date("")
Test.check_expect(TEST_TODO_1.get_description(), "ToDo 1 @ here", "ToDo.set_date(''), ToDo.get_description()")

TEST_TODO_1.set_location("")
Test.check_expect(TEST_TODO_1.get_description(), "ToDo 1", "ToDo.set_location(''), ToDo.get_description()")

Test.check_expect(TEST_TODO_1.get_complete(), False, "ToDo.get_complete() -> False")
TEST_TODO_1.set_complete()
Test.check_expect(TEST_TODO_1.get_complete(), True, "ToDo.set_complete(), ToDo.get_complete -> True")


# TASK TESTS
Test.check_expect(TEST_TASK_1.num_subs(), 0, "Task.num_subs() -> 0")

Test.check_expect(TEST_TASK_1.contains(TEST_TODO_3), False, "Task.contains() - False, empty")

TEST_TASK_1.add_doable(TEST_TODO_1)
Test.check_expect(TEST_TASK_1.get_subs()[0], TEST_TODO_1, "Task.add_doable() - empty, add one")

TEST_TASK_1.add_doable(TEST_TODO_2)
Test.check_expect(TEST_TASK_1.get_subs()[1], TEST_TODO_2, "Task.add_doable() - not empty, add new")

TEST_TASK_1.add_doable(TEST_TODO_1)
Test.check_expect(TEST_TASK_1.num_subs(), 2, "Task.add_doable() -> ERROR: existing, Task.num_subs() -> 2")
Test.check_expect(TEST_TASK_1.contains(TEST_TODO_1), True, "Task.contains() -> True")

TEST_TASK_1.remove_doable(TEST_TODO_1.get_description())
Test.check_expect(TEST_TASK_1.contains(TEST_TODO_1), False,
                  "Task.remove_doable() : contains = true, Task.contains() -> False, not empty")
