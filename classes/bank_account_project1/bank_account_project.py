from datetime import timedelta, datetime,timezone
import itertools

#********************************************************************************
#************************TimeZone Class*******************************************
class TimeZone:
    """Represents a time zone with a name and offset in hours and minutes.

        Args:
            name (str): The name of the time zone.
            offset_hours (int): The hour offset of the time zone.
            offset_minutes (int): The minute offset of the time zone.

        Returns:
            None

        Raises:
            ValueError: If the timezone name is empty, hour offset is not an integer, minute offset is not an integer,
                        minute offset is not between -59 and 59, or offset is not between -12:00 and 14:00.

        Examples:
            tz = TimeZone('GMT', 0, 0)
        """

    """Returns the offset of the time zone."""
    """Returns the name of the time zone."""
    """Compares the current time zone with another time zone for equality."""
    """Returns a string representation of the time zone."""

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

    This class represents a bank account with attributes for account number, first name, and last name.

    **Explanation:**

    This class initializes an `Account` object with an account number, first name, and last name. 
    It provides properties for accessing these attributes and methods for setting first and last names, validating names, and generating a string representation of the account.

    **Attributes:**

    * `account_number (str)`: The unique identifier for the account.
    * `first_name (str)`: The owner's first name.
    * `last_name (str)`: The owner's last name.
    
    **Raises:**

    * `ValueError`:
        * If the account number is less than 5 characters.
        * If the first name or last name is empty or null.
        * If the provided value for first or last name is not a string.
    """

    #this is going return a new transction id each time it gets called
    transaction_counter = itertools.count(100)

    def __init__(self, account_number: str, first_name: str, last_name: str):

        if len(account_number) < 5:
            raise ValueError("The minimun length for an account if five characters")
        
        self._account_number = account_number

        if (first_name is None or len(first_name) <= 1) or (last_name is None or len(last_name) <= 1):
            raise ValueError("Firts name and last name are required")
        
        self._first_name = first_name
        self._last_name = last_name


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

    @staticmethod
    def validate_firstOrLast_name(value, fiel_title):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError(f"{fiel_title} cannot be empty")
        return value.strip().capitalize()
        
    def __repr__(self):
        return (f"Account = ({self._account_number}, {self._first_name}, {self._last_name})")

#a1 = Account("ABC111", "Juan", "Hernandez")
#print(a1)