from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from datetime import timedelta
import random
from faker import Faker
    
from biblieti.models import *
    
    
class Command(BaseCommand):
    help = 'Populate IETIbiblio database with users, petitions, elements (cds, devices, books..), bookings and loans'
    
    def handle(self, *args, **kwargs):
        fake = Faker('es_ES')

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

        subjectList = [
            "Sol·licitud d'Afegir un Nou Llibre a la Col·lecció",
            "Sol·licitud d'Afegir un Nou CD a la Col·lecció"
        ]

        paragraphList = [
            "Estimat equip de la biblioteca, Espero que aquest missatge us trobi bé. Em dirigeixo a vosaltres amb la finalitat de suggerir l'afegiment d'un nou llibre a la nostra col·lecció bibliogràfica. Després de revisar detingudament el nostre catàleg actual, he notat que hi ha una oportunitat per enriquir encara més la nostra oferta de llibres. M'agradaria proposar la incorporació d'un llibre que considero seria de gran interès i utilitat per a la nostra comunitat de lectors.",
            "Em poso en contacte amb vosaltres per suggerir l'afegiment d'un nou CD a la nostra col·lecció de mitjans audiovisuals. Després d'explorar el nostre catàleg actual, he notat que hi ha una manca de diversitat en la nostra col·lecció de CDs. Creu que l'afegiment d'un nou CD podria enriquir les opcions disponibles per als nostres usuaris."
        ]


        # Seed Users
        for _ in range(10):
            User_ieti.objects.create(
                username=fake.name(),
                email=fake.email(),
                password=fake.password(),
                role=random.choice(['student', 'librarian', 'superadmin']),
                date_of_birth=fake.date_of_birth(),
                school="Institut Esteve Terradas i Illa",
                cycle=fake.random_element(elements=('Grau Superior DAW', 'Grau Superior DAM', 'Grau Mig Electromecànica de vehicles automòbils', 'Grau Mig Gestió administrativa', 'Grau Mig Mecanització')),
                # You might want to seed the image field here as well
            )

        all_users = User_ieti.objects.all()

        """Catalogue.objects.create(
            name="Institut " + fake.catch_phrase(),
            # You might want to seed the picture field here as well
        )"""

        # Seed Books
        for _ in range(10):
            Book.objects.create(
                name=fake.random.choice(booksList),
                author=fake.name(),
                ISBN=fake.isbn10(),
                publication_year=fake.year(),
                CDU=random.randint(50, 300)
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
                resolution="1920p x 1080p HD",
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
            random_choice = random.randint(0, 1)

            Petition.objects.create(
                subject=subjectList[random_choice],
                commentary=paragraphList[random_choice],
                user=random_user
            )

        # seed Loan and Booking
        all_users = User_ieti.objects.all()
        catalogues = Catalogue.objects.all()
        for _ in range(5):
            user = random.choice(all_users)
            catalogue = random.choice(catalogues)
            loan_date = timezone.now() - timedelta(days=random.randint(1, 30))
            return_date = loan_date + timedelta(days=random.randint(1, 14))
            Loan.objects.create(
                user=user,
                catalogue=catalogue,
                date_of_loan=loan_date,
                date_of_return=return_date
            )
            Booking.objects.create(
                user=user,
                catalogue=catalogue,
                booking_date=timezone.now()
            )
        
        print("Succesfully populated IETIbiblio database.")