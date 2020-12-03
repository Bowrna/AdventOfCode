def break_the_input(each_whole_element):
    splitted = each_whole_element.split(":")
    further_split = splitted[0].split()
    min_max = further_split[0]
    min_max_count = min_max.split("-")
    minc = int(min_max_count[0])
    maxc = int(min_max_count[1])
    char_to_check = further_split[1]
    password = splitted[1].strip()
    return minc, maxc, char_to_check, password


def find_number_of_valid(input_rule):
    number_of_valids = 0
    for rule in input_rule:
        valid = False
        min_count_pos, max_count_pos, char_to_find, password = break_the_input(rule)
        min_char = password[min_count_pos-1]
        max_char = password[max_count_pos-1]
        if min_char == char_to_find and max_char != char_to_find:
            valid = True
        elif min_char != char_to_find and max_char == char_to_find:
            valid = True
        else:
            valid = False
        if valid:
            number_of_valids = number_of_valids+1
    return number_of_valids


def main():
    input_content = open("input/day2.txt", "r")
    sample_input = input_content.readlines()
    output_valids = find_number_of_valid(sample_input)
    print(output_valids)


if __name__ == "__main__":
    main()