def valid_string_failure_message(valid_string, regex):
    message = 'The valid string "' + valid_string + '" failed to match '
    'against the regex: ' + str(regex)

    return message


def invalid_string_failure_message(invalid_string, regex):
    message = 'The invalid string "' + invalid_string + '" unexpectedly matched'
    ' against the regex: ' + str(regex)

    return message
