print ("A Hashtag system")
input_by_users = raw_input("Enter any sentence or word: ")

words_from_input = input_by_users.split()
#print input_by_users

words_with_hashtags = []
for i in xrange(len(words_from_input)):
    if "#" in words_from_input[i]:
        words_with_hashtags.append(words_from_input[i])

if len(words_with_hashtags) == 0:
    print ("No Hashtags")
else:
    for j in words_with_hashtags:
        print j

