def convert_list_to_number(number_as_list):

    return int("".join(map(str, number_as_list)))


def convert_decimal_to_binary(number):

    result = []

    while number > 0:
        rest = number % 2
        result.append(rest)
        number //= 2

    result.reverse()

    return convert_list_to_number(result)


def test_convert_decimal_to_binary_():

    assert convert_decimal_to_binary(1234) == 10011010010
    assert convert_decimal_to_binary(4321) == 1000011100001
    assert convert_decimal_to_binary(5) == 101


if __name__ == '__main__':
    test_convert_decimal_to_binary_()
