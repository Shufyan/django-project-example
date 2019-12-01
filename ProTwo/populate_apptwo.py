import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from AppTwo.models import Users
from faker import Faker

fakegen = Faker()

def populate_users(N=5):
    
    for entry in range(N):

        # Create the fake data for entry
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        email = fakegen.email()
        
        # Create new User entry
        user = Users.objects.get_or_create(first_name=first_name,last_name=last_name,email=email)[0]

if __name__ == '__main__':
    print('populating script statted!')
    populate_users(10)
    print('populating completed!')





