from django.test import SimpleTestCase


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = add(5, 6)

        self.assert_(res, 11)

    def test_subtract_numbers(self):
        res = subtract(20,15)

        self.assert_(res, 5)