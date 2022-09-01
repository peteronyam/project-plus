import phonenumbers

from phonenumbers import geocoder

a = input("Enter phone: ")
phone = phonenumbers.parse(a)
print(geocoder.description_for_number(phone, "en"))