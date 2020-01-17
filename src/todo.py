""" todo.py
 
A simple todo app
"""


class Composite:
    """ Composite Pattern object """

    def __init__(self, description: str):
        """ Creates object instance """

        self.description = description

    def get_description(self) -> str:
        """ Returns description string """

        return self.description    


class ToDo(Composite):
    """ A to-do entry in a given task """

    def __init__(self, description: str):
        """ Creates object instance """

        super().__init__(description) 

    def __str__(self) -> str:
        return self.description
     

class Task(Composite):
    """ A task with a list of to-do entries """

    def __init__(self, description: str):
        """ Creates object instance """

        super().__init__(description)
        self.todos = []

    # !!!
    def contains(self, t: ToDo) -> bool:
        """ Returns True if ToDo is in self.todos """

        return False

    def add_todo(self, t: ToDo):
        """ Adds ToDo to self.todos

        checks if ToDo is already in list 
        and adds it if not.
        """

        if not self.contains(t):
            self.todos.append(t)

    def remove_todo(self, t: ToDo):
        """ Removes ToDo to self.todos

        checks if ToDo is already in list 
        and removes it if so.
        """

        if self.contains(t):
            self.todos.remove(t)

    # !!!
    def __str__(self) -> str:
        return ""    


class ToDoTracker:
    """ Main app ui 
    
    Run with self.main()
    """

    def __init__(self):
        """ Creates object instance """

        self.root = Task("ToDo Tracker")

    # !!!
    def main(self):
        """ Runs main ui """

        print("ToDo Tracker")


if __name__ == "__main__":
    ToDoTracker().main()
