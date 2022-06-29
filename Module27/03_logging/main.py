def log_errors(func):
    def surrogate(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError as z_error:
            file_content1 = ('<{}>  <{}>  <{}>  <{}>\n'.format(func.__name__, kwargs, Exception, z_error))
            with open('function_errors.log', 'a', encoding='utf8') as file:
                file.write(file_content1)
            raise ZeroDivisionError
        except ValueError as v_error:
            file_content2 = ('<{}>  <{}>  <{}>  <{}>\n'.format(func.__name__, args, Exception, v_error))
            with open('function_errors.log', 'a', encoding='utf8') as file:
                file.write(file_content2)
            raise ValueError
    return surrogate
# Проверить работу на следующих функциях
@log_errors
def perky(param):
    return param / 0
@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')
lines = [
    'Имя почта@mail.ru 20',
     'имя почта@mail.ru 18'
     .....
     .....
     .....
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)