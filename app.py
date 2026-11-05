"""
SQLAlchemy Lab 02
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine, init_db
from models import Owner, Vet, Pet, Appointment

# Create and fill vet.db if it doesn't exist yet
init_db()

with Session(engine) as session:

    # Query 1: All owners
    stmt = select(Owner)

    print("\nAll Owners: ")
    for owner in session.scalars(stmt):
        print(owner)

    # Query 2: All vets
    stmt = select(Vet)

    print("\nAll Vets: ")
    for vet in session.scalars(stmt):
        print(vet)

    # Query 3: 5 pets and their owners
    # Two things per row (a Pet and an Owner), so we use execute()
    stmt = select(Pet, Owner).join(Owner, Pet.owner_id == Owner.id).limit(5)

    print("\n5 Pets and their Owners: ")
    for pet, owner in session.execute(stmt):
        print(owner.first_name, owner.last_name, "owns a", pet.species, "named", pet.name)

    # Query 4: 5 appointments, with their vet and pet
    # Each join() adds one more table
    stmt = (
        select(Appointment, Vet, Pet)
        .join(Vet, Appointment.vet_id == Vet.id)
        .join(Pet, Appointment.pet_id == Pet.id)
        .limit(5)
    )

    print("\n5 Appointments: ")
    for appt, vet, pet in session.execute(stmt):
        print(f"{vet} has an appointment with {pet.name} on {appt.date} @{appt.time}")
