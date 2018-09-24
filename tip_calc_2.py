ERROR_MESSAGE = "Bad user input."
try:
    total_bill = float(input("Total bill amount? "))
    service_level = input("Level of service? ")
    ways_split = int(input("Split how many ways? "))
    if service_level == "good":
        percent_tip = .20
    elif service_level == "fair":
        percent_tip = .15
    elif service_level == "bad":
        percent_tip = .10
    else:
        percent_tip = 1.0
    tip_amount = total_bill * percent_tip
    total_amount = total_bill + tip_amount
    amount_per_person = total_amount / ways_split
    print("Tip amount: $%.2f" % tip_amount)
    print("Total amount: $%.2f" % total_amount)
    print("Amount per person: $%.2f" % amount_per_person)
except:
    print(ERROR_MESSAGE)    