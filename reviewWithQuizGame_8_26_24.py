# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 07:55:19 2024
@author: segal
"""
# making a Quiz game
# 1st require a tuple of questions:

Questions = ("1. Pick one: dog, rat, bird, or cat: ",
             "2. Pick one: red, black, green, or blonde: ",
             "3. Pick one: boots, sneakers,bare-feet, or flip-flops: ",
             "4. Pick one: Truck, walk, scooter, or Car: ",
             "5. Pick one: Steak, chicken, turkey, or shrimp: ",)

# next 2d tuple with 10 questions:
Choices = ( ("A. dog", "B. cat", "C. bird", "D. rat"),
          ("A. red", "B. black", "C. blonde", "D. green"),
          ("A. boots", "B. sneakers", "C. bare-feet", "D. flip-flops"),
          ("A. truck", "B. walk", "C. scooter", "D. car"),
          ("A. steak", "B. chicken", "C. shrimp", "D. turkey"))
# next a tuple of ans
Answers = ( "A", "A", "A", "D", "A",) 
# and a list of guesses:
Guesses = []
# next score var:
Score = 0
# next tracking the number of questions:
QuestionNum = 0
# display each question by iterating over the tuple
for question in Questions:
    print("+++++++++++++++++++++++++")
    print(question)
    for choice in Choices[QuestionNum]:
        print(choice)# that just gives the 1st choice so it must be iterated.
    
    # and allow the user to enter in their guess 1st:
    Guess = input("Enter (A, B, C, D): ").upper()
    Guesses.append(Guess)
    if Guess == Answers[QuestionNum]:
        Score += 1
        print("Correct.")
    else:
        print("Wrong.")
        print(f"{Answers[QuestionNum]} is the correct answer.")
    
    QuestionNum += 1
    
print("+++++++++++++++++++")
print("     Results       ")
print("+++++++++++++++++++")

print("Answers: ", end="")
for answer in Answers:
    print(answer, end = " ")
print()

# do the same with some questions:
print("Guesses: ", end="")
for Guess in Guesses:
    print(Guess, end = " ")
print()

Score = int(Score / len(Questions) * 100)
print(f"Your score is: {Score}%")

    