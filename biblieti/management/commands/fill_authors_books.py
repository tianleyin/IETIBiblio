from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from faker import Faker
import random

from biblieti.models import *

class Command(BaseCommand):
    help = 'Seeder2: Populate database with authors and books'

    def handle(self, *args, **kwargs):
        fake = Faker('es_ES')

        titles_cat = [
            "Cent anys de solitud",
            "El petit príncep",
            "L'ombra del vent",
            "La sombra del viento",
            "Marina",
            "El vent entre els salzes",
            "El vent entre los sauces",
            "La metamorfosi",
            "El nom del vent",
            "El nombre del viento",
            "Les aventures de Tom Sawyer",
            "Las aventuras de Tom Sawyer",
            "Matar un rossinyol",
            "Matar un ruiseñor",
            "Un món feliç",
            "Un mundo feliz",
            "Orgull i prejudici",
            "Orgullo y prejuicio",
            "Crim i càstig",
            "Crimen y castigo"
        ]

        titles_es = [
            "Cien años de soledad",
            "El principito",
            "La sombra del viento",
            "Marina",
            "La casa de los espíritus",
            "Crónica de una muerte anunciada",
            "Don Quijote de la Mancha",
            "Rayuela",
            "El amor en los tiempos del cólera",
            "La fiesta del chivo",
            "Los detectives salvajes",
            "El túnel",
            "Cuentos de la selva",
            "La ciudad y los perros",
            "El alquimista",
            "Los renglones torcidos de Dios",
            "La sombra del viento",
            "La casa de Bernarda Alba",
            "La regenta",
            "La colmena"
        ]
        
        subjectList = [
            "Sol·licitud d'Afegir un Nou Llibre a la Col·lecció",
            "Sol·licitud d'Afegir un Nou CD a la Col·lecció"
        ]

        paragraphList = [
            "Estimat equip de la biblioteca, Espero que aquest missatge us trobi bé. Em dirigeixo a vosaltres amb la finalitat de suggerir l'afegiment d'un nou llibre a la nostra col·lecció bibliogràfica. Després de revisar detingudament el nostre catàleg actual, he notat que hi ha una oportunitat per enriquir encara més la nostra oferta de llibres. M'agradaria proposar la incorporació d'un llibre que considero seria de gran interès i utilitat per a la nostra comunitat de lectors.",
            "Em poso en contacte amb vosaltres per suggerir l'afegiment d'un nou CD a la nostra col·lecció de mitjans audiovisuals. Després d'explorar el nostre catàleg actual, he notat que hi ha una manca de diversitat en la nostra col·lecció de CDs. Creu que l'afegiment d'un nou CD podria enriquir les opcions disponibles per als nostres usuaris."
        ]
        
        author_list = []

        # Create books with random authors
        for _ in range(100):
            author_list.append(fake.name())


        for author_name in author_list:
            num_books = random.randint(1,10)
            for _ in range(num_books):
                if random.choice([True, False]):
                    title = random.choice(titles_cat)
                else: 
                    title = random.choice(titles_es)
                    
                Book.objects.create(
                    name = title,
                    author = author_name,
                    ISBN = fake.isbn10(),
                    publication_year = fake.year()
                )

        for _ in range(3):
            User_ieti.objects.create(
                username=fake.name(),
                email=fake.email(),
                password=fake.password(),
                role='librarian',
                date_of_birth=fake.date_of_birth(),
                school="Institut Esteve Terradas i Illa",
                # You might want to seed the image field here as well
            )
        
        for _ in range(15):
            User_ieti.objects.create(
                username=fake.name(),
                email=fake.email(),
                password=fake.password(),
                role='student',
                date_of_birth=fake.date_of_birth(),
                school="Institut Esteve Terradas i Illa",
                cycle=fake.random_element(elements=('Grau Superior DAW', 'Grau Superior DAM', 'Grau Mig Electromecànica de vehicles automòbils', 'Grau Mig Gestió administrativa', 'Grau Mig Mecanització')),
                # You might want to seed the image field here as well
            )
        
        all_users = User_ieti.objects.all()
        catalogues = Catalogue.objects.all()
        
        for _ in range(5):
            random_user = random.choice(all_users)
            random_choice = random.randint(0, 1)

            Petition.objects.create(
                subject=subjectList[random_choice],
                commentary=paragraphList[random_choice],
                user=random_user
            )
        
        for _ in range(15):
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
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database.'))
