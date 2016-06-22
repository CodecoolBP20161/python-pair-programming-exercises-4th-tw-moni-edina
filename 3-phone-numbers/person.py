class Person():
    _name = None
    _phone_number = None

    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number

    def is_phone_number_matching(self, input_phone_number):
        return self._phone_number == input_phone_number

    def get_name(self):
        if self.is_phone_number_matching:
            return self._name
        else:
            return "This number is not matching."

    @staticmethod
    def normalize_phone_number(phone_number):
        return phone_number.replace("-", "").replace(" ", "")
