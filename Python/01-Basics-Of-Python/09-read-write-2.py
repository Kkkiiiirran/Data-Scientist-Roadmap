with open("stocks.csv") as file, open("output.csv", "w") as output:
    output.write("Company Name, PE Ratio, PB Ratio\n")
    next(file)

    for line in file:
        column = line.split(",")
        stock = column[0]
        price = float(column[1])
        eps = float(column[2])
        book_value = float(column[3])

        pe_ratio = round(price/eps, 2)
        price_to_book_ratio = round(price/book_value, 2)
        output.write(f"{stock},{pe_ratio},{price_to_book_ratio}\n")

