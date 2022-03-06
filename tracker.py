import phonenumbers

number = input('Please enter a phone number (including country code): ')
from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))

from phonenumbers.util import prnt  
x = phonenumbers.parse(number, None)
prnt(x)
type(x)
str(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL))