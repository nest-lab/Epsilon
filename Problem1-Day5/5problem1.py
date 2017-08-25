import re

file = open("Day3PMSession.txt")
text = file.read();

sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)

file.close();
for lines in sentences:
    print lines 