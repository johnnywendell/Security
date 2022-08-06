# Da pra pegar várias informações nessa biblioteca como exemplo geolocalização abaixo
import phonenumbers
from phonenumbers import geocoder

phone = input('digite o número de telefone: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))