from flask import current_app
from sqlalchemy.orm import defaultload
from app.models.customers import Customer
from app import db

class Video(db.Model):
    video_id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String)
    release_date = db.Column(db.DateTime,nullable=True)
    total_inventory = db.Column(db.Integer, default=0)
    available_inventory = db.Column(db.Integer, default=0)
    
    def video_to_json(self):
        return {
            "id":self.video_id,
            "title":self.title,
            "release_date":self.release_date,
            "total_inventory":self.total_inventory,
            'available_inventory':self.available_inventory
        }