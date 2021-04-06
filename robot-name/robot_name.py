import random
import string


class Robot:
    name = ''

    def __init__(self):
        self.name = self.generate_name()

    def reset(self):
        self.name = self.generate_name()

    def generate_name(self):
        random.seed()
        random_int = random.randint(0, 999)
        int_to_str = str(f'{random_int:03}')
        return "".join(random.choices(string.ascii_uppercase, k=2)) + int_to_str