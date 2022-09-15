def checkIfStringIsHexCode(string):
    new_str = string[1::]
    length_of_string = len(new_str)
    digit = [str(x) for x in range(10)]
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']
    digit.extend(alphabet)
    result_list = []
    # print(digit)
    # print(str[0])
    if string[0] != '#':
        return False
    elif length_of_string != 6:
        return False
    else:
        for i in new_str:
            if i in digit:
                # print(i)
                result_list.append(True)
            else:
                # print(i)
                result_list.append(False)
    # print(result_list)

    if False in result_list:
        return False
    else:
        return True

print(checkIfStringIsHexCode("#CD5C5C")) # True
print(checkIfStringIsHexCode("#EAECEE")) # True
print(checkIfStringIsHexCode("#eaecee")) # True
print(checkIfStringIsHexCode("#CD5C58C")) # False
print(checkIfStringIsHexCode("#CD5C5Z")) # False
print(checkIfStringIsHexCode("#CD5C&C")) # False
print(checkIfStringIsHexCode("CD5C5C")) # False




