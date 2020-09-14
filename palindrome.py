def is_palindrome(var):
    # When var type is not str or int
    if type(var) != str and type(var) != int:
        raise TypeError

    elif isinstance(var, int):
        var = str(var)
    elif isinstance(var, str):
        var = var.lower().replace(' ', '')
    return var == var[::-1]
