# 1

# try:
#     num_1 = input('first number: ')
#     num_2 = input('second number: ')
#     int(num_1)/int(num_2)
# except ZeroDivisionError:
#     print('zero division')
# except ValueError:
#     print('value error')

# 2

# try:
#     num_1 = input('first number: ')
#     num_2 = input('second number: ')
#     result = int(num_1)/int(num_2)
# except (ZeroDivisionError, ValueError):
#     pass
# else:
#     print(f'result is {result}')
# finally:
#     print('End of the program')

# 3

# try:
#     num_1 = input('first number: ')
#     num_2 = input('second number: ')
#     result = int(num_1)/int(num_2)
# except (ZeroDivisionError, ValueError) as e:
#     print(f'program broke with error: {e}')
# else:
#     print(f'result is {result}')
# finally:
#     print('End of the program')

# 4

# try:
#     num = input('please give number: ')
#     num = float(num)
#     if num < 0:
#         raise ValueError('number cannont be negative')
# except ValueError as e:
#     print(e)
# else:
#     print(f'number is {num}')

# num = float(input('give a number: '))
# if num < 0:
#     raise ValueError('number cannot be negative')
# print(f'you entered {num}')

# 5

# class NegativeNumberError(ValueError):
#     def __init__(self, message='number cannot be negative'):
#         super().__init__(message)

# num = float(input('give a number: '))
# if num < 0:
#     raise NegativeNumberError
# print(f'you entered {num}')

# 6

# def invert_list(num_list):
#     try:
#         return [1 / num for num in num_list]
#     except TypeError:
#         print('input must be list of invertible numbers')
#     except ZeroDivisionError:
#         print('input items must be non-zero')
#     except Exception as e:
#         print(f'other exception: {e}')

# print(invert_list([1, 2])) # [1.0, 0.5]
# print(invert_list(['a', 1])) # type error block
# print(invert_list([1, 0])) # zero division error block

# 7

# b and c

# 8

# students = {'John': 25, 'Jane': 22, 'Doe': 30}

# def get_age(name):
#     try:
#         return students[name]
#     except KeyError:
#         return 'Student not found'
    
# print(get_age('John')) # 25
# print(get_age('Bob')) # Student not found

# 9

# numbers = [1, 2, 3, 4, 5]

# def lbyl_fetch_sixth(ls):
#     if len(ls) < 6:
#         return None
#     return ls[5]

# def afnp_fetch_sixth(ls):
#     try:
#         return ls[5]
#     except IndexError:
#         return None
    
# print(lbyl_fetch_sixth(numbers)) # None
# print(afnp_fetch_sixth(numbers)) # None

# 10

# b and d
