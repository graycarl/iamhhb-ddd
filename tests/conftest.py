import os
import sys

home = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, home)

os.environ['IAMHHB_LOCAL_CONFIG'] = 'configs/testing.py'
