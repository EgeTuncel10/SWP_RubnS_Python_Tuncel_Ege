import random


def lottery_drawing(fromNumber, toNumber, numbersToTake):
    lotto_numbers = []
    for i in range(fromNumber, toNumber):
        lotto_numbers.append(i)

    lotto_numbers_pulled = []
    for i in range(numbersToTake):
        random_number = random.choice(lotto_numbers)
        lotto_numbers_pulled.append(random_number)
        lotto_numbers.remove(random_number)

    print(lotto_numbers_pulled)


def lottery_drawing_better():
    lotto_numbers = []
    for i in range(1, 46):
        lotto_numbers.append(i)

    for i in range(6):
        endrange = 44
        random_number = random.randrange(0, endrange)
        lotto_numbers.append(lotto_numbers.pop(lotto_numbers.index(random_number)))
        endrange -= 1

    print(lotto_numbers[-6:])
    print(lotto_numbers)

if __name__ == '__main__':
    #lottery_drawing(1, 47, 6)
    lottery_drawing_better()
