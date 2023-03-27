

import time

print("Let's find out your personality trait! ")

#list of personality traits
kind = "Kind people are good listeners and takes interest in what others have to say. You never judge others based on assumptions or someones appearance. You are gentle, patient and honest."

independent = "Independent people don't rely on other people for money, help, or emotional reassurance. This means that you don't need others' validation to make decisions and feel good about yourself."

resilient = "Resilient people are flexible and adaptable to change, you don't give up easily. Resilient people have a sense of humor which helps them see the bright sight of life."

bold = "To be bold is to laugh in the face of fear. Bold people are a daring and brave person. You might show how bold you are by climbing onto the roof of your house, or by speaking up when you see someone being treated unfairly."

rounded = "A well-rounded person is someone who is an expert or has the ability to be well informed or well educated in a lot of different things or activities that cover several different genres or subjects."


# set variables for each answer = 0
kind_score = 0
independent_score = 0
resilient_score = 0
bold_score = 0

# Ask for the user name
print("First things first, tell us your name.")
name = input("> ").title()
print()

# Greet the user using their name to make ir more personal and explain the test: print("Hi {name}, welcome to your personality test. ")
print(f"Welcome {name}! You will be given 5 questions with 4 options of answers. At the end we will tell you what's your personality trait! Are you ready to find out?")
print()
print("Here we go!")
print()


while True:
  print("What is your favorite food?")
  print()
  print("[A]- Clam chowder")
  print()
  print("[B]- BLT sandwich")
  print()
  print("[C]- Salad")
  print()
  print("[D]- Spicy bowl of chilli")
  print()
  
#Create conditions to add the input answer to the variable chosen 
  answer_one = input("> ").upper()
  if answer_one == "A":
    kind_score += 1
  elif answer_one == "B":
    independent_score += 1
  elif answer_one == "C":
    resilient_score += 1
  elif answer_one == "D":
    bold_score += 1
  

  print("What is your favorite color?")
  print()
  print("[A]- Pink")
  print()
  print("[B]- Purple")
  print()
  print("[C]- Green")
  print()
  print("[D]- Black")
  print()
#Create conditions to add the input answer to the variable chosen
  answer_two = input("> ").upper()
  if answer_two == "A":
    kind_score += 1
  elif answer_two == "B":
    independent_score += 1
  elif answer_two == "C":
    resilient_score += 1
  elif answer_two == "D":
    bold_score += 1
    

  print()
  print()
  print("What is your favorite location?")
  print()
  print("[A]- Cabin in the mountains")
  print()
  print("[B]- Deserted beach")
  print()
  print("[C]- Foreing country")
  print()
  print("[D]- Deep in the forest")
  print()
#Create conditions to add the input answer to the variable chosen
  answer_three = input("> ").upper()
  if answer_three == "A":
    kind_score += 1
  elif answer_three == "B":
    independent_score += 1
  elif answer_three == "C":
    resilient_score += 1
  elif answer_three == "D":
    bold_score += 1


  print()
  print()
  print("What is your favorite season of the year?")
  print()
  print("[A]- Spring")
  print()
  print("[B]- Fall")
  print()
  print("[C]- Winter")
  print()
  print("[D]- Summer")
  print()
  
#Create conditions to add the input answer to the variable chosen
  answer_four = input("> ").upper()
  if answer_four == "A":
    kind_score += 1
  elif answer_four == "B":
    independent_score += 1
  elif answer_four == "C":
    resilient_score += 1
  elif answer_four == "D":
    bold_score += 1
    

  print()
  print()
  print("What is your favorite type of movie?")
  print()
  print("[A]- Comedy")
  print()
  print("[B]- Action")
  print()
  print("[C]- Documentary")
  print()
  print("[D]- Foreign films")
  print()


#Create conditions to add the input answer to the variable chosen
  answer_five = input("> ").upper()
  if answer_five == "A":
    kind_score += 1
  elif answer_five == "B":
    independent_score += 1
  elif answer_five == "C":
    resilient_score += 1
  elif answer_five == "D":
    bold_score += 1
    
  print("End of the test.")
  print()
  print()

  print("Taking your answers and calculating your personality.")
  timer = 3
  while timer > 0:
    print(timer, "...")
    time.sleep(2)
    timer = timer - 1

  print()
  print()
  print("We have the results!")
  print()
  print()
  print("Let's see which personaly trait fits you the most:")
  print()
  print()
  
#create condition to check which answer had the higher score and print the personality description for that personality
  if kind_score >= 3:
    print(f"{name} your personality trait is kind, here is a brief description for you:")
    print()
    print(kind)
     
  elif independent_score >= 3:
    print(f"{name} your personality trait is independent, here is a brief description for you:")
    print()
    print(independent)
     
  elif resilient_score >= 3:
    print(f"{name} your personality trait is resilient, here is a brief description for you:")
    print()
    print(resilient)

  elif bold_score >= 3:
    print(f"{name} your personality trait is bold, here is a brief description for you:")
    print()
    print(bold)

  else:
    print(f"{name} your personality trait is well-rounded, here is a brief description for you:")
    print()
    print(rounded)
    

  print()
  print()
#ask the user if they would like to play again, if yes continue, if no break and say goodbye {name}.
  print("Would you like to re-take the test?")
  print()
  retake = input("> ").lower()
  if retake.startswith("y"):
    print("Let's start over again.")
    print()
    print()
    continue
  else:
    print(f"Goodbye {name}. See you soon!")
    break