import word
import time

class WordGame:
	   
	def __init__(self, numberOfWords):  
		self.numberOfWords = numberOfWords
		self.gameWords = []
		self.createWords()
		self.play_game()
	
	
	def createWords(self):
		num = 1
		while num < self.numberOfWords:
			myWord = self.solicitWord()
			gameWord = word.Word(myWord)
			self.gameWords.append(gameWord)
			num += 1

	def solicitWord(self):
		print("Please enter word: ")
		userWord = input()
		return userWord


	def play_game(self):
		for word in self.gameWords:
			word.get_definitions_and_examples()
			syllables = word.get_syllables()
			print("How many syllables does \"{}\" have? See examples above".format(word.headword))
			userSyllalesGuess = input()

			if int(userSyllalesGuess) == int(syllables):
				print("Yes you win, loading next word")
			else:
				print("No the word has {}, loading next word".format(syllables))
			time.sleep(1)
