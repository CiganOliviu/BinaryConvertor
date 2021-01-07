def convert_list_to_number(number_as_list):

    return int("".join(map(str, number_as_list)))


def convert_decimal_to_binary(number):

    result = []

    while number > 0:
        rest = number % 2
        result.append(rest)
        number //= 2

    result.reverse()

    return result


def convert_binary_to_decimal(binary_number):

    binary_number_as_list = [int(item) for item in str(binary_number)]
    binary_number_as_list.reverse()

    result = 0

    for index in range(len(binary_number_as_list)):
        if binary_number_as_list[index] == 1:
            result += (pow(2, index))

    return result


def test_convert_decimal_to_binary_():

    assert convert_list_to_number(convert_decimal_to_binary(1234)) == 10011010010
    assert convert_list_to_number(convert_decimal_to_binary(4321)) == 1000011100001
    assert convert_list_to_number(convert_decimal_to_binary(5)) == 101


def test_convert_binary_to_decimal_():

    assert (convert_binary_to_decimal(10011010010)) == 1234
    assert (convert_binary_to_decimal(1000011100001)) == 4321
    assert (convert_binary_to_decimal(101)) == 5


if __name__ == '__main__':
    test_convert_decimal_to_binary_()
    test_convert_binary_to_decimal_()
