list_of_stocks = {
    "info" : [600, 630, 620],
    "ril" : [1430, 1490, 1567],
    "mtl" : [234, 180, 160]
}
# list_of_stocks["hello"] = [345]

def print_all():
    for stock in list_of_stocks:
        avg = 0.0
        for price in list_of_stocks[stock]:
            avg+=price

        avg = avg/len(list_of_stocks[stock])
        print(f"{stock} ==> {list_of_stocks[stock]}  avg: {round(avg, 2)}")

    
def add():
    user_stock = input("Enter a stock")
    user_stock_price = int(input("Enter the stock price"))
    if user_stock in list_of_stocks:
        lis = list_of_stocks[user_stock]
        lis.append(user_stock_price) 
    else:
        list_of_stocks[user_stock] = [user_stock_price]
    print_all()



user = input("Enter an operation: ")
user = user.lower()

if user == "print":
    print_all()
else:
    add()

