from todo import ToDo, Task

# Test Objects

TEST_TASK_1 = Task("Task 1")
TEST_TASK_2 = Task("Task 2")
TEST_TASK_3 = Task("Task 3")

TEST_TODO_1 = ToDo("ToDo 1")
TEST_TODO_2 = ToDo("ToDo 2")
TEST_TODO_3 = ToDo("ToDo 3")
TEST_TODO_4 = ToDo("ToDo 4")
TEST_TODO_5 = ToDo("ToDo 5")

class Test:
    def check_expect(self, expected, actual):
        if expected == actual:
            print("Test Passed")
        else:
            print("Test Failed: Expected: " + str(expected) + " Actual: " + str(actual))

class TestTask:
    pass


# Test Area #  

t = Test()

# TEST: Task.contains()

# TEST: Task.add_todo() - empty, add one         
TEST_TASK_1.add_todo(TEST_TODO_1)
t.check_expect(TEST_TASK_1.todos[0], TEST_TODO_1)

# TEST: Task.remove_todo()
