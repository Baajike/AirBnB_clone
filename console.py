#!/usr/bin/python3
"""
Module for the console.
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the Holberton B&B.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Override emptyline method to do nothing on empty input.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

        try:
            cls = classes[arg]
        except KeyError:
            print("** class doesn't exist **")
            return

        instance = cls()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
        else:
            print(instances[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
        else:
            del instances[key]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances.
        """
        args = shlex.split(arg)
        instances = storage.all()

        if not args:
            print([str(instance) for instance in instances.values()])
            return

        class_name = args[0]
        if class_name not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        print([str(instance) for key, instance in instances.items() if key.startswith(class_name)])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        instance = instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

