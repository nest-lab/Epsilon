def letterproblem(letter, magazine):
    texts = []
    for t in magazine:
        if t in letter:
            texts.append(t)
    if len(texts) < len(letter):
        return False
    else:
        return True
            

L = open("letter.txt", "r") 
M = open("magazine.txt", "r")

letter = []
magazine = []

for i in L:
    x = i.split()
    for l in x:
        letter.append(l)
for j in M:
    y = j.split()
    for m in y:
        magazine.append(m)

print letterproblem(letter, magazine)