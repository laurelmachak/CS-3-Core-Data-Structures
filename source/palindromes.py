#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # formated_text = text.lower()
    # formated_text = text.strip()
    # formated_text = text.replace(" ", "")
    #dont use thise ^^^
    pass
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests

def clean_text(text):
    format_text = text.strip()
    format_text = format_text.replace(",","")
    format_text = format_text.replace("!","")
    format_text = format_text.replace(".","")
    format_text = format_text.replace(" ", "")
    format_text = format_text.lower()
    return format_text



def is_palindrome_recursive(text, left=0, right=-1):
    # TODO: implement the is_palindrome function recursively here
    cleaned_text = clean_text(text)
    # left = 0
    # right = -1
    print(left)
    print(right)

    if (left <= right):
        return True

    elif (cleaned_text[left] != cleaned_text[right]):
        return False

    left = left + 1
    right = right - 1

    return(is_palindrome_recursive(cleaned_text, left, right))

    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
