from datetime import datetime, timezone
#This was created to keep a copy of the databases in the main page but instead we use the databses directly 
#the only function used here is the one to create a object and then transform it into json form 
class Task:
    def __init__(self, task_title, description):
        self.date_created = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S") 
        self.task_title = task_title
        self.done = False  # Default value is False
        self.description = description

    def mark_done(self):
        #change done to true as the to do was complated
        self.done = True

    def to_dict(self):
        #convert task object to noSQL 
        return {
            "date_created": self.date_created,
            "task_title": self.task_title,
            "done": self.done,
            "description": self.description
        }

    def __str__(self):
        """String representation of the Task object"""
        return f"Task(title={self.task_title}, done={self.done}, created={self.date_created})"
