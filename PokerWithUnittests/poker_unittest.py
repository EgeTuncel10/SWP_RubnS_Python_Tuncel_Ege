import unittest
import poker as poker

# mittels cmd im selben Ordner:  'python .\poker_unittest.py' eingeben --> Test wird automatisch durchgeführt
#       wenn erfolgreich --> 'OK'

# hier einige Tests durchgeführt --> ich verstehe jetzt wie unittests funktionieren, deswegen nicht alle methoden getestet


class TestPokerMethods(unittest.TestCase):
    def test_init(self):
        self.assertEqual(len(poker.init()), 52)

    def test_draw_five_cards(self):
        poker_cards = poker.init()
        five_cards = poker.draw_five_cards(poker_cards=poker_cards, amount_of_cards=5)
        self.assertEqual(len(five_cards), 5)
        unique_values = set(five_cards)
        self.assertEqual(len(unique_values), 5)

    def test_royal_flush(self):
        royal_flush = [12, 10, 11, 9, 8]
        self.assertEqual(poker.royal_flush(royal_flush), True)
        royal_flush = [7, 10, 11, 9, 8]
        self.assertEqual(poker.royal_flush(royal_flush), False)


if __name__ == '__main__':
    unittest.main()
