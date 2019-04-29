from rest_framework.status import HTTP_200_OK


def valid_string_failure_message(valid_string, regex):
    """
    Creates a message for failed tests of valid strings.
    :param valid_string:
    :type valid_string: str
    :param regex:
    :type regex: re
    :return:
    :rtype: str
    """
    message = 'The valid string "' + valid_string + '" failed to match '
    'against the regex: ' + str(regex)

    return message


def invalid_string_failure_message(invalid_string, regex):
    """
    Creates a message for failed tests of invalid strings.
    :param invalid_string:
    :type invalid_string: str
    :param regex:
    :type regex: re
    :return:
    :rtype: str
    """
    message = 'The invalid string "' + invalid_string + '" unexpectedly matched'
    ' against the regex: ' + str(regex)

    return message


def unexpected_status_code_message(actual, expected=HTTP_200_OK):
    """
    Creates a message for unexpected status codes in responses.
    :param expected:
    :type expected: int
    :param actual:
    :type actual: int
    :return:
    :rtype: str
    """
    expected = str(expected)
    actual = str(actual)
    message = 'Expected response code ' + expected + ', but got ' + actual

    return message
