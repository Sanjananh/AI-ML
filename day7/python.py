
name = input("What is your name? ")
daily_goal = input("What is your Daily Goal? ")


with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Daily Goal: {daily_goal}\n")
