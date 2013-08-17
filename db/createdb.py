from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#~ from sqlalchemy.ext.declarative import declarative_base
from model.posts import Post

engine = create_engine('sqlite:///blask.db')

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

posts = []
posts.append(Post('Post numero Uno','Primer post para el blog'))
posts.append(Post('Post numero Dos','Segundo post para el blog'))
for post in posts:
     session.add(post)

#~ Base = declarative_base()


session.commit()
session.close()
