'''Coffee Machine'''

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 20,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 30,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 35,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def report():
    '''prints all the available resourses'''
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Profit: {profit} rs")


def enough_resources(order):
    '''checks if there are enough resources to prepare the given order 
    (returns 0 if resources insufficient)'''
    for x in MENU[order]['ingredients']:
        if resources[x] < MENU[order]['ingredients'][x]:
            return 0
    return 1


def process_coins(order):    
    '''Takes the coin input from the user and subtracts cost of order and returns the change'''
    global profit
    print("Please insert coins.")
    rupees = int(input("How many rupees?: "))
    # aathane is half of a rupee or 50 paise
    aathane = int(input("How many aathane?: "))
    # charane is quarter of a rupee or 25 paise
    charane = int(input("How many charane?: "))
    paise = int(input("How many paise?: "))  # paise is a paisa

    in_rupees = rupees + aathane/2 + charane/4 + paise/100
    # print(in_rupees)
    if MENU[order]["cost"] > in_rupees:
        print("Sorry that's not enough money. Money Refunded")
        return 0
    profit += MENU[order]["cost"]
    change = in_rupees - MENU[order]["cost"]
    print(f"Here's your ₹{change:.2f} change.")
    return 1


def prepare_order(order):
    '''A function to prepare order, which is taken as parameter'''
    for item in resources:
        if(item == "milk" and order == "espresso"):
            continue
        resources[item] -= MENU[order]["ingredients"][item]
    print(f"Here's your {order}. Enjoy! ")


def main():
    '''A function that's main'''
    while(True):
        user_input = input(
            '''What would you like?
                A - Espresso
                B - Latte
                C - Cappuccino: 
                ''')

        if(user_input == "off"):
            break
        if(user_input == "report"):
            report()
            continue
        if(user_input == "A"):
            order = "espresso"
        elif(user_input == "B"):
            order = "latte"
        elif(user_input == "C"):
            order = "cappuccino"
        enough_resources_val = enough_resources(order)

        if enough_resources_val == 0:
            print(
                "Sorry! We don't have enough resources, \nMaintainer of the machine has been informed.")
            continue

        process_coins_val = process_coins(order)

        if process_coins_val == 0:
            continue

        prepare_order(order)

if __name__ =="__main__":
    main()
