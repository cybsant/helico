# ⬛ - земля ⚫🟩⬛🟫⬜🟧🟨
# 🟦 - вода 🌀🚰⛲🌊🟦
# 🌴 - дерево 🌴🌳🎄🌲🌵
# 🏥 - лечение 💊🍄⛑🏥
# 🏦 - апгрейд 🛠🏦

# 🌥 - тучка ⛅🌧🌨🌥💭
# ⚡ - молния ⚡🌪⛈🌩
# 🔥 - огонь 💥🔥
# 🚁 - вертолет 🚒🚁🛩
# 🧡 - жизни💙💚💛💜
# 💧 - емкости 🛢💧🪣
# ⭐ - деньги 💰💲🏆⭐🪙

""" Моды на графику """
# * DEFAULT
CELL_TYPES = "⬛🌲🌊🏥🏦"

# * Фэнтези
CELL_TYPES = "⚫🌳🌀🍄✨"

""" Моды на сложность """
# * Зима
# [ Вода замерзла(дольше набирать, но движение по льду быстрее) ]
CELL_TYPES = "⬛🎄⬜🏥🏦"

# * Острова
# [ Передвигаемся по воде(вода всегда есть) ]
# [ Больниц нет, ищем пилюли(1 пилюля = 1 очко здоровья) ]
# [ Мастерских нет, редко встречаются механники(медленный апгрейд) ]
CELL_TYPES = "🟦🏝⛰💊🛠"

# * Тропики
# [ Больниц нет, редко встречаются врачи(медленное лечение) ]
# [ Мастерских нет, редко встречаются механники(медленный апгрейд) ]
CELL_TYPES = "🟫🌴🟦⛑🛠"

# * Пустыня
# [ Вместо рек и озёр, одиночные родники ]
# [ Больниц нет, ищем пилюли(1 пилюля = 1 очко здоровья) ]
# [ Мастерских нет, редко встречаются механники(медленный апгрейд) ]
CELL_TYPES = "🟨🌵⛲💊🛠"
