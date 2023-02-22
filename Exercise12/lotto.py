import random

# using .randint...

lotto_num = []

while len(lotto_num) < 6:
    rand_num = random.randint(1, 50)
    if rand_num not in lotto_num:
        lotto_num.append(rand_num)

print(lotto_num)


# using .randint but storing the numbers in a set
# we no longer need the if statement here as the set will not store duplicates

lotto_num = set()

while len(lotto_num) < 6:
    rand_num = random.randint(1, 50)
    lotto_num.add(rand_num)

print(lotto_num)


# using random.sample...

pool=list(range(1, 51))
lotto=random.sample(pool, k=6)
print(lotto)