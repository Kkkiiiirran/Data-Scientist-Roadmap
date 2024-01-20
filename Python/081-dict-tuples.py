data = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country = input("Enter a country name to add: ")
    country = country.lower()
    if country in data:
        print(f"Country already exists")
        return
    p = input(f"Enter population of {country}")
    p = float(p)
    data[country] = p
    print_all()

def delete():
    country = input("Enter a country name to remove: ")
    country = country.lower()
    if country not in data:
        print(f"Country does not exist")
        return
    del data[country]
    print_all()

def query():
    country = input("Enter a country name to query: ")
    country = country.lower()
    if country not in data:
        print(f"Country does not exist")
        return
    print(data[country])

def print_all():
    for country in data:
        print(f"{country}==> {data[country]}")

user = input("What do you want to do? (add/delete/query/print): ")
user = user.lower()

if user == "add":
    add()
elif user == "delete":
    delete()
elif user == "query":
    query()
elif user == "print":
    print_all()