# from https://github.com/Coding-Crashkurse/Pydantic-v2-crashcourse
from typing import List
from pydantic import BaseModel, EmailStr, PositiveInt, conlist, Field, HttpUrl, __version__

print('pydantic version:', __version__)
print()

class Address(BaseModel):
  street: str
  city: str
  state: str
  zip_code: str

class Employee(BaseModel):
  name: str
  position: str
  email: EmailStr

class Owner(BaseModel):
  name: str
  email: EmailStr

class Restaurant(BaseModel):
  name: str = Field(..., pattern=r"^[a-zA-Z0-9-' ]+$")
  owner: Owner
  address: Address
  employees: conlist(Employee, min_length=2)
  number_of_seats: PositiveInt
  delivery: bool
  website: HttpUrl

# Creating an instance of the Restaurant class
restaurant_instance = Restaurant(
    name="Tasty Bites",
    owner={
        "name": "John Doe",
        "email": "john.doe@example.com"
    },
    address={
        "street": "123, Flavor Street",
        "city": "Tastytown",
        "state": "TS",
        "zip_code": "12345",
    },
    employees=[
        {
            "name": "Jane Doe",
            "position": "Chef",
            "email": "jane.doe@example.com"
        },
        {
            "name": "Mike Roe",
            "position": "Waiter",
            "email": "mike.roe@example.com"
        }
    ],
    number_of_seats=50,
    delivery=True,
    website="http://tastybites.com"
)

# Printing the instance
print(restaurant_instance)
