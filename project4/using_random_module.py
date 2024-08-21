import random
random_integer = random.randint(8,18)
print(random_integer)
print(random.randint(1,8))
print(random.randrange(99,1,-1))
#my_favourite_number = 80085
random_number_0_to_1 = random.random() #generates a random floating no. between 0 to 1
print(random_number_0_to_1 * 10) # changes range from 0 to 1 to 1 to 10

random_heads_or_tails = random.randint(0,1)
print("Heads") if random_heads_or_tails == 1 else print("Tails")

l1= ["charles", "victor", "thomas", "bruce", "anthony"]
random.shuffle(l1)
print(l1[0])
