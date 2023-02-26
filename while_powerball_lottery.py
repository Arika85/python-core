
import random
#Welcome note
print("---------------Power-Ball Simulator---------------")

white = int(input("How many white-balls to draw for the 5 winning numbers (Normally 69): "))
red = int(input("How many red-balls to draw for the Power-Ball (Normally 26): "))




def Powerball():
    result = []
    for i in range(5):
        number = random.randint(1,69)
        while (number in result):
            number = random.randint(1,69)
        result.append(number)
    result.sort()
    result.append(random.randint(1,26))
    return result
