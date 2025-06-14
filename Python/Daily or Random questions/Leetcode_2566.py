# 2566. Maximum Difference by Remapping a Digit
def minMaxDifference(num):
    num_str = str(num)

    # Find first digit not equal to '9' for max
    for_max = next((ch for ch in num_str if ch != '9'), None)
    max_version = num_str.replace(for_max, '9') if for_max else num_str

    # Find first digit not equal to '0' for min
    for_min = next((ch for ch in num_str if ch != '0'), None)
    min_version = num_str.replace(for_min, '0') if for_min else num_str

    return int(max_version) - int(min_version)

    digits = list(str(num))
    n = len(digits)
    sorted_digits = sorted(digits)

    max_digit = sorted_digits[0]
    max_count = 1
    current_count = 1

    for i in range(1, n):
        if sorted_digits[i] == sorted_digits[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_digit = sorted_digits[i - 1]
            current_count = 1

        # Early stop (optional), only if it already beats max
        if current_count > max_count:
            max_count = current_count
            max_digit = sorted_digits[i]

    # Final check for last digit group
    if current_count > max_count:
        max_digit = sorted_digits[-1]

    num_str = str(num)
    max_version = num_str.replace(max_digit, '9')
    min_version = num_str.replace(max_digit, '0')

    return int(max_version) - int(min_version)

res = minMaxDifference(90)

print(res)


        