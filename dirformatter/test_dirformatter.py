#!/usr/bin/env python

import unittest
import dirformatter
from datetime import datetime

class DirFormatterTests(unittest.TestCase):
    """Unit tests for dirformatter"""

    def setUp(self):
        date_str = "2013-07-03 12:45:45"
        self.tstamp = datetime.strptime(date_str,
                                               '%Y-%m-%d %H:%M:%S')

    def test_DefaultFormat(self):
        self.assertEqual(
            dirformatter.createdirpath('yyyy/mmmm/yyyy_mm_dd', self.tstamp),
                         '2013/July/2013_07_03')



if __name__ == '__main__':
    unittest.main()
