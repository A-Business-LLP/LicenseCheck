from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Robot

engine = create_engine("sqlite:///robots.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

def get_robot_status(id: int) -> bool:
    with SessionLocal() as session:
        robot = session.get(Robot, id)
        if robot:
            return robot.status
        else:
            return None
