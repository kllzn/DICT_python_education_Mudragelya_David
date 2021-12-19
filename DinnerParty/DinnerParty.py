print("Enter the number of friends joining (including you):")
friends_amount = int(input(">"))
if friends_amount == 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for i in range(friends_amount):
        enter = input(">")
        friends[enter] = 0
    print(friends)
