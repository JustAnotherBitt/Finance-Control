from models import *
from view import *
from datetime import datetime

class UI:
    def start(self):
        while True:
            print('''
            ===============================      
            Welcome to the Finance Control!
            ===============================
                  
            [1] -> Create account
            [2] -> Deactivate account
            [3] -> Transfer money
            [4] -> Move money
            [5] -> Total accounts
            [6] -> Filter history
            [7] -> Graphic
            [8] -> Exit program
                  ''')
            
            choice = int(input('Choose an option: '))

            if choice == 1:
                self._create_account()
            elif choice == 2:
                self._desactivate_account()
            elif choice == 3:
                self._transfer_balance() 
            elif choice == 4:
                self._move_money()
            elif choice == 5:
                self._total_accounts()
            elif choice == 6:
                self._filter_movements() 
            elif choice == 7:
                self._create_chart_by_account() # graphic
            elif choice == 8:
                break
            else:
                print("Invalid option.")
            
    def _create_account(self):
        print('Enter the name of one of the banks below:')
        for bank in Bank:
            print(f'- {bank.value}')
        
        bank = input().title()
        value = float(input('Enter the current amount available in the account: '))

        account = Account(bank=Bank(bank), value=value) 
        created_account = create_account(account)
        
        if created_account:
            print(f'''
              Account created successfully! 
              
              Bank: {bank}
              Amount: R${value}
              ''')

    def _desactivate_account(self):
        print('Choose the account you want to deactivate.')
        for i in list_accounts():
            if i.value == 0:
                print(f'{i.id} -> {i.bank} -> R$ {i.value}')

        account_id = int(input())

        try:
            deactivate_account(account_id)
            print('Account deactivated successfully.')
        except ValueError:
            print('This account still has a balance, make a transfer.')

    def _transfer_balance(self):
        print('Choose the account to withdraw the money.')
        for i in list_accounts():
            print(f'{i.id} -> {i.bank} -> R$ {i.value}')

        account_withdraw_id = int(input())

        print('Choose the account to send money to.')
        for i in list_accounts():
            if i.id != account_withdraw_id:
                print(f'{i.id} -> {i.bank} -> R$ {i.value}')

        account_send_id = int(input())

        value = float(input('Enter the value to transfer: '))
        transfer_balance(account_withdraw_id, account_send_id, value)
        print(f"Transfer of R${value} made successfully!")

    def _move_money(self):
        print('Choose the account.')
        for i in list_accounts():
            print(f'{i.id} -> {i.bank} -> R$ {i.value}')

        account_id = int(input())

        value = float(input('Enter the value moved:'))

        print('Select the type of movement')
        for typee in Types:
            print(f'- {typee.value}')
        
        typee = input().title()
        historic = Historic(account_id=account_id, typee=Types(typee), value=value, date=date.today())
        move_money(historic)
        print(f"{typee} of R${value} successfully made!")
    
    def _total_accounts(self):
        for i in list_accounts():
            print(f'{i.id} -> {i.bank} -> R$ {i.value} ({i.status})')
        print(f'Total value: R$ {total_accounts()}')

    def _filter_movements(self):
        start_date = input('Enter the start date: ')
        end_date = input('Enter the end date: ')

        try:
            start_date = datetime.strptime(start_date, '%m/%d/%Y').date()
            end_date = datetime.strptime(end_date, '%m/%d/%Y').date()
            
            search_histories = search_histories_between_dates(start_date, end_date)
            
            if search_histories:
                for i in search_histories_between_dates(start_date, end_date):
                    print(f'{i.typee.value} of R${i.value}')           
            else:
                print("History not found.")
            
        except ValueError:
            print("Dates must be in the format mm/dd/yyyy")
        

    def _create_chart_by_account(self):
        create_chart_by_account()

UI().start()