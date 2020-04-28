import sys

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def convert(s):
    number = ''
    for token in s:
        number += DIGIT_MAP[token]
    x = int(number)
    return x


#print(convert({'two', 'three', 'nine', 'zero'}))
#print(convert("two three nine zero".split()))


def convert_with_exception(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
            print(f"conversion of {token} successful")
        x = int(number)
    except (KeyError, TypeError):
        x = -1
        print(f"conversion failed")
    return x


#print(convert_with_exception("two three five seventeen".split()))
#print(convert_with_exception(450))


def convert_with_exception_with_empty_except(s):
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
            print(f"conversion of {token} successful")
        x = int(number)
    except (KeyError, TypeError):
        pass
    return x


#print(convert_with_exception_with_empty_except("two three five seventeen".split()))
#print(convert_with_exception_with_empty_except(450))

def convert_with_exception_raise_exception(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
            print(f"conversion of {token} successful")
        x = int(number)
    except (KeyError, TypeError) as e:
        print(f"conversion error {e!r}", file=sys.stderr)
        raise
    return x


print(convert_with_exception_raise_exception("two three five seventeen".split()))
print(convert_with_exception_raise_exception(450))
