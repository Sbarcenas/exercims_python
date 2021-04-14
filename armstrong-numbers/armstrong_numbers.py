def is_armstrong_number(number):
    check_list = list(str(number))
    sum, i = 0, 0

    for i in range(0, len(check_list)):
        sum += int(check_list[i]) ** len(check_list)

    if sum == number:
        return True

    else:
        return False