import pytest
from datetime import timedelta
import bank_account_project as ba

class Test_banks_account:
    def test_create_timezon(self):
        tz = ba.TimeZone("GMT-5",-5,0)

        assert "GMT-5" == tz.name
        assert timedelta(hours=-5, minutes=0) == tz.offset
        
    def test_timezone_equal(self):
        tz1 = ba.TimeZone("GTM-5",-5,0)
        tz2 = ba.TimeZone("GTM-5",-5,0)

        assert tz1.__eq__(tz2)

    def test_create_account(self):
        account_number = "A400B"
        first_name = "Felipe"
        last_name = "Hdez"
        tz = ba.TimeZone("GTM-5",-5,0)
        balance = 100

        a = ba.Account(account_number, first_name, last_name,tz, balance)

        assert account_number == a.account_number
        assert first_name == a.first_name
        assert last_name == a.last_Name
        assert tz == a.prefer_timezone
        assert balance == a.balance

    def test_create_account_blank_names(self):
        account_number = "A400B"
        first_name = ""
        last_name = "Hdez"
        tz = ba.TimeZone("GTM-5",-5,0)
        balance = 100

        with pytest.raises(ValueError):
            a = ba.Account(account_number, first_name, last_name,tz, balance)

    def test_create_account_negative_balance(self):
        account_number = "A400B"
        first_name = "Felipe"
        last_name = "Hdez"
        tz = ba.TimeZone("GTM-5",-5,0)
        balance = -100

        with pytest.raises(ValueError):
            a = ba.Account(account_number, first_name, last_name,tz, balance)