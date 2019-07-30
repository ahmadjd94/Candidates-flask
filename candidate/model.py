from sqlalchemy import Column, Integer, String, Date


class Candidate(Base):
    __tablename__ = 'candidates'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), unique=True)
    last_name = Column(String(120), unique=True)
    date_of_birth = Column(Date)
    years_of_experience = Column(Integer())

    def __init__(self, first_name, last_name,dob, yoe):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = dob
        self.years_of_experience = yoe

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'
