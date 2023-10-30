personal_data = {
    'first_name' : 'wiola',
    'last_name' : 'warner',
    'age' : 40,
    'city' : 'london',
    }

personal_data_1 = {
    'first_name' : 'mario',
    'last_name' : 'nocny',
    'age' : 45,
    'city' : 'żory',
    }

personal_data_2 = {
    'first_name' : 'natalie',
    'last_name' : 'baker',
    'age' : 47,
    'city' : 'amsterdam',
    }

people = [personal_data, personal_data_1, personal_data_2]

for person in people:
    first_name = person['first_name']
    last_name = person['last_name']
    age = person['age']
    city = person['city']
    print(f"\n{first_name.title()} {last_name.title()} "
        f"aged {age} lives in {city.title()}.")
