from modules.baseclass.BaseClass import BaseClass

class Task(BaseClass):
    """
    A class representing a Task, inheriting from BaseClass.
    """

    def __init__(self, task_id, name, description, status, due_date):
        """
        Initialize a Task instance with common attributes.
        """
        self.task_id = task_id
        self.name = name
        self.description = description
        self.status = status
        self.due_date = due_date

    def create(self):
        """
        Placeholder for creating a new task.
        """
        pass

    def read(self):
        """
        Placeholder for reading task details.
        """
        pass

    def update(self):
        """
        Placeholder for updating task details.
        """
        pass

    def delete(self):
        """
        Placeholder for deleting a task.
        """
        pass