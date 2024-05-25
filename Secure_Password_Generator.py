import random

def request_input(prompt, valid_responses):
    while True:
        response = input(prompt).lower()
        if response in valid_responses:
            return response
        elif response == 'выход':
            return response
        else:
            print('Неверный ввод, попробуйте снова\n')

def making_a_list(include_digits, include_uppercase, include_lowercase, include_punctuation, exclude_ambiguous):
    chars = ''
    if include_digits:
        chars += digits
    if include_uppercase:
        chars += uppercase_letters
    if include_lowercase:
        chars += lowercase_letters
    if include_punctuation:
        chars += punctuation
    if exclude_ambiguous:
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')
    return chars

def print_generate_password(password_length, chars):
    return ''.join(random.choice(chars) for _ in range(password_length))

def generate_password():
    print('Добро пожаловать в генерацию паролей!\n')
    print('В любой момент ты можешь завершить генерацию паролей, написав "выход"\n')

    include_digits = request_input('Включать ли в пароль цифры от 0 до 9? (да/нет): ', ['да', 'нет'])
    include_uppercase = request_input('Включать ли в пароль прописные буквы? (да/нет): ', ['да', 'нет'])
    include_lowercase = request_input('Включать ли в пароль строчные буквы? (да/нет): ', ['да', 'нет'])
    include_punctuation = request_input('Включать ли в пароль символы "!#$%&*+-=?@^_"? (да/нет): ', ['да', 'нет'])
    exclude_ambiguous = request_input('Исключать ли неоднозначные символы "il1Lo0O"? (да/нет): ', ['да', 'нет'])

    if any(response == 'выход' for response in [include_digits, include_uppercase, include_lowercase, include_punctuation, exclude_ambiguous]):
        return

    while True:
        password_length = input('Какой длины должен быть пароль? ')
        if password_length.isdigit() and int(password_length) >= 5:
            password_length = int(password_length)
            break
        else:
            print("Длина пароля должна быть не менее 5 символов, попробуйте снова\n")

    while True:
        number_of_passwords = input('Сколько паролей вам нужно сгенерировать? ')
        if number_of_passwords.isdigit() and int(number_of_passwords) >= 1:
            number_of_passwords = int(number_of_passwords)
            break
        else:
            print('Количество паролей должно быть не менее 1, попробуйте снова\n')

    chars = making_a_list(include_digits == 'да', include_uppercase == 'да', include_lowercase == 'да', include_punctuation == 'да', exclude_ambiguous == 'да')

    for i in range(number_of_passwords):
        print(f'Ваш {i + 1} пароль: "{print_generate_password(password_length, chars)}"')

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

while True:
    user_input = input('Введите "генератор паролей" для создания надежного пароля или "выход", чтобы закончить:\n').lower()
    if user_input == 'генератор паролей':
        generate_password()
    elif user_input == 'выход':
        break
    else:
        print('Неверное название, попробуйте снова\n')
        
        
    
