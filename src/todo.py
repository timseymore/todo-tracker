"""
todo.py
 
A simple todo app

"""

# Data Definitions #

class Composite:
    """
        Composite Pattern object
    """
    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description    

class ToDo(Composite):
    """
        A to-do entry in a given task
    """
    def __init__(self, description):
        super().__init__(description) 

    def __str__(self):
        return self.description
     

class Task(Composite):
    """
        A task with a list of to-do entries
    """
    def __init__(self, description):
        super().__init__(description)
        self.todos = []

    # !!!
    def contains(self, t) -> bool:
        return False

    # !!!
    def add_todo(self, t):
        if not self.contains(t):
            self.todos.append(t)

    def remove_todo(self, t):
        if self.contains(t):
            self.todos.remove(t)

    # !!!
    def __str__(self) -> str:
        return ""    

class ToDoTracker:
    def __init__(self):
        self.root = Task("ToDo Tracker")

    # !!!
    def main(self):
        print("ToDo Tracker")





if __name__ == "__main__":
    ToDoTracker().main()
