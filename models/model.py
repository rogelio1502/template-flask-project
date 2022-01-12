from .module import db

class SomeModel(db.Model):

    __tablename__ = 'model'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_name = db.Column(db.String(120))
    age = db.Column(db.String(120))
    
    address = db.Column(db.String(120))    
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age':self.age,
            'address': self.address
        }