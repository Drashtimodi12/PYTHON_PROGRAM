import random
import string
from faker import Faker
from myapp.models import *
fake = Faker()

for i in range(10):
    username = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    age = random.randint(15,25)
    # print(username, email, phone, age)

    Student.objects.create(
        username = username,
        email = email,
        phone = phone,
        age = age
    )