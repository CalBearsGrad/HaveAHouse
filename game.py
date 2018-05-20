value = 0
age = 0
balance = 0
home = (value, age)

home_type = {
  1 : { "name" : "rural",
        "cost" : "125000"},
  2 : { "name" : "suburb",
        "cost" : "400000"},
          }

#repairs = (name, cost, value)
repairs = {
  1 : { "name" : "bathroom",
        "cost" : "10000",
        "chg_value" : value*.60 },
  2 : { "name" : "window",
        "cost" : "500",
        "chg_value" : value*.80 },
  3 : { "name": "washing",
        "cost" : "5000",
        "chg_value" : value*.90 },
          }
#improvements = (name, cost, value)
improvements = {
  1 : { "name" : "solar",
        "cost" : "10000",
        "chg_value" : value*1.2 },
  2 : { "name" : "paint",
        "cost" : "1000",
        "chg_value" : value*1.02 },
  3 : { "name": "addition",
        "cost" : "25000",
        "chg_value" : value*1.3 },
              }

def start():
    print("Hi welcome to your home ownership experience!")
    print("Choose your home type:")
    home_start = raw_input("A.   2-bdrm in suburbia B.   2-bdrm rural property")
    if home_start == "A"
        play(home_type[0])
    if home_start == "B"
        play(home_type[1])
    else
        print("Pick your home type, A/B")

    print("Your new home! Take good care of it!")

# output the choice

# this function starts the game with presets for the house
def play(home_type):
#check if you've won!
    if value > 75000
        print("Congrats you've increased your house in value - maybe it's time to sell")

#your house becomes 3 mos older
    age = age+1

#things happen this quarter
    event =

    action = raw_input("Would you like to A.   Save money B.   Repair something C.   Home improvement time!")
# maybe a different word for improvement (vs repair)

    if action == "A"
        balance = balance+3000

    if action == "B"
        if repairs = [] #if there are no available repairs
            print("No repairs are needed!")
        else
            print("You have these repairs to do:")
            for i in repairs:
                item_choice = i+1
                print(item_choice, repairs[i])
            repair_action = raw_input("Which repair would you like to do?")
                if repair_action == item_choice+1 && repairs[i].cost<balance
                    balance = balance - repairs[i].cost
                    value = value + repairs[i].value
                    # remove the item from the repairs object
                if repair_action == item_choice + 1 & & repairs[i].cost > balance
                    print("You need to save up!")
                    play()
                else
                    play()

    if action == "C"
        if improvements = [] #if there are no available improvements
            print("No more improvements to make, Oh well")
        else
            print("You can choose these improvements:")
            for i in improvements:
                item_choice = i+1
                print(item_choice, improvements[i])
            improve_action = raw_input("Which improvement would you like to do?")
                if improve_action == item_choice+1 && improvements[i].cost<balance
                    balance = balance - improvements[i].cost
                    value = value + improvements[i].value
                    # remove the item from the improvements object
                if improve_action == item_choice+1 && improvements[i].cost>balance
                    print("You need to save up!")
                    play()
                else
                    play()

    # win state
