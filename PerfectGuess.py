import random

class game:
    number = random.randint(1,1000)
    guessesDone=[]
    # print(number,"selected number") #for testing purposes

    def __init__(self, name):
        self.name=name
        print(f"🎮 The Perfect Guess game welcomes you {name}\nI challenge you to guess my number which ranges from 1 to 1000\nThe Game begins...")

    def guess(self):
        inp=int(input("Enter your guess: "))
        return inp

    def store(self, guess):
        if guess in self.guessesDone:
            print("Dear, You already tried this!🔁")

        else:
            self.guessesDone.append(guess)
            
            with open (f"Guesses by {self.name}","a") as txt:
                txt.write(guess+"\n")
    
    def length(self):
        count = len(self.guessesDone)
        return count
    
    def correct(self,selected):
        guesses=self.length()
        print(f"🎉 Damn, You guessed it right!\nIt was {selected}\n\nYou took a total of {guesses} guesses")

    def high(self):
        print("📉 Oops! try a smaller number:\n")

    def low(self):
        print("📈 Oops! try a bigger number:\n")
        
    def run(self):
        selected=self.number
        guessed = self.guess()
        self.store(str(guessed))
        if guessed == selected:
            self.correct(selected)
        else:
            if guessed > selected:
                self.high()
            elif guessed < selected:
                self.low()

            return self.run()

def playerName():
    user=str(input("Enter the player's name:\n"))
    user=user.lower()
    username=user.capitalize()
    return username

def clearGuesses(username):
    with open(f"Guesses by {username}","w") as create:
        pass

username = playerName()
clearGuesses(username)
player=game(username)
player.run()