import random

weights = [0.22, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13]

random_num = random.choices([1,2,3,4,5,6,7], weights)[0]

print(random_num)