class Task:
  def __init__(self,title, description):
      self.id = None
      self.title = title
      self.description = description

  def getTitle(self):
      return self.title

  def getDescription(self):
      return self.description

  def setTitle(self, title):
      self.title = title

  def setDescription(self, description):
      self.description = description  
