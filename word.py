import os
import requests
import json

# Get the API key
apiKey = os.getenv('wordKey')

class Word:
	   
	def __init__(self, headword):  
		self.headword = headword  
	
		# Craete an empty list attribute that will store the api information
		self.apiInfo = []

		self.get_word_info()


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

		print(self.apiInfo)

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