import bs4
from urllib.request import Request, urlopen

link = "https://www.geeksforgeeks.org/java-retention-annotations/"

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
print(unique_words)
