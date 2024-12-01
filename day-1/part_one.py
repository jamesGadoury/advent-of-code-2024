# https://adventofcode.com/2024/day/1

def get_input(input_pth):
    list1, list2 = [], []
    with open(input_pth) as f:
        for line in f.readlines():
            i1, i2 = [x for x in line.strip().split(" ") if x != ""]
            list1.append(int(i1))
            list2.append(int(i2))
    return list1, list2


def compute_total_distance(list1, list2):
    assert len(list1) == len(list2)
    
    list1, list2 = sorted(list1), sorted(list2)

    distances = []
    for n1, n2 in zip(list1, list2):
        distances.append(abs(n1 - n2))
    return sum(distances)


def test_sample():
    assert compute_total_distance(*get_input("sample_input.txt")) == 11


def main():
    print(compute_total_distance(*get_input("input.txt")))


if __name__ == "__main__":
    main()
