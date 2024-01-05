from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
hostname = os.getenv("DB_HOSTNAME")
database = os.getenv("DB_DATABASE")


Base = declarative_base()

class Table(Base):
    __tablename__ = 'jobs'  # Replace with your actual table name
    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    location = Column(String(128), nullable=False)
    salary = Column(Integer, nullable=False)
    currency = Column(String(10))
    responsibilities = Column(String(2000))
    requirements = Column(String(2000))

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{hostname}/{database}")
Session = sessionmaker(bind=engine)
def load_jobs_from_db():
    with Session() as read_session:
        # Query all records from the 'jobs' table
        results = read_session.query(Table).all()
        print(f"Result type: {type(results)}")
        print("Case 1: Existing Data - Read Operation")
        jobs = []
        for result in results:
            jobs.append(result.__dict__)

        return jobs