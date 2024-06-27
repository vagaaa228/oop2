class Validator:

    def __init__(self):
        pass

    def isEmail(self, str):
        return ('@' in str) and ('.' in str)

    def isPhone(self, str):
        if len(str.split("-")) == 5:
            return True


    def isDomain(self, domain):
        return ('.' in domain)




email = "example@example.com"
phone_number = "+7-123-456-78-50"
dom = "asdf.ru"

validator = Validator()

if validator.isEmail(email):
    print("Email адрес валиден")
else:
    print("Email адрес невалиден")

if validator.isPhone(phone_number):
    print("Номер телефона валиден")
else:
    print("Номер телефона невалиден")

if validator.isDomain(dom):
    print("Адрес валиден")
else:
    print("Адрес невалиден")