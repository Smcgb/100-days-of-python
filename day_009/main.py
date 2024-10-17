import art

bids = {}

def add_bidder(name, price):
    bids[name] = price

while True:
    print(art.logo)
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))

    add_bidder(name, price)
    print('\n' * 100)
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "no":
        break


highest_bidder = max(bids, key=bids.get)

print(f"The winner is {highest_bidder} with a bid of ${bids[highest_bidder]}")



