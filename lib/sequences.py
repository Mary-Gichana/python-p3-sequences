def print_fibonacci(length):
    if length <= 0:
        print([])  
        return
    elif length == 1:
        print([0])  
        return

    
    my_list = [0, 1]
    for _ in range(2, length):
        my_list.append(my_list[-1] + my_list[-2])
    print(my_list)  
