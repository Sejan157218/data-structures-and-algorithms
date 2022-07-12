def linear_search(num_list,num_find):
    for index,element in enumerate(num_list):
        if element==num_find:
            return index
    return -1;

def Binary_search(num_list,num_find):
    left_index=0;
    right_index=len(num_list)-1;
    mid_index=0;

    while left_index <= right_index:
        mid_index=(left_index + right_index) // 2;
        mid_num = num_list[mid_index]

        if mid_num==num_find:
            return mid_index;
        

        if mid_num < num_find:
            left_index = mid_index + 1;
        else:
            right_index = mid_index - 1;
    return -1;

def Binary_search_recursive(num_list,find_num,left_index,right_index):
    if right_index < left_index:
        return -1;
    
    mid_index=(left_index + right_index) // 2;

    if mid_index >= len(num_list) or mid_index <0:
        return -1;


    mid_num=num_list[mid_index]

    if mid_num == find_num:
        return mid_index;
    
    if mid_num < find_num:
        left_index = mid_index +1;
    else:
        right_index = mid_index -1;

    return Binary_search_recursive(num_list,find_num,left_index,right_index)



if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 55

    index = Binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")