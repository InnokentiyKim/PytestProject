from faker import Faker


fake = Faker()

class PlayerLocalization:

    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            "nickname": self.fake.name(),
        }

    def build(self):
        return self.result

