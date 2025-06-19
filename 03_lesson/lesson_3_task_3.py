from address import Address
from mailing import Mailing

to_address = Address( "123456", " Томск", " Ленина", "1","82")

from_address = Address( "504600", " Новосибирск", " Лесная", "2", "5")

mailing = Mailing( to_address, from_address, "400", "12345678987")

print(mailing)