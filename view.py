from datetime import date, timedelta
from models import Account, Historic, Types, engine, Bank, SQLModel, Status
# Session = quick connection with the database
from sqlmodel import Session, select

SQLModel.metadata.create_all(engine)  # Connection
# account will be always an instance from the Account class
def create_account(account: Account):
    # Connect to the database
    with Session(engine) as session:
        # Checks if the account exists
        statement = select(Account).where(Account.bank==account.bank)
        # Returns all the results
        results = session.exec(statement).all()
        if results:
            print("There is already an account at that bank!")
            return
        # Add the account to the middle tier
        session.add(account) 
        # Takes what was done in the intermediate layer and makes it effective in the database (saves)
        session.commit() 
        return account
    
def list_accounts():
    with Session(engine) as session:
        statement = select(Account)
        results = session.exec(statement).all()
    return results

def deactivate_account(id): # Needs the id as a parameter because it will exclude a specific account
    with Session(engine) as session:
        statement = select(Account).where(Account.id==id)
        account = session.exec(statement).first()
        if account.value > 0:
            raise ValueError('This account still has a balance, it is not possible to deactivate it.')
        account.status = Status.INACTIVE
        session.commit()
        
def transfer_balance(id_output_account, id_input_account, value):
    with Session(engine) as session:
        # Output account
        statement = select(Account).where(Account.id==id_output_account)
        output_account = session.exec(statement).first()
        if output_account.value < value:
            raise ValueError('Insufficient balance')
        
        # Input account
        statement = select(Account).where(Account.id==id_input_account)
        input_account = session.exec(statement).first()

        # Transference
        output_account.value -= value
        input_account.value += value
        session.commit()


def move_money(historic: Historic):
    with Session(engine) as session:
        statement = select(Account).where(Account.id==historic.account_id)
        account = session.exec(statement).first()
        
        
        if not account:
            raise ValueError("Account not found")

        if account.status != Status.ACTIVE:
            raise ValueError("Account is not active")

        if historic.typee == Types.INPUT:
            account.value += historic.value
            
        else:
            if account.value < historic.value:
                raise ValueError("Insufficient balance")
            account.value -= historic.value

        session.add(historic)
        session.commit()
        return historic
    
def total_accounts():
    with Session(engine) as session:
        statement = select(Account)
        accounts = session.exec(statement).all()

    total = 0
    for account in accounts:
        total += account.value

    return float(total)

def search_histories_between_dates(start_date: date, end_date: date):
    with Session(engine) as session:
        statement = select(Historic).where(
            Historic.date >= start_date,
            Historic.date <= end_date
        )
        resultados = session.exec(statement).all()
        return resultados

# account = Account(value=0, bank=Bank.NUBANK.value)  # Modified: Now uses `.value` to get the enum string
# create_account(account)

# deactivate_account(4)

# transfer_balance(2, 1, 10)

# historic = Historic(account_id=1, typee=Types.INPUT, value=10, date=date.today())
# move_money(historic)

# print(total_accounts())
    
# x=search_histories_between_dates(date.today() - timedelta(days=1), date.today() + timedelta(days=1))
# print(x)


def create_chart_by_account():
    with Session(engine) as session:
        statement = select(Account).where(Account.status==Status.ACTIVE)
        accounts = session.exec(statement).all()
        banks = [i.bank for i in accounts]
        total = [i.value for i in accounts]
        import matplotlib.pyplot as plt
        plt.bar(banks, total)
        plt.show()
        
# create_chart_by_account()
