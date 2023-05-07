user_command = input('사용할 명령어를 입력하시오:')

try:
    exec(user_command)
    print('명령이 잘 실행되었습니다.')
except Exception as e:
    print('실행할 수 없는 명령이 포함되어 있습니다.')