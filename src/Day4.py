import string


def clear_info(detail):
    detail = detail.replace('\n', ' ')
    print(detail)
    detail_info = detail.split(' ')
    passport_dict = {}
    # print(detail_info)
    for single_info in detail_info:
        info = single_info.split(':')
        passport_dict[info[0]] = info[1]
    return passport_dict


def validate_byr(byr):
    valid_byr = False
    valid_int, byr_int = represents_int(byr)
    if valid_int and byr_int >= 1920 and byr_int <= 2002:
        valid_byr = True
    return valid_byr


def validate_iyr(iyr):
    valid_iyr = False
    valid_int, iyr_int = represents_int(iyr)
    if valid_int and iyr_int >= 2010 and iyr_int <= 2020:
        valid_iyr = True
    return valid_iyr


def validate_eyr(eyr):
    valid_eyr = False
    valid_int, eyr_int = represents_int(eyr)
    if valid_int and eyr_int >= 2020 and eyr_int <= 2030:
        valid_eyr = True
    return valid_eyr


def validate_hgt(hgt):
    valid_hgt = False
    if isinstance(hgt, str):
        cm_or_in = hgt[-2:]
        hgt_value = hgt[:-2]
        print("cm_or_in:",cm_or_in)
        print("hgt_value:",hgt_value)
        valid_int, hgt_int = represents_int(hgt_value)
        if valid_int:
            print('coming here')
            hgt_int = int(hgt_value)
            if cm_or_in == 'cm' and hgt_int >= 150 and hgt_int <= 193:
                valid_hgt = True
            if cm_or_in == 'in' and hgt_int >= 59 and hgt_int <= 76:
                valid_hgt = True
    return valid_hgt


def validate_hcl(hcl):
    valid_hcl = False
    return valid_hcl


def validate_ecl(ecl):
    valid_ecl = False
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl in eye_colors:
        valid_ecl = True
    return valid_ecl


def represents_int(somestring):
    val = 0
    try:
        val = int(somestring)
        return True, val
    except ValueError:
        return False, val


def represents_hex(somestring):
    try:
        return all(c in string.hexdigits for c in somestring)
    except ValueError:
        return False


def validate_hcl(hcl):
    valid_hcl = False
    check_hash = hcl[:1]
    hcl_len = len(hcl)
    # print('hash:',check_hash)
    if hcl_len == 7 and check_hash == '#' and represents_hex(hcl[1:]):
        valid_hcl = True
    return valid_hcl


def validate_pid(pid):
    valid_pid = False
    orig_length = len(pid)
    modified_pid = pid.lstrip('0')
    # modified_length = len(modified_pid)
    if represents_int(modified_pid):
        if orig_length == 9:
            valid_pid = True
    return valid_pid


def validate_passport(passport):
    # is_valid = False
    validation = []
    valid_iyr = validate_iyr(passport['iyr'])
    valid_byr = validate_byr(passport['byr'])
    valid_eyr = validate_eyr(passport['eyr'])
    valid_hgt = validate_hgt(passport['hgt'])
    valid_hcl = validate_hcl(passport['hcl'])
    valid_ecl = validate_ecl(passport['ecl'])
    valid_pid = validate_pid(passport['pid'])
    print('iyr,byr,eyr,hgt,hcl,ecl,pid')
    validation.extend([valid_iyr,valid_byr,valid_eyr,valid_hgt, valid_hcl, valid_ecl,valid_pid])
    print(validation)
    return all(validation)


def validate_passports(passports_info):
    valid_count = 0
    invalid_count = 0
    # count = 0
    mandatory_keys = {'iyr', 'byr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for passport in passports_info:
        passport = clear_info(passport)
        # print(passport)
        # print(type(passport))
        # count = count + 1
        if(passport.keys()) >= mandatory_keys:
            if validate_passport(passport):
                valid_count = valid_count+1
        else:
            invalid_count = invalid_count+1
        # if count == 3:
        #     break
    return valid_count,invalid_count


def main():
    # input_content = open("input/day3.txt", "r")
    with open("input/day4.txt") as input_content:
        sample_input = input_content.read().split("\n\n")
        print('Length:', len(sample_input))
        print('Valid and Invalid count:', validate_passports(sample_input))


if __name__ == '__main__':
    main()

