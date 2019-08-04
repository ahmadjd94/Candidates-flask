# from sqlalchemy import Column, String, DateTime
#
# from app.db import Base
#
#
# class Admin(Base):
#     email = Column(String(255), unique=True, nullable=False)
#     password = Column(String(255), nullable=False)
#     registered_on = Column(DateTime, nullable=False)
#
#     def __init__(self, first_name, last_name, dob, yoe):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.date_of_birth = dob
#         self.years_of_experience = yoe
#
#     def __repr__(self):
#         return self.email
