from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String, db.CheckConstraint('phone_number > 10'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        if len(name) > 0:
            return name
        else:
            raise ValueError

    @validates('phone_number')
    def validate_pn(self, key, phone_number):
        if len(phone_number) > 10:
            raise ValueError
        return phone_number
        
    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError
        return content
    
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError
        return summary
        
    @validates('category')
    def validate_category(self, key, category):
        if category == 'Fiction':
            return category
        else:
            if category == 'Non-Fiction':
                return category
        raise ValueError
    
    @validates('title')
    def validate_title(self, key, title):
        if title == "Won't Believe":
            return title
        else:
            if title == 'Secret':
                return title
            else:
                if title == 'Top':
                    return title
                else:
                    if title == 'Guess':
                        return title
        raise ValueError
        
    

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
