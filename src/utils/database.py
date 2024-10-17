import os
from sqlalchemy import create_engine, orm
from models import question, answer

# Database connection
MYSQL_HOST=os.getenv('MYSQL_HOST')
MYSQL_PORT=os.getenv('MYSQL_PORT')
MYSQL_USER=os.getenv('MYSQL_USER')
MYSQL_DATABASE=os.getenv('MYSQL_DATABASE')
MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD')
connection=f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
engine = create_engine(connection, echo=True)

# Init Models
question.Base.metadata.create_all(engine)
answer.Base.metadata.create_all(engine)

session = orm.sessionmaker(bind=engine)()
