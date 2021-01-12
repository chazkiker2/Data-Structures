from math import log10, floor


def is_lucky_no_comments(number):
    """Determine if a positive, even number is lucky. A number is lucky if
   the sum of the first half of its digits is equal to the sum of the
   second half of its digits."""
    half_power = floor(log10(abs(number)) + 1)
    half_power //= 2
    half_power = 10 ** half_power
    front = number // half_power
    back = number % half_power
    digit_sum = 0

    while front > 0:
        front_digit, back_digit = [x % 10 for x in [front, back]]
        front, back = [x // 10 for x in [front, back]]
        digit_sum += front_digit - back_digit
    return digit_sum == 0


# noinspection DuplicatedCode
def is_lucky(number):
    """Determine if a positive, even number is lucky. A number is lucky if
the sum of the first half of its digits is equal to the sum of the
second half of its digits."""
    # Lets break this up.
    # half_power = 10 ** (floor(log10(number) + 1) // 2)
    # Calculate the number of digits.
    half_power = floor(log10(abs(number)) + 1)
    # Divide it by two to get the size of a half. Technically since
    # there are guaranteed to be an even number of digits we don't
    # have to specify integer division, but it's best to be explicit
    # whenever possible
    half_power //= 2
    # Raise 10^(half the number of digits). This gives us a number
    # that can extract the two halves using integer division and
    # taking the modulus.
    half_power = 10 ** half_power
    # pull out the front half with integer division and the back with
    # the modulus
    front = number // half_power
    back = number % half_power
    # Keep track of all additions and subtractions
    digit_sum = 0
    # We are guaranteed to have an even number of digits in the input,
    # so we know that both sides will run out at the same time, so we
    # only have to check if one has run out. We choose the front to
    # check because we know the first digit will never be 0, but the
    # first digit of the second half may be, ie, 1001. The first half
    # is 10 and the second half is 01.
    while front > 0:
        # % 10 to extract the next digits from the two halves
        front_digit, back_digit = [x % 10 for x in [front, back]]
        # // 10 to leave only the remaining digits
        front, back = [x // 10 for x in [front, back]]
        # Add and subtract the two digits we extracted
        digit_sum += front_digit - back_digit
    # return the result of checking if all the additions and
    # subtractions canceled themselves out.
    return digit_sum == 0
