# Sol 1:

import random

#Welcome note
print("Welcome to the coin Toss App")
print("\nI will flip a coin a set number of times.")

#Flipping count
count = int(input("How many times would you like me to flip the coin: "))
result = input("Would you like to see the result of each flip (y/n): ").lower().strip()


HEADS = 0
TAILS = 0

for i in range(count):
    # print(*random.choices(['HEADS', 'TAILS'], k=count), sep='\n')
    if random.randint(0,1) == 1 and result == 'y':
        HEADS += 1
        print('HEADS')
    else:
        TAILS += 1
        print('TAILS')

    if HEADS == TAILS:
        print(f"At {i+1} flips, the number of heads and tails were equal at {int((i+1)/2)} each")
        # print(f"At {i+1} flips, the number of heads and tails were equal at {HEADS} each")
        # print(f"At {i+1} flips, the number of heads and tails were equal at {TAILS} each")
print(f"\nResults For Flipping A Coin {count} Times:\n")
print(f"Side\t\tCount\t\tPercentage")
print(f"Heads\t\t{HEADS}/{count}\t\t{(round((HEADS*100)/count, 2))}%")
print(f"Tails\t\t{TAILS}/{count}\t\t{(round((TAILS*100)/count, 2))}%")


# Solution 2:

# # To find Count of heads and tails
import random

count = int(input("How many times would you like me to flip the coin: "))
samples = [ random.randint(1, 2) for i in range(count) ]
heads = samples.count(1)
tails = samples.count(2)

for s in samples:
    msg = 'Heads' if s==1 else 'Tails'
    print(msg)

print("Heads count=%d, Tails count=%d" % (heads, tails))