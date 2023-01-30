import random
import time

print('hello user, welcome to this small code.')
time.sleep(2)
print('today i will tell you a story, that you may wich rewrite by choosing options.')
time.sleep(2)
print('choose the number 1 if u wanna play the story or choose 2 if u dont.')
choice = input('choose: ')
while True:
    if choice == "1":
        print('good choice.')
        time.sleep(2)
        print("so, you're walking down in the sreet's of Blaha.")
        time.sleep(2)
        print("a man walk's up to you and say's: - hello sir. do you have a cigarett, i need it for a bus ticket.")
        time.sleep(2)
        print("you've got 3 options.")
        print("1. you give him the cigarett he asked for and hope he dosen't stab you.")
        print("2. you don't give him what he asked for.")
        print("3. you run thinking its the safest option in this moment.")
        choice1 = input("you choose: ")
        if choice1 == "1":
            print("he appreciate it and walk's off.")
            time.sleep(2)
            print("you are relifed that you we're not shanked.")
            time.sleep(2)
            print("Happy ending")
            break  
        elif choice1 == "3":
            print("you start running as fast as you can.")
            time.sleep(2)
            print("the man seems to start chasing you, but you just keep running.")
            time.sleep(2)
            print("you have seem to come up in a bad situation as you've got not much option here.")
            time.sleep(2)
            print("as the time passes by as you think, the man quickly chatches up to you and in a brief moment you we're shanked.")
            time.sleep(2)
            print("Bad ending")
            break
        else: print("he didn't like your answer and he stab you.")
        time.sleep(2)
        print("Bad ending")
        break
    else:
        print('you dont seem to understand the story must be played.')
        time.sleep(2)
        print("try again, maybe you will change you're mind.")
        time.sleep(2)
        break
    
