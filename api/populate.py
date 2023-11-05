import random
from faker import Faker
from api.models import Book

def add_books(num=100):
    fake = Faker()
    for _ in range(num):
        title = fake.sentence(nb_words=4).rstrip('.')
        author = fake.name()
        category = random.choice(Book.CATEGORY_CHOICES)[0]
        date_of_publishing = fake.date_between(start_date='-10y', end_date='today')

        Book.objects.create(
            title=title,
            author=author,
            category=category,
            date_of_publishing=date_of_publishing
        )
    print(f'{num} books have been created!')

def add_books_author(num=10, author = "Thomas Anthony"):
    fake = Faker()
    for _ in range(num):
        title = fake.sentence(nb_words=4).rstrip('.')
        author = author
        category = random.choice(Book.CATEGORY_CHOICES)[0]
        date_of_publishing = fake.date_between(start_date='-10y', end_date='today')
        rating = random.uniform(0.0,5.0)

        Book.objects.create(
            title=title,
            author=author,
            category=category,
            date_of_publishing=date_of_publishing,
            rating = rating
        )
    print(f'{num} books have been created!')
