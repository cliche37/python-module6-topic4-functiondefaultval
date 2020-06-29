def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
    """Accepts name and score arguments and ensures score is within range.

    Accepts test_name, test_score, and an optional message and
    ensures the test_score argument is within a valid range.

    :param string test_name: Name of test/test taker
    :param int test_score: Test score value.
    :param string invalid_message: Optional. Invalid message warning.
    :returns test_name: test_score
    """

    while True:
        test_score_str = str(test_score)

        try:
            if test_score_str.isnumeric() and 0 <= int(test_score) <= 100:
                return test_name + ": " + str(test_score)

            else:
                raise ValueError

        except ValueError:
            test_score = (input(invalid_message))
