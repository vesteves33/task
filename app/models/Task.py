from app import database

class Task(database.Model):
    __tablename__ = 'tb_task'
    
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(180), nullable=False)
    description = database.Column(database.String(500), nullable=False)
    created_at = database.Column(database.Date)
  
    def __init__(self, title, description):
            self.title = title
            self.description = description 

    def loadTask(self):
      return {
          "id": self.id,
          "title": self.title,
          "description": self.description,
          "created_at": str(self.created_at.strftime('%d-%m-%Y'))
      }


    

  