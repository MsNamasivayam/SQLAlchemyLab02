"""
The starting data for vet.db.
init_db() uses this to fill a brand-new database.
"""

from models import Owner, Vet, Pet, Appointment

OWNERS = [
    Owner(id=1, first_name="Tom", last_name="Hanks", email="thanks@gmail.com", phone_number="555-1234"),
    Owner(id=2, first_name="Beyonce", last_name="Knowles", email="queenbey@gmail.com", phone_number="555-5678"),
    Owner(id=3, first_name="George", last_name="Clooney", email="gclooney@yahoo.com", phone_number="555-9012"),
    Owner(id=4, first_name="Angelina", last_name="Jolie", email="ajolie@hotmail.com", phone_number="555-3456"),
    Owner(id=5, first_name="Dwayne", last_name="Johnson", email="therock@gmail.com", phone_number="555-7890"),
    Owner(id=6, first_name="Jennifer", last_name="Lawrence", email="jlawrence@yahoo.com", phone_number="555-2345"),
    Owner(id=7, first_name="Brad", last_name="Pitt", email="bpitt@hotmail.com", phone_number="555-6789"),
    Owner(id=8, first_name="Taylor", last_name="Swift", email="tswift@gmail.com", phone_number="555-0123"),
    Owner(id=9, first_name="Leonardo", last_name="DiCaprio", email="ldicaprio@yahoo.com", phone_number="555-4567"),
    Owner(id=10, first_name="Oprah", last_name="Winfrey", email="oprahwinfrey@gmail.com", phone_number="555-8901"),
]

VETS = [
    Vet(id=1, first_name="John", last_name="Dolittle"),
    Vet(id=2, first_name="Ted", last_name="Mullins"),
    Vet(id=3, first_name="Gerry", last_name="Harding"),
    Vet(id=4, first_name="Zia", last_name="Rodriguez"),
    Vet(id=5, first_name="Alan", last_name="Grant"),
]

PETS = [
    Pet(id=1, name="Buddy", species="Dog", owner_id=1),
    Pet(id=2, name="Luna", species="Cat", owner_id=2),
    Pet(id=3, name="Max", species="Dog", owner_id=3),
    Pet(id=4, name="Simba", species="Cat", owner_id=4),
    Pet(id=5, name="Charlie", species="Dog", owner_id=5),
    Pet(id=6, name="Bella", species="Dog", owner_id=6),
    Pet(id=7, name="Milo", species="Cat", owner_id=7),
    Pet(id=8, name="Rocky", species="Dog", owner_id=8),
    Pet(id=9, name="Daisy", species="Dog", owner_id=9),
    Pet(id=10, name="Oreo", species="Cat", owner_id=10),
    Pet(id=11, name="Shelly", species="turtle", owner_id=1),
    Pet(id=12, name="Leonardo", species="turtle", owner_id=2),
    Pet(id=13, name="Raphael", species="turtle", owner_id=3),
    Pet(id=14, name="Polly", species="bird", owner_id=8),
    Pet(id=15, name="Tweety", species="bird", owner_id=1),
]

APPOINTMENTS = [
    Appointment(id=1, pet_id=1, vet_id=1, date="2023-02-15", time="0900"),
    Appointment(id=2, pet_id=2, vet_id=2, date="2023-02-15", time="0900"),
    Appointment(id=3, pet_id=5, vet_id=4, date="2023-02-15", time="0900"),
    Appointment(id=4, pet_id=None, vet_id=3, date="2023-02-15", time="0900"),
    Appointment(id=5, pet_id=None, vet_id=5, date="2023-02-15", time="0900"),
    Appointment(id=6, pet_id=None, vet_id=1, date="2023-02-18", time="1100"),
    Appointment(id=7, pet_id=None, vet_id=1, date="2023-02-19", time="1100"),
    Appointment(id=8, pet_id=None, vet_id=2, date="2023-02-19", time="1100"),
    Appointment(id=9, pet_id=None, vet_id=3, date="2023-02-19", time="1100"),
    Appointment(id=10, pet_id=None, vet_id=4, date="2023-02-19", time="1100"),
    Appointment(id=11, pet_id=8, vet_id=3, date="2023-02-17", time="1000"),
    Appointment(id=12, pet_id=10, vet_id=5, date="2023-02-18", time="0900"),
    Appointment(id=13, pet_id=1, vet_id=1, date="2023-02-18", time="1000"),
    Appointment(id=14, pet_id=2, vet_id=2, date="2023-02-18", time="1400"),
    Appointment(id=15, pet_id=3, vet_id=3, date="2023-02-19", time="0900"),
    Appointment(id=16, pet_id=4, vet_id=4, date="2023-02-19", time="1000"),
    Appointment(id=17, pet_id=5, vet_id=5, date="2023-02-19", time="1100"),
    Appointment(id=18, pet_id=6, vet_id=1, date="2023-02-20", time="0800"),
    Appointment(id=19, pet_id=8, vet_id=3, date="2023-02-20", time="1200"),
    Appointment(id=20, pet_id=10, vet_id=5, date="2023-02-21", time="1000"),
    Appointment(id=21, pet_id=1, vet_id=1, date="2023-02-21", time="1300"),
    Appointment(id=22, pet_id=2, vet_id=2, date="2023-02-22", time="1200"),
    Appointment(id=23, pet_id=3, vet_id=3, date="2023-02-22", time="1000"),
    Appointment(id=24, pet_id=4, vet_id=4, date="2023-02-22", time="1100"),
    Appointment(id=25, pet_id=5, vet_id=5, date="2023-02-23", time="0900"),
    Appointment(id=26, pet_id=6, vet_id=1, date="2023-02-23", time="1000"),
    Appointment(id=27, pet_id=8, vet_id=3, date="2023-02-24", time="0300"),
    Appointment(id=28, pet_id=10, vet_id=5, date="2023-02-24", time="1200"),
]


def seed_db(session):
    """Add the starting rows. Owners and vets first, then pets, then appointments,
    so every foreign key points at a row that already exists."""
    session.add_all(OWNERS)
    session.add_all(VETS)
    session.flush()
    session.add_all(PETS)
    session.flush()
    session.add_all(APPOINTMENTS)
    session.commit()
