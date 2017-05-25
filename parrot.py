# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# the input() function pauses your program and waits for the user to enter something
# takes one argument: the prompt
# the input is stored as the variabl message

prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#
#     if message != 'quit':
#         print(message)


# 'active' is a flag that tells the program to run while true and quit when false
# does the same as the while loop above
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
