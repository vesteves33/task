class Status:
   def __init__(self, type):
       self.id = None
       self.type = type

   def getType(self):
       return self.type

   def setType(self, type):
       self.type = type 