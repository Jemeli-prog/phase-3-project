from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    feedbacks = relationship("Feedback", back_populates="customer", cascade="all, delete-orphan" )

    def __repr__(self):
        return f"<Customer(id={self.id}, name ={self.name}, email = {self.email})>"

class Company(Base):
    __tablename__  = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)

    feedbacks = relationship("Feedback", back_populates="company", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Company(id={self.id}, name={self.name})>"

class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    rating = Column(Integer)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))

    customer = relationship("Customer", back_populates="feedbacks")
    company = relationship("Company", back_populates="feedbacks")

    def __repr__(self):
        return f"<Feedback(id={self.id}, customer = {self.customer},  rating = {self.rating}, content = {self.content})>"