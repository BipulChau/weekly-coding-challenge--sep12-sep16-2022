def checkIfStringIsHexCode(str):
    new_str = str[1::]
    length_of_string = len(new_str)
    digit = [x for x in range(0, 10)]
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']
    digit.extend(alphabet)
    # print(digit)
    # print(str[0])
    if str[0] != '#' and len != 6:
        return False
    else:
        for i in new_str:
            if i not in digit:
                return False
            else:
                return True


print(checkIfStringIsHexCode("#CD5C5C"))
print(checkIfStringIsHexCode("CD5C5C"))
print(checkIfStringIsHexCode("#CD5C&C"))