import math
from functools import reduce


def traverse_direction(input_rows, right, down, current_location_row1):
    """
    Here input rows is passed as list of string.
    The number of string inside list is determined by the downsize.
    If we have to go down 1 unit, then row size of 2 is sufficient
    Return if the point is tree or open, and the current location for next traversal
    """
    is_tree = False
    land_to_traverse = input_rows[1]
    current_location_row1 = current_location_row1 + right
    # print('Current location to traverse:',current_location_row1)
    land_size = len(land_to_traverse)
    # print('Original land size:', land_size)
    if current_location_row1 >= land_size:
        # print('I am going to multiply')
        number_to_multiply = math.ceil(current_location_row1/land_size)
        if current_location_row1%land_size == 0:
            number_to_multiply += 1
        # print('I am multiplied by:', number_to_multiply)
        land_to_traverse = number_to_multiply*land_to_traverse
    # print(land_to_traverse)
    # print(len(land_to_traverse))
    find_element = land_to_traverse[current_location_row1]
    if find_element == '#':
        is_tree = True
    return is_tree, current_location_row1


def pass_the_land_coverage(sample_input):
    # print(type(sample_input))
    # Slice the land coverage depending on the slope down size
    directions = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    si = len(sample_input)
    found_trees = []
    for direction in directions:
        # print(direction)
        right = direction[0]
        down = direction[1]

        zipped_input = [[sample_input[i], sample_input[i + down]] for i in range(0, si - down, down)]
        # zipped_input = list(zip(sample_input, sample_input[down:]))
        previous_location = 0
        no_of_trees = 0
        # looping = 0
        for small_land in zipped_input:
            # print(small_land)
            # print(len(small_land[0]))
            # looping+=1
            # print('Loop:',looping)
            found_tree, current_location = traverse_direction(small_land, right, down, previous_location)
            if found_tree:
                no_of_trees += 1
            previous_location = current_location
        print('No of trees till now:', no_of_trees)
        found_trees.append(no_of_trees)
    return found_trees


def main():
    # input_content = open("input/day3.txt", "r")
    with open("input/day3.txt") as input_content:
        sample_input = input_content.read().splitlines()
    trees_found = pass_the_land_coverage(sample_input)
    print(trees_found)
    multiply_trees = reduce(lambda x, y: x*y,trees_found)
    print(multiply_trees)


if __name__ == '__main__':
    main()
