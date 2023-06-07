true_start_text = 'Приветствую тебя в нашем боте,'
false_start_text = 'Ты уже зарегистрирован в боте,'
commands = ('/help', '/bonus ', '/profile', '/shop', '/fight')


def txt_commands():
    return ''.join(f"\n{com}" for com in commands)
