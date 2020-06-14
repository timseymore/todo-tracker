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
        print()


t = Test()


# TO-DO TESTS

# set_date() tests
# 
# Notes on set_date() tests:
# - a date should follow the format "MM-DD-YYYY" ; any other format should fail to change date
# - the "-" are unimportant, meaning that they may be replaced with any character ie: "12,15,1567" is considered valid
# - dates with the above circumstances should have "-" as the final result for dividers
# - ie: the above would be changed to "12-15-1567" in set_date()
# - the Month must be a 2-digit integer (01 - 12)
# - the Day must be a 2-digit integer (01 - 31)
# - the Year must be a 4-digit integer (0001 - 9999) ; no year zero ; app is meant to be used with modern day dates only

TEST_TODO_1.set_date(101)
t.check_expect(TEST_TODO_1.get_date(), "", "ToDo.set_date(101) - invalid argument type given")

TEST_TODO_1.set_date("01-01-0001")
t.check_expect(TEST_TODO_1.get_date(), "01-01-0001", "ToDo.set_date('01-02-1234') - valid lower bounds")

TEST_TODO_1.set_date("06-15-5432")
t.check_expect(TEST_TODO_1.get_date(), "06-15-5432", "ToDo.set_date('06,15,5432') - valid middle / change previous")

TEST_TODO_2.set_date("12-31-9999")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('12-31-9999') - valid upper bounds")

TEST_TODO_2.set_date("00-31-9999")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('1-31-9999') month out of bounds - under")

TEST_TODO_2.set_date("13-31-9999")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('13-31-9999') month out of bounds - over")

TEST_TODO_2.set_date("12-00-9999")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('12-32-9999') day out of bounds - under")

TEST_TODO_2.set_date("12-32-9999")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('12-32-9999') day out of bounds - over")

TEST_TODO_2.set_date("01-31-0000")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('01-31-0000') try year zero")

TEST_TODO_2.set_date("12-31-12345")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('12-31-12345') year length too long")

TEST_TODO_2.set_date("01-31-123")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('01-31-123') year length too short")

TEST_TODO_2.set_date("1-31-9999")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('1-31-9999') month length too short")

TEST_TODO_2.set_date("1-1-9999")
t.check_expect(TEST_TODO_2.get_date(), "12-31-9999", "ToDo.set_date('1-31-9999') day length too short")

TEST_TODO_1.set_date("06,15,5432")
t.check_expect(TEST_TODO_1.get_date(), "06-15-5432", "ToDo.set_date('06,15,5432') - valid with comma divider")



# set_location() tests
TEST_TODO_1.set_location("here")
t.check_expect(TEST_TODO_1.get_location(), "here", "ToDo.set_location('here') - valid")

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
