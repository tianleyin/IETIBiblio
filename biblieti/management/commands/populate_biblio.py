from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from datetime import timedelta
import random
from faker import Faker
    
from biblieti.models import *
    
    
class Command(BaseCommand):
    help = 'Populate IETIbiblio database with users, elements (cds, devices, books..), bookings and loans'
    
    def handle(self, *args, **kwargs):
        fake = Faker()

        booksList = [
            "Cent anys de solitud",
            "1984",
            "El petit príncep",
            "Don Quijote de la Mancha",
            "Harry Potter i la pedra filosofal",
            "Orgull i prejudici",
            "Matar un rossinyol",
            "El senyor dels anells",
            "Crim i càstig",
            "El gran Gatsby",
            "Les aventures de Sherlock Holmes",
            "La metamorfosi",
            "El nom del vent",
            "Les raïms de la còlera",
            "Anna Karenina",
            "Sapiens: dels animals als déus",
            "L'Odissea",
            "L'ombra del vent",
            "L'alquimista",
            "L'art de la guerra"
        ]

        cdList = [
            "Abbey Road",
            "Thriller",
            "The Dark Side of the Moon",
            "Back in Black",
            "Sgt. Pepper's Lonely Hearts Club Band",
            "The Wall",
            "Led Zeppelin IV",
            "Greatest Hits",
            "Rumours",
            "Born to Run",
            "Nevermind",
            "Hotel California",
            "The Joshua Tree",
            "The Rise and Fall of Ziggy Stardust and the Spiders from Mars",
            "Goodbye Yellow Brick Road",
            "A Night at the Opera",
            "American Idiot",
            "OK Computer",
            "Kind of Blue",
            "Pet Sounds"
        ]

        devicesList = [
            "Tauleta",
            "Lector de llibres electrònics (e-readers)",
            "Auriculars de cancel·lació de soroll",
            "Dispositius d'audiollibres",
            "Portàtils"
        ]



        # Seed Users
        for _ in range(5):
            User.objects.create(
                name=fake.name(),
                mail=fake.email(),
                password=fake.password(),
                role=random.choice(['student', 'librarian', 'superadmin']),
                date_of_birth=fake.date_of_birth(),
                school=fake.company(),
                cycle=fake.random_element(elements=('A', 'B', 'C', 'D', 'E', 'F')),
                # You might want to seed the image field here as well
            )

        all_users = User.objects.all()

        Catalogue.objects.create(
            name="Institut " + fake.catch_phrase(),
            # You might want to seed the picture field here as well
        )

        # Seed Books
        for _ in range(10):
            Book.objects.create(
                name=fake.random.choice(booksList),
                author=fake.name(),
                ISBN=fake.isbn10(),
                publication_year=fake.year(),
            )

        # Seed CDs
        for _ in range(10):
            CD.objects.create(
                name=fake.random.choice(cdList),
                artist=fake.name(),
                tracks=random.randint(5, 15),
            )

        # seed DVDs
        for _ in range(10):
            DVD.objects.create(
                name=fake.random.choice(cdList),
                director=fake.name(),
                duration=random.randint(5, 15),
            )

        # seed BR (blurray disc?)
        for _ in range(10):
            BR.objects.create(
                name=fake.random.choice(cdList),
                resolution="1920 x 1080 HD",
            )

        # seed device
        for _ in range(10):
            Device.objects.create(
                name=fake.random.choice(devicesList),
                manufacturer=fake.company(),
                model=fake.sentence(),
            )

        # seed Petition
        for _ in range(3):
            random_user = random.choice(all_users)
            Petition.objects.create(
                subject=fake.sentence(),
                commentary=fake.paragraph(),
                user=random_user
            )

        # Seed DVDs, BRs, Devices, etc.
        # Add similar seeding logic for other models if needed

        # Seed Bookings, Loans, Petitions, etc.
        # Add seeding logic for related models if needed

