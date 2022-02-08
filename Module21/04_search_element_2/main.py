site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}


def find_key(struct, key, max_depth=None, depth=1):
	result = None

	if max_depth and max_depth < depth:
		return result

	if key in struct:
		return struct[key]

	for sub_struct in struct.values():
		if isinstance(sub_struct, dict):
			result = find_key(sub_struct, key, max_depth, depth=depth + 1)
			if result:
				break
	return result


user_key = input('Введите искомый ключ: ')
deep = input('Хотите ввести максимальную глубину? Y/N: ')

if deep == 'n':
	value = find_key(site, user_key)
	print('Значение ключа: ', value)
else:
	deep_max = int(input('Введите максимальную глубину:'))
	value = find_key(site, user_key, max_depth=deep_max)
	print('Значение ключа: ', value)
