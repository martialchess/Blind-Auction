import art
print(art.logo)

# Step 1: create an empty dictionary to hold all bids
bids = {}

#Step 2: create a function to find the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

#Step 3: Loop for multiple bidders
should_continue = True
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    #save the bid into the dictionary
    bids[name] = bid

    # Quit program if no more players
    restart = input("Are there other bidders? Type 'yes' or 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        find_highest_bidder(bids)
    else:
        print("\n" * 20) #clear screen