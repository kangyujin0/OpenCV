import random

groups = [2,3,4,12,19]

random.shuffle(groups)

for i in range(0,5):
    print(str(i+1)+" 순서:"+str(groups[i]))
