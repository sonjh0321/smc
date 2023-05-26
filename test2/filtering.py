def starts_with_any(string, prefixes):
    return any(string.startswith(prefix) for prefix in prefixes)


allowed_commands = ['print', 'len', 'type', 'a']

user_input = input("사용할 명령어를 입력하시오: ")

tokens = user_input.split(';')
check = True

for i in tokens:
    if not starts_with_any(i, allowed_commands):
        print('불가능한 명령어가 있습니다.')
        check = False

if check:
    exec(user_input)