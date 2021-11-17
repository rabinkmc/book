from random import choice
from book.models import Publisher

from book.constants import NAME, CITY, ADDRESS, STATE_PROVINCE, COUNTRY

def load_publisher():
    for _ in range(10):
        Publisher.objects.create( 
                name = choice(NAME), 
                city =choice(CITY),
                address = choice(ADDRESS),
                state_province = choice(STATE_PROVINCE),
                country = choice(COUNTRY)
                )

