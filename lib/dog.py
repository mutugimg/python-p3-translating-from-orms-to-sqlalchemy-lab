from models import Dog
from sqlalchemy import create_engine

engine = create_engine('sqlite:///dogs.db')

def create_table(base, engine):
    base.metadata.create_all(engine)
    

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()
    
   
    
def find_by_name(session, name):
    dog_name = session.query(Dog).filter(Dog.name == name).first()
    return dog_name
...


def find_by_id(session, id):
    dog_id = session.query(Dog).filter(Dog.id == id).first()
    return dog_id
    
def find_by_name_and_breed(session, name, breed):
    dog_name_and_breed = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dog_name_and_breed

def update_breed(session, dog, breed):
    dog.breed = breed
    return session.query(Dog).update({Dog.breed: dog.breed})
