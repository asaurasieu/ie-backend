from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, country, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', 'Spain')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'
    assert account.country == 'Spain'
    
    
def test_delete_account():
    """
    GIVEN a list of Accounts
    WHEN an Account is deleted
    THEN ensure the Account is removed from the list
    """
    # Create a sample list of accounts
    accounts = [
        Account('John Doe', '€', 'Spain'),
        Account('Jane Smith', '$', 'USA'),
        Account('Alice Johnson', '¥', 'Japan')
    ]
    
    # Choose an account to delete
    account_to_delete = accounts[1]
    
    def delete_account(accounts):
        accounts.remove(account_to_delete)

    # Delete the account
    delete_account(accounts)
    
    # Ensure the account is removed from the list
    assert account_to_delete not in accounts
    

def test_get_account():
    """
    GIVEN a list of Accounts
    WHEN an Account is retrieved by account number
    THEN ensure the correct Account is returned
    """
    # Create a sample list of accounts
    accounts = [
        Account('John Doe', '€', 'Spain'),
        Account('Jane Smith', '$', 'USA'),
        Account('Alice Johnson', '¥', 'Japan')
    ]
    
    # Choose an account to retrieve
    account_number = accounts[1].account_number
    
    def get_account(account_number):
    # Retrieves an account from the list of accounts based on the account number.
    # Returns None if the account is not found.
    
        for account in accounts:
            if account.account_number == account_number:
                return account
        return None
    
    # Retrieve the account
    retrieved_account = get_account(account_number)
    
    # Ensure the correct account is returned
    assert retrieved_account == accounts[1]

def test_update_account():
    """
    GIVEN a list of Accounts
    WHEN an Account is updated
    THEN ensure the Account details are correctly modified
    """
    # Create a sample list of accounts
    accounts = [
        Account('John Doe', '€', 'Spain'),
        Account('Jane Smith', '$', 'USA'),
        Account('Alice Johnson', '¥', 'Japan')
    ]
    
    # Choose an account to update
    account_to_update = accounts[0]
    
    # Define the updated account details
    updated_name = 'John Smith'
    updated_currency = '$'
    updated_country = 'USA'
    
    def update_account(account, name, currency, country):
        account.name = name
        account.currency = currency
        account.country = country

    # Update the account
    update_account(account_to_update, updated_name, updated_currency, updated_country)
    
    # Ensure the account details are correctly modified
    assert account_to_update.name == updated_name
    assert account_to_update.currency == updated_currency
    assert account_to_update.country == updated_country
    
def test_delete_invalid_account():
    """
    GIVEN a list of Accounts
    WHEN an invalid Account is attempted to be deleted
    THEN ensure the list remains unchanged
    """
    # Create a sample list of accounts
    accounts = [
        Account('John Doe', '€', 'Spain'),
        Account('Jane Smith', '$', 'USA'),
        Account('Alice Johnson', '¥', 'Japan')
    ]
    
    # Choose an invalid account to delete
    invalid_account = Account('Invalid Account', 'Invalid Currency', 'Invalid Country')
    
    def delete_account(accounts, account):
        if account in accounts:
            accounts.remove(account)

    # Attempt to delete the invalid account
    delete_account(accounts, invalid_account)
    
    # Ensure the list remains unchanged
    assert len(accounts) == 3
    assert invalid_account not in accounts

