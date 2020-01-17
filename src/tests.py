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
    def check_expect(self, actual, expected):
        if expected == actual:
            print("Test Passed")
        else:
            print("Test Failed: Expected: " + str(expected) + " Actual: " + str(actual))


# Test Area #  

t = Test()


print("TEST: Task.add_todo() - empty, add one")         
TEST_TASK_1.add_todo(TEST_TODO_1)
t.check_expect(TEST_TASK_1.nodes[0], TEST_TODO_1)

print("TEST: Task.add_todo() - not empty, add new")         
TEST_TASK_1.add_todo(TEST_TODO_2)
t.check_expect(TEST_TASK_1.nodes[1], TEST_TODO_2)

print("TEST: Task.num_todos() - 2") 
t.check_expect(TEST_TASK_1.num_todos(), 2)

print("TEST: Task.add_todo() - not empty, add existing")         
TEST_TASK_1.add_todo(TEST_TODO_1)
t.check_expect(TEST_TASK_1.num_todos(), 2)

print("TEST: Task.contains() - True") 
t.check_expect(TEST_TASK_1.contains(TEST_TODO_1), True)

print("TEST: Task.contains() - False") 
t.check_expect(TEST_TASK_1.contains(TEST_TODO_3), False)

print("TEST: Task.remove_todo() - contains = true") 
TEST_TASK_1.remove_todo(TEST_TODO_1)
t.check_expect(TEST_TASK_1.contains(TEST_TODO_1), False)

# Test ToDoTracker.print_task()
TEST_TRACKER.root.add_todo(TEST_TASK_1)
TEST_TRACKER.print_task(TEST_TRACKER.root, TEST_TRACKER.indent_level)
