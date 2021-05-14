import song as sng

print("Welcome to Musical Lake Program \n")
print("For exiting, input the word \"end\" \n\n")
sound = "init"
while sound != "end":
    sound = input("Input a sound: ")
    print(sng.singsong(sound))

