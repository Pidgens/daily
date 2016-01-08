
def plant(people, fruits):
    week = 1
    listFruits = []
    for fruit in range(0, fruits):
        listFruits.append(0)
    total_fruit = 0
    while (total_fruit < people):
        # add one to all fruits
        listFruits = incrementOne(listFruits)
        # increase number of plants
        total_fruit = addList(listFruits)
        for i in range(0, total_fruit):
            listFruits.append(0)
        # print listFruits
        week += 1
        # print listFruits
    print total_fruit
    return week


def addList(listFruits):
    numberFruits = 0
    for fruit in listFruits:
        numberFruits += fruit
    # print 'numberofFruits' + str(numberFruits)
    return numberFruits

def incrementOne(listFruits):
    new_list = [x+1 for x in listFruits]
    # print new_list
    return new_list

print plant(15,1)
print plant(200,15)
print plant(50000,1)
print plant(150000,250)
