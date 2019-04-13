import random, csv


def generate_randints(n):
    """
    Generates n random integers between 0 and 1,000,000 (inclusive)

    :param int n: number of ints to generate
    :return: list of random ints
    """
    rand_ints = list()
    for x in range(n):
        rand_ints.append(random.randint(0, 1000000))

    return rand_ints


def dump_list_to_csv(filename, list):
    """
    Dumps contents of list to <filename>.csv
    Each row contains 20 columns and each element is delimited with a comma

    :param filename: name of file (excluding extention)
    :param list: list of items to write to .csv
    :return: void
    """
    try:
        with open(filename + '.csv', 'w') as data_dump:
            # iterate through list appending "," after each entry
            for x in range(len(list)):
                data_dump.write(str(list[x]) + ',')

                # create line break after every 20 items (20 columns)
                if (x + 1) % 20 is 0:
                    data_dump.write('\n')
    except IOError:
        print('I/O error')

dump_list_to_csv('1k_ints', generate_randints(1000))
dump_list_to_csv('10k_ints', generate_randints(10000))
dump_list_to_csv('100k_ints', generate_randints(100000))
dump_list_to_csv('1000k_ints', generate_randints(1000000))
