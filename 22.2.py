class Validator:

    def __init__(self):
        pass

    def isEmail(self, str):
        return ('@' in str) and ('.' in str)




email = "example@example.com"

validator = Validator()

if validator.isEmail(email):
    print("Email адрес валиден")
else:
    print("Email адрес невалиден")
