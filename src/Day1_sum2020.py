import pdb
from itertools import combinations
from functools import reduce
import operator


def find_subset(input_list, size):
    return list(combinations(input_list, size))


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def find_the_three_numbers_sum2020(input_content):
    size = 3
    input_content_modified = [int(i) for i in input_content]
    possible_list = find_subset(input_content_modified, size)
    product = 0
    for possibles in possible_list:
        #print(possibles)
        #print(type(possibles))
        out = sum(list(possibles))
        if out == 2020:
            print(possibles)
            product = prod(possibles)
            print(product)
            break
    return product




# def find_the_three_numbers_sum2020(input_content):
#     content_size = len(input_content)
#     content_pointer = 0
#     output = 0
#     matched = False
#     for content in input_content:
#         # pdb.set_trace()
#         # print(content)
#         int_content = int(content)
#         content_pointer_1 = content_pointer + 1
#         content_pointer_2 = content_pointer_1 + 1
#         content_pointer = content_pointer + 1
#         if content_pointer_1 < content_size and content_pointer_2 < content_size:
#             int_content_1 = int(input_content[content_pointer_1])
#             input1 = int_content + int_content_1
#             new_index = content_pointer_2
#             if input1 < 2020:
#                 print(int_content, int_content_1, input1, new_index)
#                 while new_index < content_size:
#                     input1 = int_content
#                     input2 = int(input_content[new_index])
#                     if input1+input2 == 2020:
#                         matched = True
#                         print(int_content)
#                         print(int_content_1)
#                         print(input2)
#                         output = int_content * int_content_1 * input2
#                         break
#                     else:
#                         new_index = new_index + 1
#         if matched:
#             break
#         else:
#             continue
#     return output


def find_the_two_numbers_sum2020(input_content):
    content_size = len(input_content)
    content_pointer = 0
    output = 0
    matched = False
    for content in input_content:
        # pdb.set_trace()
        # print(content)
        int_content = int(content)
        content_pointer = content_pointer + 1
        new_index = content_pointer
        while new_index < content_size:
            input1 = int_content
            input2 = int(input_content[new_index])
            if input1+input2 == 2020:
                matched = True
                print(input1)
                print(input2)
                output = input1 * input2
                break
            else:
                new_index = new_index + 1
        if matched:
            break
        else:
            continue
    return output


def main():
    input_content = open("input/day1.txt", "r")
    sample_input = input_content.readlines()
    output = find_the_two_numbers_sum2020(sample_input)
    output1 = find_the_three_numbers_sum2020(sample_input)
    print(output)
    print(output1)
    # print(sample_input[0])


if __name__ == "__main__":
    main()
