def is_palindrome_for_loop(num):
   
    str_num = str(num)
    length = len(str_num)
    
    
    for i in range(length // 2):
        if str_num[i] != str_num[length - 1 - i]:
            return False     
    return True  # It is a palindrome

num = 121
print(is_palindrome_for_loop(num)) 