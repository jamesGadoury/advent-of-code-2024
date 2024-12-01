# https://adventofcode.com/2024/day/1

def get_input(input_pth):
    list1, list2 = [], []
    with open(input_pth) as f:
        for line in f.readlines():
            i1, i2 = [x for x in line.strip().split(" ") if x != ""]
            list1.append(int(i1))
            list2.append(int(i2))
    return list1, list2


def compute_similarity_score(list1, list2):
    assert len(list1) == len(list2)
    
    list1, list2 = sorted(list1), sorted(list2)

    score = 0

    for n1 in list1:
        score += list2.count(n1) * n1
    
    return score


def test_sample():
    assert compute_similarity_score(*get_input("sample_input.txt")) == 31


def main():
    print(compute_similarity_score(*get_input("input.txt")))


if __name__ == "__main__":
    main()
