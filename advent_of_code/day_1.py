

def calculate_frequency():

    with open("inputs/day_1.txt", 'r') as f:
        frequency = 0

        for num in f.readlines():
            frequency += int(num)

        print(frequency)

def first_twice_frequency():

    with open("inputs/day_1.txt", 'r') as f:
        changes = f.readlines()
        print(changes)
        frequency = 0
        list_freq = {frequency}
        i = 0
        while True:
            print(len(list_freq))
            #i += 1
            #print(i)
            for num in changes:
                frequency += int(num)
                if frequency in list_freq:

                    return frequency
                else:
                    list_freq.add(frequency)
        return False

def test():
    f = open("inputs/day_1.txt").read()
    print(f[:])


if __name__ == '__main__':
    #main()
    #calculate_frequency()
    #test()
    print(first_twice_frequency())
