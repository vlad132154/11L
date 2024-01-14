from Victory import game


def f():
    nam = input('Введите своё имя: ')
    ans = input(f'Здравстуй, {nam}, ты готов? ')
    if ans.lower() == 'да':
        game()
    elif ans.lower() == 'нет':
        print('Готовься ещё')
    else:
        print('Введите понятный ответ!')
        f()
