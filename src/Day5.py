def find_missing(lst):
    first_seatid = lst[0]
    # total_seats = len(lst)
    # print(first_seatid)
    # print(lst[-1])
    # print(len(lst))
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]
    # seat = first_seatid
    # (lambda seats: print(
    #     f"Highest: {max(seats)}\nYour seat: {next(filter(lambda x: x not in seats, range(min(seats), max(seats))))}"))
    #
    # for i in range(1, total_seats):
    #     seat = seat + 1
    #     if (lst[i] != seat):
    #         print('Seat:', seat)
    #         break


def find_biggest_seat_id(list_of_seatid):
    # print('List:',list_of_seatid)
    return max(list_of_seatid)


def convert_binary_to_int(binary_string):
    return int(binary_string, base=2)


def convert_to_binary(locations):
    new_locations = []
    for location in locations:
        location = location.replace('F', '0')
        location = location.replace('B', '1')
        location = location.replace('L', '0')
        location = location.replace('R', '1')
        new_locations.append(location)
    return new_locations


def find_seatids(seating_locations):
    binary_locations = convert_to_binary(seating_locations)
    seat_ids = []
    for location in binary_locations:
        find_row = convert_binary_to_int(location[:7])
        find_column = convert_binary_to_int(location[-3:])
        seat_id = (find_row*8) + find_column
        seat_ids.append(seat_id)
    return seat_ids


def main():
    # input_content = open("input/day3.txt", "r")
    with open("input/day5.txt") as input_content:
        sample_input = input_content.read().splitlines()
    all_seats = find_seatids(sample_input)
    # print(all_seats)
    large_id = find_biggest_seat_id(all_seats)
    print('Large id:', large_id)
    all_seats.sort(reverse=False)
    missed_id = find_missing(all_seats)
    # print('Largest seat id:', large_id)
    print('Missed id:',missed_id)


if __name__ == '__main__':
    main()
