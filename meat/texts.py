true_start_text = 'Приветствую тебя в нашем боте👋,'
false_start_text = 'Ты уже зарегистрирован в боте,'
start_desc = 'Этот бот фармилка дота 3 гыгыгы'
commands = ('/help', '/bonus ', '/profile', '/shop', '/fight', '/farm')
commands_description = ('Посмотреть все возможные команды👀',
                        'Получить ежедневный бонус💸',
                        'Посмотреть свой профиль👤',
                        'Заглянуть в магазин🛍',
                        'Отправить своего героя драться⚔️',
                        'Отправить героя фармить👨🏿‍🌾',)


def txt_commands():
    return ''.join(f"\n{com} - {desc} " for com, desc in zip(commands, commands_description))
