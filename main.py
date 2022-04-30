from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

repeat_input = False         # Create flag variable 
empty_dict = {}              # Create empty dict

def final_dict(bidders_dict):
  highest_bid = 0                 # Create empty variable for the value
  name_with_highest_bid = ""     # Create empty variable for the string
  for bidder in bidders_dict:      # Iterate through the key (name) of the dict
    bid_amount = bidders_dict[bidder] 
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      name_with_highest_bid = bidder
  print(f"The winner is {name_with_highest_bid} with a bid of ${highest_bid}.")

while not repeat_input:          # While not False : True
  name = input("What is your name?\n")
  bid = int(input("What is your bid price? \n$"))
  empty_dict[name] = bid          # To add key-value pair to that empty dict
  anymore_users = input("Are there anymore users who want to bid? Type 'yes' or 'no'.\n").lower()
  if anymore_users == 'yes':
    clear()                  # Clear the output so next user won't see previous output
  elif anymore_users == 'no':
    repeat_input = True          # Will become False and stop loop
    final_dict(bidders_dict = empty_dict)