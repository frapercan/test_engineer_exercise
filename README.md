# Squares Adder

This code contains tests for the SquaresAdder class, which calculates the sum of squared numbers within a given interval.

## Setup

1. Install the required dependencies by running `pip install -r requirements.txt`.

## Test Parameters

The test parameters are defined in the `parameters.yaml` file located in the `test` directory. You can modify this file to customize the test cases.

## Running Tests

To run the tests, execute the following command:

```shell
pytest
```


# Test Cases

The code includes the following test cases:
## Positive Test
The test_squares_adder_positive() test case verifies that the SquaresAdder class correctly calculates the sum of squared numbers for positive intervals.
## Negative Test
The test_squares_adder_negative() test case verifies that the SquaresAdder class handles negative intervals properly. It asserts that an OverflowError is not raised during the calculation.
## Inverse Test
The test_squares_adder_inverse() test case verifies the SquaresAdder class handles the case where start is greater than end.
## Auto Test
The test_squares_adder_auto() test case generates pairwise combinations of values within the given interval and checks that the calculated sum matches the expected sum. Including start is greater than end cases.

# Report

## The given interval is not calculated inclusively.
The behaviour is not consistent with the programme description.
## Negative values are not handled.
Fix or handle.
```
Failed: OverflowError occurred.
```

## Wrong behaviour during the power of sums for big values.
It seems like it is working under Half-precision floating-point format.

Cases:

| Start | End | Result | Expected |
|-------|-----|--------|----------|
| 5     | 59  |  1163 |  66699  |
| 8     | 76  |  12238 |  143310  |
| 9     | 90  |  42153 |  238761  |

