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
    def check_expect(expected, actual):
        if actual == expected:
            print("Test Passed")
        else:
            print("Test Failed: Expected: " + str(expected) + " Actual: " + str(actual))


t = Test()


# TO-DO TESTS

print("TEST: ToDo.set_date()")
TEST_TODO_1.set_date("01-02-1234")
t.check_expect(TEST_TODO_1.get_date(), "01-02-1234")
print()

print("TEST: ToDo.set_location()")
TEST_TODO_1.set_location("here")
t.check_expect(TEST_TODO_1.get_location(), "here")
print()

print("TEST: ToDo.get_description()")
t.check_expect(TEST_TODO_1.get_description(), "ToDo 1 on 01-02-1234 @ here")
TEST_TODO_1.set_date("")
t.check_expect(TEST_TODO_1.get_description(), "ToDo 1 @ here")
TEST_TODO_1.set_location("")
t.check_expect(TEST_TODO_1.get_description(), "ToDo 1")
print()

print("TEST: ToDo.set_complete()")
t.check_expect(TEST_TODO_1.get_complete(), False)
TEST_TODO_1.set_complete()
t.check_expect(TEST_TODO_1.get_complete(), True)
print()


# TASK TESTS

print("TEST: Task.add_doable() - empty, add one")
TEST_TASK_1.add_doable(TEST_TODO_1)
t.check_expect(TEST_TASK_1.get_subs()[0], TEST_TODO_1)
print()

print("TEST: Task.add_doable() - not empty, add new")
TEST_TASK_1.add_doable(TEST_TODO_2)
t.check_expect(TEST_TASK_1.get_subs()[1], TEST_TODO_2)
print()

print("TEST: Task.num_subs() - 2")
t.check_expect(TEST_TASK_1.num_subs(), 2)
print()

print("TEST: Task.add_doable() - not empty, add existing")
TEST_TASK_1.add_doable(TEST_TODO_1)
t.check_expect(TEST_TASK_1.num_subs(), 2)
print()

print("TEST: Task.contains() - True") 
t.check_expect(TEST_TASK_1.contains(TEST_TODO_1), True)
print()

print("TEST: Task.contains() - False") 
t.check_expect(TEST_TASK_1.contains(TEST_TODO_3), False)
print()

print("TEST: Task.remove_doable() - contains = true")
TEST_TASK_1.remove_doable(TEST_TODO_1.get_description())
t.check_expect(TEST_TASK_1.contains(TEST_TODO_1), False)
print()

# TODOTRACKER TESTS

print("TEST: ToDoTracker.print_all()")
TEST_TRACKER.root.add_doable(TEST_TASK_1)
TEST_TASK_1.add_doable(TEST_TODO_1)
TEST_TRACKER.root.add_doable(TEST_TASK_2)
TEST_TASK_2.add_doable(TEST_TODO_3)
TEST_TRACKER.root.add_doable(TEST_TASK_3)
TEST_TASK_2.add_doable(TEST_TODO_4)
TEST_TASK_3.add_doable(TEST_TODO_5)
TEST_TRACKER.print_all()
print()

print("TEST: ToDoTracker.print_task()")
TEST_TRACKER.print_task(TEST_TASK_1, "")
print()
