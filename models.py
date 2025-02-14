# create_engine creates the connection to the database
from sqlmodel import Field, SQLModel, create_engine, Relationship
from enum import Enum
from datetime import date

class Bank(str, Enum): # Modified: Now inherits from `str` to store values as strings in the database. (Before it was just Enum)
    NUBANK = 'Nubank'
    SANTANDER = 'Santander'
    INTER = 'Inter'
    BRADESCO = 'Bradesco'

class Status(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'  

class Account(SQLModel, table=True):
    # Data will be add automatically by the database
    id: int = Field(primary_key=True)  
    # If the user does not provide the bank, the default will be nubank 
    bank: str = Field(default=Bank.NUBANK.value) # Now it's `str`, not `Enum`
    status: str = Field(default=Status.ACTIVE.value) # Now it's `str`, not `Enum`
    value: float

class Types(Enum): # Change it for str enum?? Not for now, but maybe in the future
    INPUT = 'Input'
    OUTPUT = 'Output'

class Historic(SQLModel, table=True):
    id: int = Field(primary_key=True)
    account_id: int = Field(foreign_key="account.id")
    account: Account = Relationship()
    typee: Types = Field(default=Types.INPUT)
    value: float
    date: date


sqlite_file_name = "database.db"  
sqlite_url = f"sqlite:///{sqlite_file_name}"  

engine = create_engine(sqlite_url, echo=False) # Change it for True to activate the logs on the terminal

def create_db_and_tables():  
    SQLModel.metadata.create_all(engine)  # Connection


if __name__ == "__main__":  
    create_db_and_tables()  
