import task

class tasklists:
    
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task):
        self.tasks.remove(task)
        
    def organize_task(self):
       self.tasks = sorted(self.tasks, key=lambda x: (-x.prio, x.title))
    
    
        
        
        
    
    