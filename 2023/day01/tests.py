"Implements basic testing for the main function."
from typing import List
from main import get_calibration_value, get_calibration_items_sum


def test_calibration_value(test_input, expected_output) -> bool:
    """
    Test the calibration value obtained from the function `get_calibration_value`.

    Parameters:
    - test_input: The input value for the calibration function.
    - expected_output: The expected output for the given value.

    Returns:
    - bool: True if the test passes, False otherwise.
    """

    result = get_calibration_value(test_input, True)
    try:
        assert result == expected_output
        return True
    except AssertionError:
        print(
            f"""
(Failed - get_calibration_value) 
{test_input} result was {result} ({type(result).__name__}) 
[Expected: {expected_output} ({type(expected_output).__name__})]\n
            """)
        return False


def batch_test_calibration_value(test_inputs: List, expected_outputs: List) -> int:
    """
    Batch test the calibration function for a list of inputs.

    Parameters:
    - test_inputs: List of input values for the function.
    - expected_outputs: List of expected outputs after the calibration function.

    Returns:
    - int: Successful tests count
    """

    if len(test_inputs) != len(expected_outputs):
        raise ValueError("Both lists must have the same length.")

    successful_tests_count = 0

    for index, value in enumerate(test_inputs):
        test_result = test_calibration_value(value, expected_outputs[index])

        if test_result:
            successful_tests_count += 1

    return successful_tests_count


def test_get_calibration_items_sum(items, expected_output):
    """
    Test the result of the sum of calibration items obtained from `get_calibration_items_sum`.

    Parameters:
    - items: List of items for the function.
    - expected_output: The expected sum of calibration items.

    Returns:
    - bool: True if the test passes, False otherwise.
    """

    try:
        result = get_calibration_items_sum(items, True)
        assert result == expected_output
        return True
    except AssertionError:
        print(
            f"""
(Failed - test_get_calibration_items_sum) 
result was {result} 
[Expected: {expected_output}]\n
            """)
        return False


if __name__ == "__main__":

    # Inputs and expected outputs for the tests
    CALIBRATION_ITEMS_INPUT = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four",
                               "4nineeightseven2", "zoneight234", "7pqrstsixteen", "1abc2",
                               "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet", "thereisnodigit",
                               17]
    CALIBRATION_ITEMS_EXPECTED_OUTPUT = [
        29, 83, 13, 24, 42, 14, 76, 12, 38, 15, 77, None, 17]

    CALIBRATION_SUM_INPUT = ["two1nine", "eightwothree", "abcone2threexyz",
                             "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
    CALIBRATION_SUM_EXPECTED_OUTPUT = 281

    # Running the tests
    CALIBRATION_ITEMS_TEST_RESULT_COUNT = batch_test_calibration_value(
        CALIBRATION_ITEMS_INPUT, CALIBRATION_ITEMS_EXPECTED_OUTPUT)
    CALIBRATION_SUM_TEST_RESULT = test_get_calibration_items_sum(
        CALIBRATION_SUM_INPUT, CALIBRATION_SUM_EXPECTED_OUTPUT)

    # Get the total tests count and the count of successful ones
    PASSED_TESTS_COUNT = CALIBRATION_ITEMS_TEST_RESULT_COUNT + \
        int(CALIBRATION_SUM_TEST_RESULT)
    TOTAL_TESTS_COUNT = len(CALIBRATION_ITEMS_INPUT) + 1

    print(f"\n{PASSED_TESTS_COUNT} / {TOTAL_TESTS_COUNT} tests passed successfully!")
