import time

FORMAT_NUMBER = "{number:0>{len_string}}"

def karatsuba(first_number, second_number):
    if first_number < 10 or second_number < 10:
        return first_number * second_number
    max_len = max(len(str(first_number)), len(str(second_number)))
    number_len = max_len if max_len % 2 == 0 else max_len + 1
    # making the two numbers strings here
    str_x = FORMAT_NUMBER.format(number=first_number, len_string=number_len)
    str_y = FORMAT_NUMBER.format(number=second_number, len_string=number_len)

    # finding the mid point for each number here
    n = number_len
    n_2 = int(n / 2)

    # higher bits of each number
    x_h = int(str_x[:n_2])
    y_h = int(str_y[:n_2])

    # lower bits for each number here
    x_l = int(str_x[n_2:])
    y_l = int(str_y[n_2:])

    a = karatsuba(x_h, y_h)
    d = karatsuba(x_l, y_l)
    e = karatsuba(x_h + x_l, y_h + y_l) - a - d

    if e in results:
        results[e] += 1
    else:
        results[e] = 1

    return a * 10 ** len(str_x) + e * 10 ** (len(str_x) // 2) + d

global results
if __name__ == '__main__':
    while True:
        try:
            first_input_number = int(input("Введите первое число:  "))
            second_input_number = int(input("Введите второе число:  "))
            start_time = time.time()
            result = karatsuba(first_input_number, second_input_number)
            print("karatsuba: ", result, "\ttime:", time.time() - start_time)
            print("normal: ", first_input_number * second_input_number, "\ttime:", time.time() - start_time)

        except:
            print("\033[1m\033[31mПожалуйста, введите еще раз\033[0m")
