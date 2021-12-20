import random

print("Enter the number of friends joining (including you):")
friends_amount = int(input(">"))
if friends_amount <= 0:
    print("No one is joining for the party")

print("Enter the name of every friend (including you), each on a new line:")
friends = {}
for i in range(friends_amount):
    enter = input(">")
    friends[enter] = 0

print("Enter the total amount")
total_amount = int(input(">"))
splitted_check = round(total_amount / friends_amount, 2)
for j in friends:
    friends[j] = splitted_check

print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
enter = input(">")
if enter == "yes":
    luckiest = random.choice(list(friends.keys()))
    print(f"{luckiest} is the lucky one!")
    new_splitted_check = round(total_amount / (friends_amount - 1), 2)
    for i in friends.keys():
        if i == luckiest:
            friends[i] = 0
        else:
            friends[i] = new_splitted_check
    print(friends)
elif enter == "no":
    print("No one is going to be lucky")
    print(friends)
