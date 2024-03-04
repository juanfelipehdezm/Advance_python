from datetime import timedelta, datetime,timezone
from collections import namedtuple
import itertools
import numbers

#********************************************************************************
#************************TimeZone Class*******************************************
class TimeZone:
    """
    **Summary:**

    Represents a time zone with its name and offset from Coordinated Universal Time (UTC).

    **Attributes:**

    * `name (str)`: The name of the time zone.
    * `offset (timedelta)`: The time offset from UTC, expressed as a `timedelta` object.
    * `offset_hours (int)`: The hours component of the offset.
    * `offset_minutes (int)`: The minutes component of the offset.

    **Methods:**

    * `__init__(self, name: str, offset_hours: int, offset_minutes: int)`: Initializes a `TimeZone` object with the given name and offset.
    * `offset(self) -> timedelta`: Returns the time offset from UTC.
    * `name(self) -> str`: Returns the name of the time zone.
    * `__eq__(self, other_timezone) -> bool`: Compares two `TimeZone` objects for equality.
    * `__repr__(self) -> str`: Returns a string representation of the `TimeZone` object.

    **Raises:**

    * `ValueError`: If any of the following conditions are not met:
        * The time zone name is empty.
        * The offset hours or minutes are not integers.
        * The offset minutes are outside the range of -59 to 59.
        * The total offset is outside the range of -12:00 to 14:00.
    """
    def __init__(self, name: str, offset_hours: int, offset_minutes: int):
        if name is None:
            raise ValueError("Timezone name can not be empty")
        self._name = name.strip()

        if not isinstance(offset_hours, int):
            raise ValueError("Hour offset must be an integer")
        

        if not isinstance(offset_minutes, int):
            raise ValueError("Hour offset must be an integer")

        if offset_minutes > 59 or offset_minutes < -59:
            raise ValueError("Minutes offset must be between -59 and 59")

        offset = timedelta(hours=offset_hours, minutes=offset_minutes)

        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes= 0):
            raise ValueError("Offset must be between -12:00 and 14:00")

        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset


    @property
    def offset(self):
        return self._offset
    
    @property
    def name(self):
        return self._name
    
    def __eq__(self, other_timezone):
        return (isinstance(other_timezone, TimeZone) and
                self._name == other_timezone._name and
                self._offset == other_timezone._offset)

    def __repr__(self):
        return (f"TimeZone(name='{self.name}'", 
                f"offset_hours= {self._offset_hours}", 
                f"offset_minutes = {self._offset_minutes}")
    

#time_zone1 = TimeZone("ABC", 2, 4)
#print(time_zone1.offset)
"""
today = datetime.now(timezone.utc)
print(today) #2024-02-27 22:41:25.575990+00:00
print(today + time_zone1.offset) #2024-02-28 00:45:25.575990+00:00
it added 2 hours and 4 minuntes
"""


#********************************************************************************
#************************Account Class*******************************************
class Account:
    """
    **Summary:**

    This class represents a bank account with attributes for account number, owner's name, balance, preferred time zone, and interest rate. 
    It also provides methods for account management, including deposits, withdrawals, and interest payments.

    **Attributes:**

    * `account_number (str)`: The unique identifier for the account.
    * `first_name (str)`: The owner's first name.
    * `last_name (str)`: The owner's last name.
    * `_balance (float)`: The current balance of the account.
    * `_prefer_timezone (TimeZone)`: The preferred time zone for displaying transactions. (default: UTC)
    * `_transactions_code (dict)`: Internal dictionary mapping transaction types to their codes.
    * `_INTERES_RATE (float)`: The annual interest rate applied to the account (as a decimal).

    **Nested Class:**

    * `Confirmation(namedtuple)`: Represents a confirmation record for an account transaction with attributes:
        * `account_number (str)`: The account number involved in the transaction.
        * `transaction_code (str)`: The code representing the transaction type (deposit, withdrawal, interest, etc.).
        * `transaction_id (str)`: A unique identifier for the transaction.
        * `time_utc (str)`: The UTC timestamp of the transaction in ISO 8601 format.
        * `preferred_time (str)`: The transaction time displayed in the preferred time zone.

    **Methods:**

    * `__init__(self, account_number: str, first_name: str, last_name: str, prefer_timezone=None, initial_balance=0.0)`: Initializes an `Account` object with the given attributes.
    * `account_number (self) -> str`: Returns the account number. (property)
    * `first_name (self) -> str`: Returns the first name. (property)
    * `first_name (self, new_name: str)`: Sets the first name after validation. (setter)
    * `last_name (self) -> str`: Returns the last name. (property)
    * `last_name (self, new_last_name: str)`: Sets the last name after validation. (setter)
    * `prefer_timezone (self) -> TimeZone`: Returns the preferred time zone. (property)
    * `prefer_timezone (self, new_timezone: TimeZone)`: Sets the preferred time zone. (setter)
    * `balance (self) -> float`: Returns the account balance. (property)
    * `@classmethod get_interest_rate(cls) -> float`: Returns the current annual interest rate (as a percentage).
    * `@classmethod set_interest_rate(cls, new_rate: float)`: Sets the annual interest rate (must be a decimal between 0 and 1).
    * `@staticmethod validate_firstOrLast_name(value: str, fiel_title: str) -> str`: Validates and capitalizes the given name.
    * `generate_confirmation_code(self, transaction_code: str) -> str`: Generates a unique confirmation code for a transaction.
    * `@staticmethod parse_confirmation_code(confirmation_code: str, preferred_time_zone=None) -> Confirmation`: Parses a confirmation code and returns a `Confirmation` namedtuple.
    * `deposit(self, amount_to_deposit: numbers.Real) -> str`: Deposits a specified amount and returns a confirmation code.
    * `withdraw(self, amount_to_withdraw: numbers.Real) -> str`: Attempts to withdraw an amount and returns a confirmation code (success or rejection).
    * `pay_interest(self) -> str`: Calculates and deposits interest, returning a confirmation code.
"""
    #this is going return a new transction id each time it gets called
    transaction_counter = itertools.count(100)

    _INTERES_RATE = 0.5

    _transactions_code = {
        "deposit" : "D",
        "withdraw" : "W",
        "interest" : "I",
        "rejected" : "R"
    }


    Confirmation = namedtuple("Confirmation", "account_number transaction_code transaction_id time_utc preferred_time")

    def __init__(self, account_number: str, first_name: str, last_name: str, 
                 prefer_timezone = None, initial_balance = 0.0):

        if len(account_number) < 5:
            raise ValueError("The minimun length for an account if five characters")
        
        self._account_number = account_number

        if (first_name is None or len(first_name) <= 1) or (last_name is None or len(last_name) <= 1):
            raise ValueError("Firts name and last name are required")
        
        self._first_name = first_name
        self._last_name = last_name

        if prefer_timezone is None: 
            prefer_timezone = TimeZone("UTC",0,0)

        self._prefer_timezone = prefer_timezone

        if initial_balance < 0:
            raise ValueError("Balance can not be negative")
        self._balance = initial_balance


    @property
    def account_number(self):
        return self._account_number
        
    @property
    def first_name(self):
        return self._first_name
        
    @first_name.setter
    def first_name(self, new_name):
        self._first_name = Account.validate_firstOrLast_name(new_name, "First Name")
    @property
    def last_Name(self):
        return self._last_name
        
    @last_Name.setter
    def last_Name(self, new_last_name):
        self._last_name = Account.validate_firstOrLast_name(new_last_name, "Last Name")

    @property
    def prefer_timezone(self):
        return self._prefer_timezone    


    @prefer_timezone.setter
    def prefer_timezone(self, new_timezone):
        if not isinstance(new_timezone, TimeZone):
            raise ValueError("Time Zone must be a valid TimeZone object")
        self._prefer_timezone = new_timezone


    @property
    def balance(self):
        return self._balance
    
    @classmethod
    def get_interest_rate(cls):
        return cls._INTERES_RATE
    
    @classmethod
    def set_interest_rate(cls,new_rate):
        if not isinstance(new_rate, float) or new_rate < 0:
            raise ValueError("Interest rate must be a real number and can not be negative")
        
        cls._INTERES_RATE = new_rate

    @staticmethod
    def validate_firstOrLast_name(value, fiel_title):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError(f"{fiel_title} cannot be empty")
        return value.strip().capitalize()
    
    def generate_confirmation_code(self, transaction_code:str) -> str:
        dt_str = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        return f"{transaction_code}-{self.account_number}-{dt_str}-{next(Account.transaction_counter)}"


    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_time_zone = None):
        #dummy-A100-20240229073715-101
        parts = confirmation_code.split("-")

        if len(parts) != 4:
            raise ValueError("Invalid confirmation Code")

        transaction_code, account_number, raw_dt_utc, trasaction_counter_id = parts

        try:
            dt_utc = datetime.strptime(raw_dt_utc, "%Y%m%d%H%M%S")
        except ValueError as ex:
            raise ValueError("Invalid transaction datetime") from ex
        
        if preferred_time_zone is None:
            preferred_time_zone = TimeZone("UTC", 0, 0)

        if not isinstance(preferred_time_zone,TimeZone):
            raise ValueError("Invalid TimeZone object")
        
        dt_preferred = dt_utc + preferred_time_zone.offset

        dt_preferred_str = f"{dt_preferred.strftime('%Y-%m-%d %H:%M:%S')} ({preferred_time_zone.name})"

        return Account.Confirmation(account_number, transaction_code, 
                            trasaction_counter_id,dt_utc.isoformat(), dt_preferred_str )

    def deposit(self, amount_to_deposit):
        min_deposit_value = 50000

        if not isinstance(amount_to_deposit, numbers.Real):
            raise ValueError("Deposit value must be a real number")
        
        if amount_to_deposit < min_deposit_value:
            raise ValueError(f"The minimun deposit value is {min_deposit_value}$")

        transaction_code = Account._transactions_code["deposit"]

        confirmation_code = self.generate_confirmation_code(transaction_code)

        self._balance += amount_to_deposit

        return confirmation_code
    
    def withdraw(self, amount_to_withdraw):

        accepted = False

        if not isinstance(amount_to_withdraw, numbers.Real):
            raise ValueError("Withdraw value must be a real number")
        
        if amount_to_withdraw <= 0:
            raise ValueError("Withdraw can not be negative")
        
        if self.balance - amount_to_withdraw < 0:
            transaction_code = Account._transactions_code["rejected"]

        else:
            accepted = True
            transaction_code = Account._transactions_code["withdraw"]

        confirmation_code = self.generate_confirmation_code(transaction_code)

        if accepted:
            self._balance -= amount_to_withdraw

        return confirmation_code

                 
    def pay_interest(self):
        interest_earn = self._balance * Account.get_interest_rate() / 100

        confirmation_code = self.generate_confirmation_code(Account._transactions_code["interest"])

        self._balance += interest_earn

        return confirmation_code
    
    def __repr__(self):
        return (f"Account = ({self._account_number}, {self._first_name}, {self._last_name})")

a1 = Account("ABC111", "Juan", "Hernandez")

"""
conf_code = a1.generate_confirmation_code("dummy") 

print(conf_code)
#dummy-ABC111-20240301010306-100

prefered_time_zone = TimeZone("GMT-5", -5,0)
parse_conf_code = a1.parse_confirmation_code(conf_code, prefered_time_zone)

print(parse_conf_code)
#Confirmation(account_number='ABC111', transaction_code='dummy', transaction_id='100', time_utc='2024-03-01T01:03:06', preferred_time='2024-02-29 20:03:06 (GMT-5)')
"""


print(a1.deposit(100000))

print(a1.balance)

print(a1.withdraw(5000))

print(a1.balance)