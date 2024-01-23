car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("year", 15000)
print(x)
x = car.get("price", 15000)
print(x)