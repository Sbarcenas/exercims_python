my_dict = {3: 'Pling', 5: 'Plang', 7: 'Plong'}


def convert(number):
    my_ans = ""
    for key in my_dict:
        if number % key == 0:
            my_ans = my_ans + (my_dict[key])
    if not my_ans:
        my_ans = str(number)
    return my_ans