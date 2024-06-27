class Validator:

    def __init__(self):
        pass

    def isEmail(self, str):
        return ('@' in str) and ('.' in str)

    def isDomain(self, domain):
        return ('.' in domain)




email = "example@example.com"
dom = "asdf.ru"

validator = Validator()

if validator.isEmail(email):
    print("Email адрес валиден")
else:
    print("Email адрес невалиден")

if validator.isDomain(dom):
    print("Адрес валиден")
else:
    print("Адрес невалиден")