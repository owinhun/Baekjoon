num = input()

while num != '0':
    num_list = list(num)
    num_list.reverse()
    reverse = ''.join(num_list)

    if num == reverse:
        print('yes')
    else:
        print('no')
    num = input()