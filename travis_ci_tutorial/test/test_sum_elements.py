#!/usr/bin/env python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.tutorial import sum_elements

def test_sum1():
    assert 10 == sum_elements([1,2,3,4])