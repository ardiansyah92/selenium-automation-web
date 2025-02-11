
import random
import string

class input_element:
    @staticmethod
    def id_generator(length=4, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(length))

    random_string = id_generator()  # Properly calling static method

    usernameInput = "Software Quality Assurance " + random_string
    userEmailInput = f"Softwarequalityassurance_{random_string}@yopmail.com"
    currentAddressInput = "Bandung Indigo Hub"
    permanentAddressInput = "Bandung Lautan API" 
    