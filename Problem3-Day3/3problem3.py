words = open ("words.txt", "r") 

v_words = []
for j in words:
    v_words.append(j.strip())

user_input = str(raw_input("Enter any scrambled word with no spaces: "))
l_input = int(raw_input("Enter the length of english combination words you want from your scrambled words: "))

subs = []
for i, c in enumerate(user_input):
    for j in range(i, len(user_input)):
        tmpstr = ''
        for k in range(i, j+1):
            tmpstr += user_input[k]
        subs.append(str(tmpstr))

needed_words = []
for x in subs:
    if len(x) == l_input:
        for y in v_words:
            if x == y:
                needed_words.append(x)
print needed_words