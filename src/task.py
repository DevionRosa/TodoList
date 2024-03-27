import tasklist

class tasks:
    
    def __init__(self, title = None, prio = 0, due_date = None, desc = None, completed = False):
        self.title = title
        self.prio = prio
        self.due_date = due_date
        self.desc = desc
        self.completed = completed
    
    def mark_as_completed(self):
        self.completed = True
        tasklist.remove_task(self)
    
    
        
    
        

        