# put your code here.
from sys import argv
script, filename = argv
dict_count = {}
files = open(filename)
for line in files:
    # print line
    lines = line.rstrip().split(" ")
    # print lines
    #words = lines.split(" ")
    for word in lines:
        word = word.lower()
        # z = word.isalpha
        # print z
        if word[-1].isalpha() is False:
            word = word[0:-1]
        # else:
        #     word = word
        if word not in dict_count:
            dict_count[word] = 1
        else:
            dict_count[word] = dict_count[word] + 1

for key, value in dict_count.items():
    print key, value
