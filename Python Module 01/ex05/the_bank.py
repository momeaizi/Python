import random
import string

class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError('Attribute value cannot be negative.')
        if not isinstance(self.name, str):
            raise AttributeError('Attribute name must be a str object.')

    def transfer(self, amount):
        self.value += amount


def isCorrupted(account):

    attributes = dir(account)

    if len(attributes) % 2 == 0: # number of attributes is even
        return True
    if any(attr.startswith('b') for attr in attributes): # an attribute starts with b
        return True
    if not any(attr.startswith('zip') or attr.startswith('addr') for attr in attributes): # no attribute starts with zip or addr
        return True
    if not hasattr(account, 'name') or not hasattr(account, 'id') or not hasattr(account, 'value'): # no attribute name, id or value
        return True
    if not isinstance(account.name, str): # name no being a str
        return True
    if not isinstance(account.id, int): # id no being a int
        return True
    if not isinstance(account.value, (int, float)): # value no being a int or float
        return True
    return False



class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account=None):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if new_account is None:
            return False
        if not isinstance(new_account, Account): # new_account not being an Account instance
            return False
        
        if not next((account for account in self.accounts if account.name == new_account.name), None) is None: # account name is already exists
            return False

        self.accounts.append(new_account) # add the account to the bank
        return True

    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if not isinstance(origin, str) or not isinstance(dest, str) or not isinstance(amount, (float, int)):
            return False
        
        originAccount = next((account for account in self.accounts if account.name == origin), None)
        destAccount =  next((account for account in self.accounts if account.name == dest), None)


        if originAccount is None or destAccount is None: # one of these accounts doesn't exist
            return False

        if isCorrupted(originAccount) or isCorrupted(destAccount): # one of these accounts is corrupted
            return False
    
        if amount < 0 or amount > originAccount.value: # invalid amount
            return False

        originAccount.transfer(-amount)
        destAccount.transfer(amount)
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str): # name not being a string
            return False
        account = next((account for account in self.accounts if account.name == name), None)
        
        if account is None: # account doesn't exist
            return False
    
        if not isCorrupted(account):
            return True
    
        self.try_fix_account(account)

    def try_fix_account(self, account):

        for attr in dir(account): # delete attribute starting with b
            if attr.startswith('b'):
                delattr(account, attr)

        if not any(attr.startswith('zip') or attr.startswith('addr') for attr in dir(account)): # add if no attribute starting with zip or addr
            setattr(account, 'zip' + ''.join(random.choices(string.ascii_uppercase, k=6)), None)
        
        if not hasattr(account, 'id'): # add id if it doesn't exist
            setattr(account, 'id', len(self.accounts) - 1)
        
        if not hasattr(account, 'value'): # add value if it doesn't exist
            setattr(account, 'value', 0)

        
        if not isinstance(account.id, int): # id no being a int
            account.id = int(account.id)
        
        if not isinstance(account.value, (int, float)): # value no being a int or float
            account.value = int(account.value)
        
        if len(dir(account)) % 2 == 0: # fix even number of attributes
            setattr(account, ''.join(random.choices(string.ascii_letters + string.digits, k=6)), None)



