from time import sleep as s
import random as r


class MacbethQuotes:

    def easy(self):
        pass

    def normal(self):
        pass

    def hard(self):
        pass

    def leaderboard(self):
        pass

    def about(self):
        print(open("assets/logo.txt", "r", encoding="UTF-8").read())
        print("Macbeth Quote Tester")
        s(1)
        print("Finn O'Neill, 2020")
        s(1)
        print("Quotes from William Shakespeare's 'Macbeth'")
        s(1)
        print("Current Version - 0.0.1")

    def __init__(self):
        print(open("assets/logo.txt", "r", encoding="UTF-8").read())
        print("\nQuote Tester - [0.0.1]")
        s(1)
        print("By Finn O'Neill, 2020\n")
        s(1)
        picked = False
        while not picked:
            try:
                print("What would you like to do?\n1) Easy Mode\n2) Normal Mode\n3) Hard Mode\n4) Look at the leaderboard [BETA]\n5) About")
                option = int(input())
                picked = True
            except:
                print("\nAn error occurred!\nMake sure your putting in numbers within the given range!\n")
        picked = False
        while not picked:
            if option == 1:
                self.easy()
                picked = True
            elif option == 2:
                self.normal()
                picked = True
            elif option == 3:
                self.hard()
                picked = True
            elif option == 4:
                self.leaderboard()
                picked = True
            elif option == 5:
                self.about()
                picked = True
            else:
                print("An error occurred! Make sure your putting in numbers within the given range!")


if __name__ == "__main__":
    MacbethQuotes()
