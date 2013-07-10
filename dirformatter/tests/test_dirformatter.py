

import unittest
import sys
from datetime import datetime
import dirformatter

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

    def test_customFormat_1(self):
        self.assertEqual(dirformatter.createdirpath(
            'yyyy/yyyy_mm_dd', self.tstamp), '2013/2013_07_03')

    def test_customFormat_2(self):
        self.assertEqual(dirformatter.createdirpath(
            'yyyymmdd', self.tstamp), '20130703')

    def test_customFormat_3(self):
        self.assertEqual(dirformatter.createdirpath(
            'MyPics/yyyy/yyyy_mm_dd', self.tstamp,
            '/Users/shireenrao/Pictures'),
            '/Users/shireenrao/Pictures/MyPics/2013/2013_07_03')

    def test_customFormat_4(self):
        self.assertEqual(dirformatter.createdirpath(
            'yyyymmdd', self.tstamp,
            '/Users/shireenrao/Pictures'),
            '/Users/shireenrao/Pictures/20130703')

    def test_customFormat_5(self):
        self.assertEqual(dirformatter.createdirpath(
            'yyyymmdd', self.tstamp),
            '20130703')

    def test_customFormat_6(self):
        self.assertEqual(dirformatter.createdirpath(
            'yyyy\\mm\\dd', self.tstamp),
            '2013/07/03')
if __name__ == '__main__':
    unittest.main()
