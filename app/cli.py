from app.db import SessionLocal, engine
from app.models import Base, Customer, Company, Feedback
from sqlalchemy.exc import IntegrityError

def create_tables():
    Base.metadata.create_all(bind=engine)

def menu():
    print("\n--- Customer Feedback System ---")
    print("1. Create Customer")
    print("2. Create Company")
    print("3. Create Feedback")
    print("4. List Customers")
    print("5. List Companies")
    print("6. List Feedbacks")
    print("7. Exit")

def create_customer(session):
    name = input("Enter customer name: ").strip()
    email = input("Enter customer email: ").strip()

    customer = Customer(name=name, email=email)
    session.add(customer)
    try:
        session.commit()
        print("Customer created successfully!")
    except IntegrityError:
        session.rollback()
        print("Error: Email must be unique.")

def create_company(session):
    name = input("Enter company name: ").strip()
    description = input("Enter company description: ").strip()

    company = Company(name=name, description=description)
    session.add(company)
    try:
        session.commit()
        print("Company created successfully!")
    except IntegrityError:
        session.rollback()
        print("Error: Company name must be unique.")

def create_feedback(session):
    customer_id = input("Enter customer ID: ").strip()
    company_id = input("Enter company ID: ").strip()
    content = input("Enter feedback content: ").strip()
    rating = input("Enter rating (1-5): ").strip()

    try:
        rating = int(rating)
        if rating < 1 or rating > 5:
            raise ValueError
    except ValueError:
        print("Invalid rating, must be an integer between 1 and 5.")
        return

    feedback = Feedback(customer_id=customer_id, company_id=company_id, content=content, rating=rating)
    session.add(feedback)
    try:
        session.commit()
        print("Feedback created successfully!")
    except IntegrityError:
        session.rollback()
        print("Error: Invalid customer or company ID.")

def list_customers(session):
    customers = session.query(Customer).all()
    for c in customers:
        print(c)

def list_companies(session):
    companies = session.query(Company).all()
    for comp in companies:
        print(comp)

def list_feedbacks(session):
    feedbacks = session.query(Feedback).all()
    for f in feedbacks:
        print(f)

def main():
    create_tables()
    session = SessionLocal()
    while True:
        menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            create_customer(session)
        elif choice == "2":
            create_company(session)
        elif choice == "3":
            create_feedback(session)
        elif choice == "4":
            list_customers(session)
        elif choice == "5":
            list_companies(session)
        elif choice == "6":
            list_feedbacks(session)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

    session.close()

if __name__ == "__main__":
    main()

