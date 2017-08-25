from random import randint

array=[]

for i in range(10):
    array.append(randint(1,10))

print(array)

for i in range(len(array)):
    if i == len(array)-1:
        break
    if (array[i] >= array[i-1]) and (array[i]>= array[i+1]):
      print array[i], "passed Condition One"

    elif (array.index(array[i]) == 0) and (array[i] >= array[1]):
        print array[i], "passed Condition Two"

    elif (array.index(array[i]) == len(array)-1) and (array[i] >= array[i-1]):
        print array[i], "passed Condition Three"