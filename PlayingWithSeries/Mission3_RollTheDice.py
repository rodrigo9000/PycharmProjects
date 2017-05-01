# User should be able to enter how many dices he wants to roll: 1 ,2 or 3. He should pass this value as a parameter in the
# function RollTheDice(num). Dices should show random numbers from 1 to 6.
import random
def main():
    def RollTheDice(num):
        if num in [1, 2, 3]:
            for turns in range(1, (num + 1)):
                print "Dice {} is number: ".format(turns), random.randint(1, 6)
        else:
            print "Number out of range"

    RollTheDice(1)


if __name__== "__main__": main()