from sounds.py import soundmap, song

print("Welcome to Musical Lake Program \n")
print("For exiting, input the word \"end\" \n\n")
sound = "init"
while sound != "end":
    sound = input("Input a sound: ")
    print(song(sound))

