import random

def chatbot():
  print("Welcome to the chatbot!")
  while True:
    user_input = input("You: ").lower()
    if user_input == "hello":
      responses = ["Hi!", "Hey!", "Hello!"]
      print("Chatbot:", random.choice(responses))
    elif user_input == "how are you":
      responses = ["I'm good, thanks!", "I'm doing well.", "I'm great, thanks for asking!"]
      print("Chatbot:", random.choice(responses))
    elif user_input == "what is your name":
      print("Chatbot: My name is Chatbot.")
    elif user_input == "exit":
      print("Chatbot: Goodbye!")
      break
    else:
      print("Chatbot: Sorry, I didn't understand that.")

chatbot()
