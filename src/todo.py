""" todo.py
 
A simple todo app
"""


class Composite:
    """ Composite Pattern object """

    def __init__(self, description: str):
        """ Creates object instance """

        self.description = description
        self.nodes = []

    def get_description(self) -> str:
        """ Returns description string """

        return self.description 

    def get_nodes(self) -> list:
        """ Returns list of child nodes """

        return self.nodes

    def __str__(self) -> str:
        """ Returns string for printing object """

        return self.description


class ToDo(Composite):
    """ A to-do entry in a given task """

    def __init__(self, description: str):
        """ Creates object instance """

        super().__init__(description) 


class Task(Composite):
    """ A task with a list of to-do entries """

    def __init__(self, description: str):
        """ Creates object instance """

        super().__init__(description)

    def num_todos(self) -> int:
        """ Returns the number of to-dos in task """

        return self.nodes.__len__()

    def contains(self, t: ToDo) -> bool:
        """ Returns True if ToDo is in self.todos """

        for todo in self.nodes:
            if t.get_description() == todo.get_description():
                return True
        return False

    def add_todo(self, t: ToDo):
        """ Adds ToDo to self.todos

        checks if ToDo is already in list 
        and adds it if not.
        """

        if not self.contains(t):
            self.nodes.append(t)

    def remove_todo(self, t: ToDo):
        """ Removes ToDo to self.todos

        checks if ToDo is already in list 
        and removes it if so.
        """

        if self.contains(t):
            self.nodes.remove(t)  


class ToDoTracker:
    """ Main app ui 
    
    Run with self.main()
    """

    def __init__(self):
        """ Creates object instance """

        self.root = Task("ToDo Tracker")
        self.indent_level = "  "

    # !!!
    def main(self):
        """ Runs main ui """

        print()
        print("  ToDo Tracker")
        print("-----------------")
        print("type 'h' for help")
        self.get_input()

    def print_task(self, task, indent):
        """ Prints the description and to-dos for task """

        print(indent + str(task))
        for entry in task.get_nodes():
            self.print_task(entry, indent + self.indent_level)

    def print_all(self):
        """ Prints all tasks and to-dos """

        self.print_task(self.root, "")

    def get_input(self) -> str:
        """ Get and Return input from user """
        
        print()
        inpt = input('>>> ')
        print()
        return inpt


if __name__ == "__main__":
    ToDoTracker().main()
