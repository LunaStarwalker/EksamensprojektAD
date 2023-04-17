import nltk
symbols = ['.',',',':',';','!','?']

f = open(r"macbeth.txt", encoding="latin1")
text = f.read()
f.close()
what = nltk.word_tokenize(text)
sentence_amount = len(nltk.sent_tokenize(text))
word_amount = len(nltk.word_tokenize(text))
long_words = []
for word in what:
    if len(word) > 6:
        long_words.append(word)
long_word_amount = len(long_words)

lixtal = word_amount/sentence_amount+(long_word_amount*100/word_amount)

filtered_list = []
for word in what:
    if word not in symbols:
        filtered_list.append(word)
print(filtered_list)
print('Sentences:',sentence_amount)
print('Words:', word_amount)
print('Long words:', long_word_amount)
print(lixtal)