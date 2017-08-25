import random
 random_items = [random.randint(-50, 100) for c in range(32)]
 
# &gt; = greater than
# &lt; = lesser than

def sort(items):
        for i in range(1, len(items)):
                j = i
                while j &gt; 0 and items[j] &lt; items[j-1]:
                        items[j], items[j-1] = items[j-1], items[j]
                        j -= 1

print 'Before: ', random_items
sort(random_items)
print 'After : ', random_items