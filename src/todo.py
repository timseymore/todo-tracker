""" To-Do Tracker
 
A simple task manager console app

- 2019 Tim Seymore
"""

import pickle
import sys


class Doable:
    """ Composite Pattern object """

    def __init__(self, description: str):
        """ Creates object instance """

        self.complete = False
        self.description = description
        self.nodes = []  # TODO: remove this field

    def get_complete(self) -> bool:
        """ Getter method """

        return self.complete

    def get_description(self) -> str:
        """ Returns description string """

        return self.description

    # TODO : remove this method
    def get_subs(self) -> list:
        """ Returns list of child nodes """

        return self.nodes

    def set_complete(self):
        """ sets complete to True """

        self.complete = True

    def display(self, indent_space: str):
        """ Prints Doable to console """

        pass

    def __str__(self) -> str:
        """ Returns string for printing object """

        return self.description


class ToDo(Doable):
    """ A to-do entry in a given task
    
     - description: String ; description of To-do
     - date: String ; date to complete To-do
     - location: String ; time to complete To-do
     """

    def __init__(self, description: str, date="", location=""):
        """ Constructor method """

        super().__init__(description) 
        self.date = date
        self.location = location

    # Getters
    def get_date(self) -> str:
        """ Getter method """

        return self.date

    def get_location(self) -> str:
        """ Getter method """

        return self.location

    # Setters
    def set_date(self, d: str):
        """ Setter method """

        self.date = d

    def set_location(self, t: str):
        """ Setter method """

        self.location = t

    def get_description(self) -> str:
        date_str = ""
        loc_str = ""
        if not self.date == "":
            date_str = " on " + self.date
        if not self.location == "":
            loc_str = " @ " + self.location
        return self.description + date_str + loc_str

    def set_complete(self):
        """ Sets complete to True unless already True """

        if not self.complete:
            self.complete = True

    def display(self, indent_space: str):
        """ Prints To-do to console """

        return self.__str__()


class Task(Doable):
    """ A task with a list of Doables """

    def __init__(self, description: str):
        """ Creates object instance """

        super().__init__(description)
        self.subDoablesComplete = False
        # self.subs = self.nodes  # TODO: subs should only exist in this class

    def num_subs(self) -> int:
        """ Returns the number of sub-components in task """

        return self.nodes.__len__()

    def contains(self, t: Doable) -> bool:
        """ Returns True if Component is in self.nodes
        
        Checks for Component with matching description
        and returns True if found, False otherwise
        """

        for sub in self.nodes:
            if t.get_description() == sub.get_description():
                return True
        return False

    def add_doable(self, t: Doable):
        """ Adds Component to self.subs

        checks if Component is already in list
        and adds it if not found.
        """

        if not self.contains(t):
            self.nodes.append(t)
        else:
            print("ERROR: Doable already exists in current task")

    def remove_doable(self, t: str):
        """ Removes Component from self.subs

        checks for Component with matching description
        and removes it if found.
        """

        for sub in self.nodes:
            if t == sub.get_description():
                self.nodes.remove(sub)
                return
        print("ERROR: Doable not found in task")

    def display(self, indent_space: str):
        """ Prints Task and all subs to console """
        return self.__str__()


class ToDoTracker:
    """ Main app ui 
    
    Run with self.main()
    """

    def __init__(self):
        """ Creates object instance """

        self.root = Task("ToDo Tracker")
        self.indent_level = " " * 2
        self.commands = [
            'help',
            'exit',
            'addtask',
            'addtodo',
            'rmtask',
            'rmtodo',
            'ls',
            'ct',
            'pwt'
        ]

    def main(self):
        """ Runs main ui """

        self.load_from_disk()
        current_task = self.root

        print()
        print("  ToDo Tracker")
        print("-----------------")
        print("type 'help' for help")

        while True:
            choice = self.get_input()
            current_task = self.handle_input(choice, current_task)

    def get_input(self) -> str:
        """ Get and Return input from user

        Continue prompting for input until valid command is entered
        RETURN: valid input
        """

        print()
        inpt = input('>>> ')
        while not self.is_valid_command(inpt):
            inpt = input('>>> ')
        print()
        return inpt

    def handle_input(self, inp: str, current: Task) -> Task:
        """ Handle given user input

         - inp: input choice
         - current: current task
         Return: new current task
         """

        if inp == 'exit':
            self.exit_program()
            sys.exit()
        elif inp == 'help':
            self.show_help_menu()
        elif inp == 'ls':
            self.print_task(current, "")
        elif inp == 'pwt':
            print(current)
        elif inp == 'ct':
            print("Change to:")
            current = self.change_task(input('>>> '), current)
        elif inp == 'addtask':
            print("New Task:")
            current.add_doable(Task(input('>>> ')))
        elif inp == 'addtodo':
            print("New To-do:")
            current.add_doable(ToDo(input('>>> ')))
        elif inp == 'rmtask':
            print("Task to remove:")
            current.remove_doable(input('>>> '))
        elif inp == 'rmtodo':
            print("To-do to remove:")
            current.remove_doable(input('>>> '))
        return current

    def is_valid_command(self, c) -> bool:
        """ Check if command is in list of commands

        RETURN: True if command is valid, False otherwise
        """

        for command in self.commands:
            if c == command:
                return True
        return False

    def change_task(self, task: str, current: Task) -> Task:
        """ Change current working task

        RETURN: new task if it exists in current or
                root task otherwise and prints Error message
        """

        for t in current.nodes:
            if task == t.get_description():
                return t
        if task != self.root.get_description():
            print("ERROR: task not found in current working task - changing to 'ToDo Tracker'")
        return self.root

    def print_task(self, task, indent):
        """ Prints the description and to-dos for task """

        print(indent + str(task))
        for entry in task.get_subs():
            self.print_task(entry, indent + self.indent_level)

    def print_all(self):
        """ Prints all tasks and to-dos """

        self.print_task(self.root, "")

    def save_to_disk(self):
        """ Save ToDoTracker object to file """

        try:
            temp_file = open("data.obj", 'wb')
            pickle.dump(self.root, temp_file)
            temp_file.close()
        except FileNotFoundError:
            print("ERROR: FileNotFound")

    def load_from_disk(self):
        """ Load saved data from file """

        try:
            temp_file = open('data.obj', 'rb')
            self.root = pickle.load(temp_file)
            temp_file.close()
        except FileNotFoundError:
            print("ERROR: FileNotFound")

    def exit_program(self):
        """ Prompt to save and exit program """

        print("Save work? (y/n)")
        save = input('>>> ')
        while save not in ['Yes', 'yes', 'Y', 'y', 'No', 'no',  'N', 'n']:
            save = input('>>> ')
        if save == 'y':
            self.save_to_disk()
            print("Saved to disk")
        print("Exiting program")

    @staticmethod
    def show_help_menu():
        """ Print help menu to console """

        print("                   COMMANDS")
        print("=================================================")
        print(" | exit    : Exit program")
        print(" | help    : Help Menu")
        print(" | ls      : List current working task and todos")
        print(" | ct      : Change current working task")
        print(" | pwt     : Show present working task")
        print(" | addtask : Add new task to current task")
        print(" | addtodo : Add new to-do to current task")
        print(" | rmtask  : Delete task from current task")
        print(" | rmtodo  : Delete to-do from current task")


if __name__ == "__main__":
    ToDoTracker().main()
