import os
import requests
import json

apiKey = os.getenv('wordKey')


class Word:  
	   
	def __init__(self, headword):  
		self.headword = headword  
	
		# Craete an empty list attribute that will store the api information
		self.apiInfo = []


	def get_word_info(self):


		url = "https://wordsapiv1.p.rapidapi.com/words/" + self.headword

		headers = {
			'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
			'x-rapidapi-key': apiKey
		}

		response = requests.request("GET", url, headers=headers)

		responseText = response.text
		responseJSON = json.loads(responseText)

		self.apiInfo.append(responseJSON)

	def get_definitions_and_examples(self):

		for entry in self.apiInfo[0]['results']:
			print("Definition: ")
			print(entry["definition"])
			print("")
			
			try:
				print("Example: ")
				for sentence in entry["examples"]:
					print(sentence)
				print("")
			except:
				print("no examples")
				print("")

	def get_syllables(self):

		#print(self.apiInfo[0]['syllables']['count'])
		return self.apiInfo[0]['syllables']['count']


print("Welcome to the word game")
print("Please enter your favorite word")

userWord = input()
gameWord = Word(userWord)
gameWord.get_word_info()
gameWord.get_definitions_and_examples()

syllables = gameWord.get_syllables()

print("How many syllables does the word have?")

userSyllalesGuess = input()

if int(userSyllalesGuess) == int(syllables):
	print("Yes you win")
else:
	print("No the word has {}".format(syllables))