from time import sleep as s
import random as r
import csv

with open("assets/macbeth.quotes", encoding="utf8") as f:
    read = csv.reader(f, delimiter='|')
    quotes = list(read)


class MacbethQuotes:
    points = 0

    def easy(self):
        print("Coming soon!")

    def normal(self):
        lives = 3
        name = input("What is your name? ")
        print("\n")
        while True:

            q = r.randint(0, len(quotes) - 1)
            phrase = quotes[q][1].split()
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
            newWord = ""
            for l in range(len(phrase[remword])):
                if phrase[remword][l] == ",":
                    LetterToPut = ""
                elif phrase[remword][l] == "!":
                    LetterToPut = ""
                else:
                    LetterToPut = phrase[remword][l]
                newWord = newWord + LetterToPut
            remwordstr = newWord

            dash = ""
            newWord = ""
            for j in range(len(phrase[remword])):
                if phrase[remword][j] == ",":
                    dash = dash + ","
                elif phrase[remword][j] == "!":
                    dash = dash + "!"
                else:
                  dash = dash + "_"

            phrase[remword] = dash
            phrase = " ".join(phrase)
            print(phrase)
            ans = input("What is the missing word from the quote?\n")
            if ans.lower() == remwordstr.lower():
                self.points = self.points + 1
                print(f"\nWell done, {name}! You have {self.points} point(s), and {lives} lives left.\n")
            else:
                lives = lives - 1
                if lives < 0:
                    print(f"\nSorry, {name}. Your're out of lives. You got {self.points} point(s)")
                    print(f"\nThe correct answer is {remwordstr}")
                    break
                print(f"\nIncorrect answer, {name}. Better luck next time! You have {self.points} point(s), "
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
        print("Follow me on GitHub! https://github.com/Explorer017")

    def menu(self):
        while True:
            self.points = 0
            picked = False
            while not picked:
                try:
                    print(
                        "What would you like to do?\n1) Easy Mode\n2) Normal Mode\n3) Hard Mode\n4) Look at the leaderboard [BETA]\n5) About")
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

    def __init__(self):
        print(open("assets/macbeth.logo", "r", encoding="UTF-8").read())
        print("\nQuote Tester - [0.0.1]")
        s(1)
        print("By Finn O'Neill, 2020\n")
        s(1)
        self.menu()





if __name__ == "__main__":
    MacbethQuotes()
