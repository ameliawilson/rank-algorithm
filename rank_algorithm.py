##############################################################################
# Rating Algorithm:
#   Takes Item Price, Gathers data through a questionaire.
#   Mandatory cost taken in to account
#       return rating, free money percent, total income percent
##############################################################################
text_file = open("rank.txt", "a")
# takes input str, returns value for item similarity
def similar(user_str):
    if user_str == 'y':
        return 10
    elif user_str == 'm':
        return 50
    elif user_str == 'n':
        return 100
    else:
        print("INVALID Similar Item input")
        return 0

# takes input str, returns value for item necessity       
def essential(user_str):
    if user_str == 'y':
        return 100
    elif user_str == 'm':
        return 50
    elif user_str == 'n':
        return 10
    else:
        print("INVALID Essential Item input")
        return 0

# takes input str, returns value for item desire        
def desire(user_str):
    if user_str == '1':
        return 10
    elif user_str == '2':
        return 20
    elif user_str == '3':
        return 50
    elif user_str == '4':
        return 70
    elif user_str == '5':
        return 100
    else:
        print("INVALID Item Desire input")
        return 0

# takes free(p1) and total(p2) percent, returns value based on cost impact        
def percent(p1, p2):
    if p1 < .2:
        return 100
    elif p2 < 1 and p1< 1:
        return 75
    elif p1 < 1:
        return 50
    elif p2 < 2:
        return 30
    else:
        return 10 ## i.e this item is way out of budget    
    
# money in
bi_week_income = 334
# money out
groceries = 50 # weekly
electricity = 30*.25 # once a month
gas = 20*.25 # once a month
lease = 179*.25 #once a month
# based off every two weeks
free_money = bi_week_income - (2 * groceries) - (electricity + gas+lease)
#print("Your Income: ", bi_week_income, "\nFree Money: ", free_money, "\n")
print("This progam determines rank for items on your wishlist")
date = input("Please Enter today's date (mm/dd/yy): ")
item_str = input("Please enter the item name: ")
while item_str != "":
    # gather additional data
    price = float(input("Please Enter the price: "))
    store = input("Please Enter the store name: ")
    category = input("Please Enter the item category: ")
    data_1 = input("(y/m/n) Do you own a similar item? ")
    data_2 = input("(y/m/n) Is this item 'essential'? ")
    data_3 = input("On a Scale 1-5, how much do you want it? ")
      
    # Item Percent
    percent_total = (price/bi_week_income)
    percent_free = (price/free_money)
    
    data_4 = percent(percent_free, percent_total)
    score = similar(data_1)+essential(data_2)+desire(data_3)+data_4
    rank = str(score)

    p1 = '{:.1%}'.format(percent_total)
    p2 = '{:.1%}'.format(percent_free)
    price2 = '${:,.2f}'.format(price)
    print()
    print(item_str, price2)
    print(p1, "of a paycheck and", p2, "of spending money.")
    print("Ranking it:", score)
    new_str =item_str+','+rank+','+price2+','+p2+','+p1+','+store+','+category
    new_str = new_str + ',' + date
    print(new_str, file=text_file)
    item_str = input("Please enter the next item name: ")

text_file.close()
# write another program that will sort the lines of the file by rank