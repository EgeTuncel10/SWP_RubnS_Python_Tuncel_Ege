import random
import json

statistic = {}
#numberOne = 0 ... nur zur Kontrolle

def lottery_drawing():
    lotto_numbers = []
    for i in range(1, 46):
        lotto_numbers.append(i)

    for i in range(6):
        endrange = 44
        random_number = random.randrange(1, endrange)
        lotto_numbers.append(lotto_numbers.pop(lotto_numbers.index(random_number)))
        endrange -= 1

    #if 1 in lotto_numbers[-6:]:
        #global numberOne
        #numberOne += 1

    return lotto_numbers[-6:]


def statistics(lotto_numbers_pulled):
    for i in lotto_numbers_pulled:
        if statistic['Number: %d' % i][9].isdigit():
            previous_number = (statistic['Number: %d' % i][7]) + (statistic['Number: %d' % i][8]) + (statistic['Number: %d' % i][9])
        elif statistic['Number: %d' % i][8].isdigit():
            previous_number = (statistic['Number: %d' % i][7]) + (statistic['Number: %d' % i][8])
        else:
            previous_number = int(statistic['Number: %d' % i][7])

        statistic['Number: %d' % i] = "pulled %d time(s)" % (int(previous_number)+1)


def init_statistics():
    for i in range(1, 46):
        statistic['Number: %d' % i] = "pulled %d time(s)" % 0


if __name__ == '__main__':
    init_statistics()
    for i in range(999):
        statistics(lottery_drawing())

    print(json.dumps(statistic, indent=4))
    #print('\n%d' % numberOne)
