more_bidders = "y"
bidding = {}
while(more_bidders == "y"):
    name = input("Enter Name")
    bid = int(input("Enter bid"))
    bidding[name] = bid
    more_bidders = input("Are there any more bidders?")

highest = 0
winner = ""
for bidder in bidding:
    if highest < bidding[bidder]:
        highest = bidding[bidder]
        winner = bidder
    
print(f"{winner} won the auction")
    


