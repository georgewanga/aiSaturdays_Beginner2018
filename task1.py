import random 

ourList = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    
ourList

# list comprehension for elemets of **ourList** that are below 5
belowFive = [item for item in ourList if item<5]
print(belowFive)