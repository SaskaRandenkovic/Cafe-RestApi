import unittest
from flask_testing import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath('../..'))

from app.caffe.tests import *

if __name__ == '__main__':
    unittest.main()