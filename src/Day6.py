def break_the_string(input_answer):
    # return input_answer.replace('\n','')
    return input_answer.split('\n')


def split(word):
    return list(word)


def get_grand_count(input_answers):
    grand_count = 0
    for answer in input_answers:
        broken_answer = break_the_string(answer)
        new_list = []
        for ans in broken_answer:
            new_list.append(split(ans))
        # print(new_list)
        result = set(new_list[0]).intersection(*new_list)

        # set_answer = ''.join(set(broken_answer))
        # count = len(set_answer)
        grand_count = grand_count + len(result)

    return grand_count


def main():
    # input_content = open("input/day3.txt", "r")
    with open("input/day6.txt") as input_content:
        sample_input = input_content.read().split("\n\n")
        # print('Length:', len(sample_input))
        # print('Input', sample_input[0].replace('\n',''))
        count = get_grand_count(sample_input)
        print('Count:',count)


if __name__ == '__main__':
    main()
