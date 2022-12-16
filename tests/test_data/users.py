from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Pysics'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    gender: Gender
    name: str
    last_name: str = 'Lukyanov'
    email: str = 'lukyanov@qaguru.com'
    user_number: str = '89111201212'
    birth_day: str = '04'
    birth_month: str = 'May'
    birth_year: str = '1990'
    subjects: Tuple[Subject] = (Subject.History, )
    current_address: str = 'Russia Saint-P Moskovskaya 20'
    hobbies: Tuple[Hobby] = (Hobby.Sports, )
    picture_file: str = 'photo.jpg'
    state: str = 'Haryana'
    city: str = 'Karnal'


student = User(name='Evgeniy', gender=Gender.Male)
