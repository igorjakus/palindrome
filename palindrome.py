def is_palindrome(var):

    if isinstance(var, str):
        var = var.lower().replace(' ', '')
        return var == var[::-1]

    elif isinstance(var, int) and not isinstance(var, bool):
        num_list = []
        while var:
            num_list.append(var % 10)
            var = var // 10
        return num_list == num_list[::-1]
        # 1234 -> [4, 3, 2, 1]
        # 1234 % 10 = 4
        # 123 % 10 = 3
        # 12 % 10 = 2
        # 1 % 10 = 1

    # When var type isn't str or int
    raise TypeError
