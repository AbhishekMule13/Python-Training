def is_duck_no(num_str):
    if num_str[0]=='0':
        return False
    return '0' in num_str[1:]
num=input("Enter the number:")
if num.isdigit():
    if is_duck_no(num):
        print("It is a Duck Number.")
    else:
        print("It is NOT a Duck Number.")
else:
    print("Invalid input! Please enter only positive digits.")
