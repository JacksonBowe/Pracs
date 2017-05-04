import random

num_picks = input('How many quick picks? ')

#quick_picks = []
for i in range(0, int(num_picks)):
    quick_picks = []
    j = 0
    quick_picks.append(random.randint(1, 45))
    while j < 5:
        value = (random.randint(1, 45))
        if not value in quick_picks:
            quick_picks.append(value)
            j += 1
    quick_picks.sort()

    print(quick_picks)