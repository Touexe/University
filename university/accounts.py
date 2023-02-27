from .models import account
from .database import accounts_table

class Accounts:
    def create_account(self, account: account) -> dict:
        data = accounts_table.create(account.dict())
        accounts_table.save()
        return data
    
    def read_account(self, query: dict = {}) -> list:
        data = accounts_table.read(query)
        return data
    
    def update_account(self, query: dict, data: dict) -> dict:
        accounts_table.update(query, data)
        accounts_table.save()
        return self.read_account(query)
        
    def delete_account(self, query: dict) -> None:
        accounts_table.delete(query)
        accounts_table.save()
        
    def count_account(self, query: dict = {}) -> int:
        return accounts_table.count(query)
    
    