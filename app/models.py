# this is the code to transform our class intoa sql table in the db
#user class represents a users stored int eh database
from typing import Optional 
from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db 

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates = 'author')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
# new model as a class - this represents the blog posts written by users. 
class Post(db.Model): 
    id: so.Mapped[int] = so.mapped_column(primary_key = True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(index = True, default = lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index = True)
    author: so.Mapped[User] = so.relationship(back_populates = 'posts')

    def __repr__(self): 
        return '<Post {}>'.format(self.body)