from time import sleep as s
import random as r
import csv

with open("assets/macbeth.quotes", encoding="utf8") as f:
		read = csv.reader(f)
		quotes = list(read)



class MacbethQuotes:

    def easy(self):
        print("Coming soon!")

    def normal(self):
        lives = 3
        name = input("What is your name?")
        while True:

            global points

            q = r.randint(0, len(quotes) - 1)
            phrase = quotes[q][0].split()
            for i in range(len(phrase)):
                newWord = ""
                for k in range(len(phrase[i])):
                    if phrase[i][k] == "|":
                        LetterToPut = ","
                    elif phrase[i][k] == "/":
                        LetterToPut = '\n'
                    else:
                        LetterToPut = phrase[i][k]
                    newWord = newWord + LetterToPut
                phrase[i] = newWord


            remword = r.randint(0, len(phrase) - 1)
            dash = ""
            remwordstr = phrase[remword]

            for j in range(len(phrase[remword])):
                dash = dash + "_"

            phrase[remword] = dash
            phrase = " ".join(phrase)
            print(phrase)
            ans = input("What is the missing word from the quote?\n")
            if ans.lower() == remwordstr.lower():
                points = points + 1
                print(f"\nWell done, {name}! You have {points} point(s), and {lives} lives left.\n")
            else:
                lives = lives - 1
                if lives < 0:
                    print(f"\nSorry, {name}. Your're out of lives. You got {points} point(s)")
                    print(f"\nThe correct answer is {remwordstr}")
                    break
                print(f"\nIncorrect answer, {name}. Better luck next time! You have {points} point(s), "
                      f"and {lives} lives left.\n")
                print(f"The correct answer is {remwordstr}\n")

    def hard(self):
        print("Coming soon!")

    def leaderboard(self):
        print("Coming soon!")

    def about(self):
        print(open("assets/macbeth.logo", "r", encoding="UTF-8").read())
        print("Macbeth Quote Tester")
        s(1)
        print("Finn O'Neill, 2020")
        s(1)
        print("Quotes from William Shakespeare's 'Macbeth'")
        s(1)
        print("Current Version - 0.0.1")

    def __init__(self):
        global points
        while True:
            points = 0
            print(open("assets/macbeth.logo", "r", encoding="UTF-8").read())
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
            print("Thanks for playing! Would you like to try again?")
            answer = input().lower()

            picked = False
            while not picked:
                if answer == "y":
                    picked = True
                elif answer == "n":
                    exit(print("Bye Bye!"))
                else:
                    print("Sorry, I don't understand this!")



if __name__ == "__main__":
    MacbethQuotes()
