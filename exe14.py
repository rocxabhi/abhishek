from sys import argv
script, user_name = argv
prompt = '>'
print(f"Hi {user_name}, I'am the {script} script")
print("I'd like to ask you a few questions.")
print(f"So you Like me {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}?")
lives = input(prompt)
print("What kind of computer do you have")
computer = input(prompt)
print(f"""So you have said: {likes} about liking me.
You live in {lives}.
And you have a {computer} computer.""")
