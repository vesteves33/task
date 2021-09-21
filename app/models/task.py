from app import database
from datetime import datetime

class Task(database.Model):    
    __tablename__ = 'tb_task'
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(180), nullable=False)
    description = database.Column(database.String(500), nullable=False)
    created_at = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)

    def returnTask(self):
      return {
          "id": self.id,
          "title": self.title,
          "description": self.description,
          "created_at": str(self.created_at.strftime('%d-%m-%Y'))
      }


    

  