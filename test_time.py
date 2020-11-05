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
'''
def test_time_check():
    with raises(ValueError):
        time_range("2010-01-12 12:00:00","2010-01-12 10:00:00")
