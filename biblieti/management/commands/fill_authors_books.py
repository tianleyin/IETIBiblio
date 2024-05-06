from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from faker import Faker
from faker.providers import lorem
import random

from biblieti.models import *

class Command(BaseCommand):
    help = 'Seeder2: Populate database with authors and books'

    def handle(self, *args, **kwargs):
        fake_es = Faker('es_ES')
        fake_en = Faker('en_US')
        
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
            "Crimen y castigo",
            "El secret de la muntanya",
            "El misteri de la masia",
            "L'enigma del far",
            "L'illa perduda",
            "El tresor del pirata",
            "La llegenda del drac",
            "El poder de la màgia",
            "El regne oblidat",
            "La princesa sense corona",
            "El cavaller de la nit",
            "L'ombra del passat",
            "El xiuxiueig del vent",
            "L'eco dels somnis",
            "El xiuxiueig de les estrelles",
            "El laberint dels secrets",
            "El destí del heroi",
            "La clau del laberint",
            "L'últim vol del fènix",
            "La senda del guerrrer",
            "La dansa de les ombres"
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
            "La colmena",
            "La herencia perdida",
            "El secreto del bosque",
            "El misterio de la mansión",
            "El tesoro del pirata",
            "La leyenda del caballero",
            "El enigma del faro",
            "El vuelo del águila",
            "La senda del destino",
            "El susurro de las sombras",
            "La melodía del alma",
            "El jardín de las ilusiones",
            "El eco del silencio",
            "El laberinto de los recuerdos",
            "El sueño del navegante",
            "La estrella fugaz",
            "El susurro de la luna",
            "La promesa del mañana",
            "La voz del viento",
            "El fuego eterno",
            "El canto de los sueños"
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
        
        
        all_titles = list(set(titles_es + titles_cat))

        # Create books with random authors
        for _ in range(100):
            author_list.append(fake_es.name())



        
        for author_name in author_list:
            num_books = random.randint(1,4)
            for _ in range(num_books):
                title = random.choice(all_titles)
                    
                Book.objects.create(
                    name = title,
                    author = author_name,
                    ISBN = fake_es.isbn10(),
                    publication_year = fake_es.year(),
                    CDU=random.randint(50, 300)
                )
                
                Book.objects.create(
                    name = fake_es.sentence(nb_words=random.randint(1,5)),
                    author = author_name,
                    ISBN = fake_es.isbn10(),
                    publication_year = fake_es.year(),
                    CDU=random.randint(50, 300)
                )
                
                Book.objects.create(
                    name = fake_en.sentence(nb_words=random.randint(1, 5)),
                    author = author_name,
                    ISBN = fake_es.isbn10(),
                    publication_year = fake_es.year(),
                    CDU=random.randint(50, 300)
                )

        for _ in range(3):
            User_ieti.objects.create(
                username=fake_es.name(),
                email=fake_es.email(),
                password=fake_es.password(),
                role='librarian',
                date_of_birth=fake_es.date_of_birth(),
                school="Institut Esteve Terradas i Illa",
                # You might want to seed the image field here as well
            )
        
        for _ in range(15):
            User_ieti.objects.create(
                username=fake_es.name(),
                email=fake_es.email(),
                password=fake_es.password(),
                role='student',
                date_of_birth=fake_es.date_of_birth(),
                school="Institut Esteve Terradas i Illa",
                cycle=fake_es.random_element(elements=('Grau Superior DAW', 'Grau Superior DAM', 'Grau Mig Electromecànica de vehicles automòbils', 'Grau Mig Gestió administrativa', 'Grau Mig Mecanització')),
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