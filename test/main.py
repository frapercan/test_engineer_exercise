import itertools
import pytest
import yaml

from testlib import SquaresAdder

def read_test_params():
    with open('./test/parameters.yaml', 'r') as file:
        params = yaml.safe_load(file)
    return params

test_params = read_test_params()

def test_squares_adder_positive():
    for params in test_params['positive']:
        start = params['start']
        end = params['end']
        expected_sum = params['expected_sum']
        result = SquaresAdder.get_sum(start, end)
        assert result == expected_sum

def test_squares_adder_negative():
    for params in test_params['negative']:
        start = params['start']
        end = params['end']
        expected_sum = params['expected_sum']
        try:
            result = SquaresAdder.get_sum(start, end)
            assert result == expected_sum
        except OverflowError:
            pytest.fail("OverflowError occurred.")

def test_squares_adder_inverse():
    for params in test_params['positive']:
        start = params['start']
        end = params['end']
        expected_sum = params['expected_sum']
        result = SquaresAdder.get_sum(start, end)
        assert result == expected_sum


#
def test_squares_adder_auto():
    params = test_params['auto']
    interval = range(params['start'], params['end'])
    combinations = list(itertools.combinations(interval, 2))
    for combination in combinations:
        start,end = combination
        result = SquaresAdder.get_sum(start, end)
        expected_sum = sum(value*value for value in range(start,end+1))
        assert result == expected_sum


