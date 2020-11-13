from times import compute_overlap_time, time_range
from pytest import raises 
'''
def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 13:30:00", "2010-01-12 13:45:00", 2, 60)
    expected = []
    assert compute_overlap_time(large, short) == expected

def overlaptest_withinterval():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",2, 0)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00", 2, 0)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:45:00'), ('2010-01-12 10:45:00', '2010-01-12 11:00:00')]
    assert compute_overlap_time(large,short) == expected

def test_time_check():
    with raises(ValueError):
        time_range("2010-01-12 12:00:00","2010-01-12 10:00:00")
'''


import pytest
import yaml


with open('fixture.yaml', 'r') as yaml_file:
    times_lists =  yaml.safe_load(yaml_file)
    
# you only need to input the values into pytest once to them use in your functions
# test_name will be a dictionary 
@pytest.mark.parametrize("test_name", times_lists)

def test_time_no_overlap(test_name):
   
    properties = list(times_lists.values())[0]
    start_time = time_range(*properties['time_range_1'])
    end_time = time_range(*properties['time_range_2'])
    expected_overlap = [(start,stop) for start,stop in properties['expected']]
    assert compute_overlap_time(start_time, end_time ) == expected_overlap


def test_negative_time_range():
   with pytest.raises(ValueError) as e:
        time_range("2010-01-12 10:00:00", "2010-01-12 09:30:00")
        assert e.match('The end of the time range has to come strictly after its start.')
# just adding a minor change in the code file 
#adding a nother minor change so i can commit
