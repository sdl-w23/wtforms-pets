from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

def connect_db(app):
    """To connect to the database."""
    db.app = app
    db.init_app(app)



class Pet(db.Model):
    """Class for the pets."""
    __tablename__ = "pets"

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(50), 
                     nullable=False)
    
    species = db.Column(db.String(50), 
                        nullable=False)
    
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)

    photo_url = db.Column(db.String(200))
    
    age = db.Column(db.Integer)

    notes = db.Column(db.String)

    def show_image(self):
        
        return self.photo_url or GENERIC_IMAGE


    