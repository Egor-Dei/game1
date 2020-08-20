import uuid

numbers = ['H', '7', 'b', 'm', '3', 'o', 't', 'S', 'Y', 'L', 'Q', 'J', '6', 'i', 'E', '0', 'C', 'R', 's', 'T', 'h', \
           'x', 'd', 'g', '2', '9', 'w', 'n', 'P', 'M', 'f', '1', 'N', 'l', 'c', 'W', 'A', 'K', 'a', 'U', '5', 'I', \
           'Z', 'y', 'D', 'j', 'u', 'p', 'q', 'v', 'F', 'V', 'X', 'O', 'B', 'k', 'r', 'G', 'e', 'z', '8', '4']


def generate(name):
    new_name = ""
    for i in range(len(name)):
        if name[i] not in numbers:
            continue
        index = numbers.index(name[i])
        if i % 2 == 0:
            if index + 5 >= len(numbers):
                index = index + 5 - len(numbers)
            else:
                index += 5
        else:
            if index + 7 >= len(numbers):
                index = index + 7 - len(numbers)
            else:
                index += 7
        new_name += numbers[index]
    return new_name


def new_generate(name):
    new_name = ""
    for i in range(len(name)):
        index = numbers.index(name[i])
        if i % 2 == 0:
            if index + 3 >= len(numbers):
                index = index + 3 - len(numbers)
            else:
                index += 3
        else:
            if index + 2 >= len(numbers):
                index = index + 2 - len(numbers)
            else:
                index += 2
        new_name += numbers[index]
    return new_name


def check_code(name):
    new_name = ""
    for i in range(len(name)):
        if name[i] not in numbers:
            continue
        index = numbers.index(name[i])
        if i % 2 == 0:
            if index + len(numbers) - 8 >= len(numbers):
                index -= 8
            else:
                index += len(numbers) - 8
        else:
            if index + len(numbers) - 9 >= len(numbers):
                index -= 9
            else:
                index += len(numbers) - 9
        new_name += numbers[index]
    return hex(uuid.getnode()).replace('0x', '') == new_name

