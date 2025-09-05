import csv


csv_file = open('PROCESSED_DATA.csv', newline='')
reader = csv.reader(csv_file)
words = {}
next(reader)
for row in reader:
    words_in_title = (row[1].strip().split(' '))
    for word in words_in_title:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
most_frequent_word = max(words, key=words.get)
print(most_frequent_word, words[most_frequent_word])
