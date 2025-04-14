from faker import Faker
import uuid

class Generator:
    fake = Faker()

    @staticmethod
    def fake_email():
        email = f"test_{uuid.uuid4().hex[:8]}@gmail.com"
        return email

    @staticmethod
    def fake_password():
        return Generator.fake.password()

    @staticmethod
    def fake_name():
        return Generator.fake.user_name()