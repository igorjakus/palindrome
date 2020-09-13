def is_text_palindrome(text):
    text = text.lower().replace(' ', '')
    return text == text[::-1]

def is_number_palindrome(number):
    num_list = []
    while number:
        num_list.append(number % 10)
        number = number // 10
    return num_list == num_list[::-1]

    # 1234 -> [1, 2, 3, 4]
    # 1234 % 10 = 4
    # 123 % 10 = 3
    # 12 % 10 = 2
    # 1 % 10 = 1
