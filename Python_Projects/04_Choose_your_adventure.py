#
name = input("Type Your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on dirt road, it has come to an end and you can go left or right. Which way would you like to go?  "
).lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: "
    ).lower()

    if answer == "swim":
        print("you swim accross and were eated by aligator ☠️")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game ☠️")
    else:
        print("Not a valid option. You loose.❌")
elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? "
    ).lower()

    if answer == "back":
        print("You win")

    elif answer == "cross":
        answer = input(
            "You crossed the bridge and meet a stranger. Do you talk to him (yes/no)? "
        ).lower()
        if answer == "yes":
            print("you talk to stranger and they give you gold. You loose. Note => don`t take anything from strangers")
        elif answer == "no":
            print("You loose because you don`t believe on others you are arrogant.")
        else:
            print("Not a valid option. You loose ❌.")
    else:
        print("Not a valid option. You loose ❌.")

else:
    print("Not a valid option. You loose ❌.")
