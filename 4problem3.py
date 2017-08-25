corpus = open("corpus.txt", "r")
search_word = raw_input("Enter any word you want to search in the corpus file")

count = 0

def find_str (string, sub_string):
    index = 0
    length = len(sub_string)
    for j in range(len(string)):
        if is_next_sub(string, sub_string, j):
            return j        
    return "-1"

def is_next_sub(string, sub_string, index):
    for i in range(len(sub_string)):
        if sub_string[i] != string[index + i]:
            return False
    return True

for line in corpus:
    s = line.strip()
    s_in_list = line.split()
    if search_word in sentences:
        count = count + 1

        print "Typed word is found in", s, "at position", find_str(s, search_word)

print "found your words", count, "times"