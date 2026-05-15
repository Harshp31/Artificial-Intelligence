# list = [1, 2, 3, 4, 5]

# list.append(6) # adds an element to the end of the list
# list.insert(0, 0) # adds an element at a specific index
# list.remove(1) # removes the first occurrence of the specified value
# list.pop() # removes the last element of the list
# list.sort() # sorts the list in ascending order
# list.clear() # removes all elements from the list
# list.reverse() # reverses the order of the list
# list.count(2) # counts the number of occurrences of a specific value
# list.index(3) # returns the index of the first occurrence of a specific value


# squares = [x * x for x in range(5)]
# print(squares)

# matrix = [[1, 2], [3, 4]]
# print(matrix[0][1]) # Output: 2

# a = [1, 2, 3]
# b = a # b references the same list as a
# a.append(4) # Modifying the list through a

# print(b) # Output: [1, 2, 3, 4] - b reflects the change made through a




#Shopping Cart program

# foods = []
# prices = []
# total = 0

# while True: 
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input("Enter the price of the food: "))
#         foods.append(food)
#         prices.append(price)

# print("------Your Cart-------")

# for food in foods:
#     print(food, end=" ")

# for price in prices:
#     total += price #total = total + price

# print()
# print(f"Your total is: ₹{total}")


# 2D Lists: - A 2D list is a list of lists. It can be used to represent a matrix or a grid.

# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["carrot", "potatoes", "broccoli"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]
# groceries = [["apple", "orange", "banana", "coconut"],
["carrot", "potato", "broccoli"],
#                 ["chicken", "fish", "turkey"]]

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")

# print(groceries[0][0]) # Output: apple
# print(groceries[2][2]) # Output: turkey




# two Dimensional keypad

# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*", 0, "#"))

# for row in num_pad:
#     for key in row:
#         print(key, end=" ")
#     print()

#Python Quiz game

questions = ("How many elements are in the periodic table?",
             "which animal lays the largest eggs?",
             "what is the most abundant gas in the Earth's atmosphere?",
             "How many bones are in the human body?",
             "which planet in the solar system is the hottest?")

options = (("A. 116 ", "B. 117", "C. 118", "D. 119"),
            ("A. Whale", "B. crocodile", "C. Elephant", "D. Ostrich"),
            ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
            ("A. 206", "B. 201", "C. 210", "D. 205"),
            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C. 118", "D. Ostrich", "A. Nitrogen", "A. 206", "B. Venus")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter your answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"{answers[question_num]} was the correct answer.")

    question_num += 1

    print()


    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()


score  =  int(score / len(questions) * 100)
print(f"Your score is: {score}%")

