# https://adventofcode.com/2024/day/2

def get_input(input_pth):
    reports = []
    with open(input_pth) as f:
        for line in f.readlines():
            reports.append([int(x) for x in line.strip().split(" ")])
    return reports


def validate_condition_one(report):
    return sorted(report) == report or sorted(report, reverse=True) == report 


def validate_condition_two(report):
    for i in range(1, len(report)):
        distance = abs(report[i] - report[i-1])
        if distance < 1 or distance > 3:
            return False
    return True


def compute_safe_report_count(reports):
    safe_count = 0
    for report in reports:
        if validate_condition_one(report) and validate_condition_two(report):
            safe_count += 1
    return safe_count


def test_validate_condition_one():
    assert validate_condition_one([1, 2, 3])
    assert validate_condition_one([3, 2, 1])
    assert validate_condition_one([3, 3, 1])
    assert not validate_condition_one([1, 3, 1])
    assert not validate_condition_one([5, 3, 7])


def test_validate_condition_two():
    assert validate_condition_two([1, 2, 3])
    assert validate_condition_two([1, 3, 5])
    assert validate_condition_two([1, 4, 7])
    assert validate_condition_two([3, 2, 1])
    assert validate_condition_two([5, 3, 1])
    assert validate_condition_two([7, 4, 1])
    assert not validate_condition_two([7, 7, 4])
    assert not validate_condition_two([4, 7, 7])
    assert not validate_condition_two([1, 5, 8])
    assert not validate_condition_two([8, 5, 1])


def test_sample():
    assert compute_safe_report_count(get_input("sample_input.txt")) == 2


def main():
    print(compute_safe_report_count(get_input("input.txt")))


if __name__ == "__main__":
    main()
