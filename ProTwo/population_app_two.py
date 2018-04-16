import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random
from AppTwo import models
from faker import Faker

fake = Faker()


def add_user():
    fake_name = fake.name().split(" ")
    first_name = fake_name[0]
    last_name = fake_name[-1]

    fake_email = fake.email()

    user = models.User.objects.get_or_create(
        first_name=first_name,
        last_name=last_name,
        email=fake_email,
    )[0]
    user.save()

    return user


def populate(N=5):

    for i in range(N):
        user = add_user()
        print("Generated {}".format(user))


if __name__ == "__main__":
    print("Starting to generate fake users...")
    populate(5)
    print("Done!")
