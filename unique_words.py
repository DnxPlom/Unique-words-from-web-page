import bs4
from urllib.request import Request, urlopen

from binary_search import binary_search

page_link = "https://www.geeksforgeeks.org/java-retention-annotations/"

def unique_words(link):
	r = Request(link, headers={'User-Agent': 'Mozilla/5.0'})

	webpage=urlopen(r).read()
	soup = bs4.BeautifulSoup(webpage, features="html.parser")

	raw = soup.get_text()
	formatted_text = ""

	for i in raw:
		if i.isalpha(): formatted_text += i
		else: formatted_text += " "

	words_dict = {}

	for i in formatted_text.split():
		if i in words_dict: words_dict[i] += 1
		else: words_dict[i] = 1

	#print(words_dict)
	unique_words = [x for x in words_dict if words_dict[x] == 1]
	# print(unique_words)

	return unique_words

# offline comparison 
def compare_to_english(link):

	### Words from the english dictionary
	with open('dict.txt', 'r') as f:
		file = f.read()
		english_words = file.split()
		english_words.sort()
	# print(english_words)

	page_unique_words = unique_words(link)

	eng_words = []
	eng_words2 = []

	for i in page_unique_words:
		if binary_search(english_words, i):
			eng_words.append(i)
	
	# for i in page_unique_words:
	# 	if i in english_words:
	# 		eng_words2.append(i)

	# print(len(eng_words))
	# print(len(eng_words2))
	return eng_words

print(compare_to_english(page_link))
