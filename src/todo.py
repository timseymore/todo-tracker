""" todo.py
 
A simple todo app
"""

import os, sys, shutil

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

    def num_nodes(self) -> int:
        """ Returns the number of to-dos in task """

        return self.nodes.__len__()

    def contains(self, t: Composite) -> bool:
        """ Returns True if Composite is in self.nodes 
        
        Checks for Composite with matching description 
        and returns True if found
        """

        for node in self.nodes:
            if t.get_description() == node.get_description():
                return True
        return False

    def add_node(self, t: Composite):
        """ Adds Composite to self.nodes

        checks if Composite is already in list 
        and adds it if not found.
        """

        if not self.contains(t):
            self.nodes.append(t)
        else:
            print("ERROR: Node already exists in task")

    def remove_node(self, t: Composite):
        """ Removes Composite to self.nodes

        checks for Composite with matching description 
        and removes it if found.
        """

        for node in self.nodes:
            if t.get_description() == node.get_description():
                self.nodes.remove(node)
                return
        print("ERROR: Node not found in task")


class ToDoTracker:
    """ Main app ui 
    
    Run with self.main()
    """

    def __init__(self):
        """ Creates object instance """

        self.root = Task("ToDo Tracker")
        self.indent_level = "  "
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
        # setup  
              
        self.load_from_disk()
        current_task = self.root

        print()
        print("  ToDo Tracker")
        print("-----------------")
        print("type 'help' for help")        
        
        # main loop
        while True:
            # get user input
            choice = self.get_input()

            # handle user input
            if choice == 'exit':
                print("Save work? (y/n)")
                save = input('>>> ')
                while save not in ['y', 'n']:
                    save = input('>>> ')
                if save == 'y':
                    self.delete_all()
                    self.save_to_disk()
                    print("Saved to disk")
                print("Exiting program")
                sys.exit()
            elif choice == 'help':
                self.show_help_menu() 
            elif choice == 'ls':
                self.print_task(current_task, "") 
            elif choice == 'pwt':
                print(current_task)
            elif choice == 'ct':
                print("Change to:")
                current_task = self.change_task(input('>>> '), current_task)
            elif choice == 'addtask':
                print("New Task:")
                temp = Task(input('>>> '))
                self.root.add_node(temp)
            elif choice == 'addtodo':
                print("New To-do:")
                temp = ToDo(input('>>> '))
                current_task.add_node(temp)  
            elif choice == 'rmtask':
                print("Task to remove:")
                self.root.remove_node(input('>>> ')) 
            elif choice == 'rmtodo':
                print("To-do to remove:")
                current_task.remove_node(input('>>> '))       

    def show_help_menu(self):
        """ Print help menu to console """

        print("       COMMANDS")
        print("=======================")
        print("| exit : Exit program")
        print("| help : Help Menu")
        print("| ls : List current working task and todos")
        print("| ct : Change current working task")
        print("| pwt : Show present working task")
        print("| addtask : Add new task to tracker")  
        print("| addtodo : Add new to-do to current task") 
        print("| rmtask : Delete task from tracker") 
        print("| rmtodo : Delete to-do from current task")    

    def change_task(self, task: str, current: Task) -> Task:
        """ Change current working task 
        
        Returns new task if it exists in current, 
        returns root task otherwise and prints Error message
        """
        for t in current.nodes:
            if task == t.get_description():
                return t
        print("ERROR: Task does not exist in current - changing to root")
        return self.root

    def print_task(self, task, indent):
        """ Prints the description and to-dos for task """

        print(indent + str(task))
        for entry in task.get_nodes():
            self.print_task(entry, indent + self.indent_level)

    def print_all(self):
        """ Prints all tasks and to-dos """

        self.print_task(self.root, "")

    def get_input(self) -> str:
        """ Get and Return input from user 
        
        Continue prompting for input until valid command is entered
        RETURN: input
        """
        
        print()
        inpt = input('>>> ')
        while not self.is_valid_command(inpt):
            inpt = input('>>> ')
        print()
        return inpt

    def is_valid_command(self, c) -> bool:
        """ Check if command is in list of commands
        
        RETURN: True if command is valid, False otherwise 
        """

        for command in self.commands:
            if c == command:
                return True
        return False

    def save_to_disk(self):
        """ Save ToDoTracker object to disk """

        root = self.root.get_description()
        os.mkdir(root)
        for task in self.root.get_nodes():
            tempdir = task.get_description()
            os.mkdir(root + "\\" + tempdir)
            for todo in task.get_nodes():
                tempfile = todo.get_description()
                with open(root + "\\" + tempdir + "\\" + tempfile, 'w') as f:
                    f.write(tempfile)
                    f.close()

    def load_from_disk(self):
        index = 0
        for task in os.listdir("./ToDo Tracker"):
            if os.path.isdir(task):
                self.root.add_node(Task(task))                
                for todo in os.listdir(task):
                    self.root.nodes[index].add_node(ToDo(todo))
                index += 1   
    
    def delete_all(self):
        try:
            shutil.rmtree("./ToDo Tracker") 
        except:
            print('Error while deleting directory')
        




if __name__ == "__main__":
    ToDoTracker().main()
