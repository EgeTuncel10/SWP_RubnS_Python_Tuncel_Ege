from models.int_sequence_iter import IntegerSequenceIterator
import random


def main():
    linked_list = IntegerSequenceIterator([])

    for _ in range(10):
        linked_list.append_to_sequence(random.randint(1, 100))

    print("Length of the linked list:", linked_list.__len__())

    print("\nUsing iterator protocol:")
    for data in linked_list:
        print(data)
