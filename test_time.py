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


with open('fixture.yaml') as yaml_file:
    times_lists =  yaml.safe_load(yaml_file)
    
print(times_lists['time_points']['expected'])


@pytest.mark.parametrize("starttime, endtime, expected",
 [(times_lists['time_points']['start_time'], times_lists['time_points']['end_time'], [(times_lists['time_points']['expected'][0], times_lists['time_points']['expected'][1])]
 )]
 )
def test_range(starttime, endtime, expected):
    assert time_range(starttime, endtime) == expected

@pytest.mark.parametrize("range1, range2, expected",
[(time_range(times_lists['no_overlap']['time_range_1'][0], times_lists['no_overlap']['time_range_1'][1]),
  time_range(times_lists['no_overlap']['time_range_2'][0], times_lists['no_overlap']['time_range_2'][1],times_lists['no_overlap']['time_range_2'][2],times_lists['no_overlap']['time_range_2'][3]),
  [(times_lists['no_overlap']['expected'][0],times_lists['no_overlap']['expected'][1]), (times_lists['no_overlap']['expected'][2], times_lists['no_overlap']['expected'][3])]
  
)]

)

def test_overlap(range1, range2, expected):
    assert compute_overlap_time(range1,range2) == expected
