
def secret_string(message):
    return message.startswith('secret')


def any_starts_with_secret(test_strings):
    for test_string in test_strings:
        if test_string.startswith('secret'):
            return True
    return False


def is_prime_number(test_num):
    for i in range(2, test_num):
        if test_num % i == 0:
            return False
    return True
