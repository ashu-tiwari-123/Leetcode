# 1432. Max Difference You Can Get From Changing an Integer

def maxDiff(num):
    num_str = str(num)

    # Step 1: Maximize - replace first digit not '9' with '9'
    for ch in num_str:
        if ch != '9':
            max_version = num_str.replace(ch, '9')
            break
    else:
        max_version = num_str  # all digits were 9 already

    # Step 2: Minimize - choose the right digit to replace with '1' or '0'
    # If first digit is not '1', try replacing it with '1' (can't be '0' to avoid leading zero)
    first = num_str[0]
    if first != '1':
        min_version = num_str.replace(first, '1')
    else:
        # First digit is '1', find next digit not 0 or 1
        for ch in num_str[1:]:
            if ch not in ['0', '1']:
                min_version = num_str.replace(ch, '0')
                break
        else:
            min_version = num_str  # nothing to minimize

    return int(max_version) - int(min_version)
