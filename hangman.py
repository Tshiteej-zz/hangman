import random
class hangman():
    def __init__(self):
        wish = raw_input("Want to start the game..?(y/n)")
        if wish == 'y':
            print "Let's start the game...!"
            self.start_game()
        elif wish == 'n':
            print "So why are you here..!??"
            exit()

    def generate_the_word(self,infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]

    def start_game(self):
        guess = 0
        letters_used = ""
        word = self.generate_the_word("word.txt")
        word_length = len(word)
        progress = ['?'] * word_length
        chances = str(word_length+5)
        print progress
        print "You get " + chances + " chances to save yourself"
        while(guess < word_length+5):
            print "Letters used: " + letters_used
            user_guess = raw_input("Guess the word: ")
            if (user_guess in word) and (user_guess not in letters_used):
                guess += 1
                print "Good"
                print self.progress_bar(user_guess, word, progress)
                if self.progress_bar(user_guess, word, progress).replace(" ", "") == word:
                    print "##################################"
                    print "We spare you this time..!"
                    print "##################################"
                    exit()
                letters_used += "," + user_guess


            elif (user_guess not in word) and (user_guess not in letters_used):
                guess += 1
                print "You wanna die?"
                print self.progress_bar(user_guess, word, progress)
                if self.progress_bar(user_guess, word, progress).replace(" ", "") == word:
                    print "##################################"
                    print "We spare you this time..!"
                    print "##################################"
                    exit()
                letters_used += "," + user_guess
            else :
                print "you wanna be here all day?"
        else:
            print "I guess you're going to hell"
            print "The word was: " + word


    def progress_bar(self, user_guess, word, progress):
        i = 0
        while i < len(word):
			if user_guess == word[i]:
				progress[i] = user_guess
				i += 1
			else:
				i += 1
        return " ".join(progress)

game = hangman()
