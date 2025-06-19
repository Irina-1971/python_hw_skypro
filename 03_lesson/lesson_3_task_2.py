from smartphone import Smartphone


catalog = [
    Smartphone("samsung", "GL s20", "+79211234567"),
    Smartphone("samsung", "GL s21", "+79211234568"),
    Smartphone("samsung", "GL s22", "+79211234569"),
    Smartphone("samsung", "GL s23", "+79211234560"),
    Smartphone("samsung", "GL s24", "+79211234561"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
    