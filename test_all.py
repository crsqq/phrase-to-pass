#!/usr/bin/env python3
# vim: set fileencoding=utf-8:
import unittest
from PhraseToPass import all_in_one


class all_in_one_TestCase(unittest.TestCase):
    def test_phrase_one(self):
        result = all_in_one("I can't see the wood for the trees!")
        assert result == "ItEeDrEs!81"


if __name__ == '__main__':
    unittest.main()
