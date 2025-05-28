from app.db import SessionLocal, engine
from app.models import Base, Customer, Company, Feedback

def seed():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()

    # Clear existing data (optional)
    session.query(Feedback).delete()
    session.query(Customer).delete()
    session.query(Company).delete()
    session.commit()

    # Create some sample customers
    customers = [
        Customer(name="Alice Smith", email="alice@example.com"),
        Customer(name="Bob Johnson", email="bob@example.com"),
    ]

    # Create some sample companies
    companies = [
        Company(name="TechCorp", description="Technology company"),
        Company(name="Foodies", description="Food delivery service"),
    ]

    session.add_all(customers + companies)
    session.commit()

    # Create some sample feedbacks
    feedbacks = [
        Feedback(customer_id=customers[0].id, company_id=companies[0].id, content="Great service!", rating=5),
        Feedback(customer_id=customers[1].id, company_id=companies[1].id, content="Could be better.", rating=3),
    ]

    session.add_all(feedbacks)
    session.commit()
    session.close()

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed()
