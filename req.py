import requests

def get_weather(url):
	result = requests.get(url)
	if result.status_code == 200:
		return result.json()
	else:
		print('Что-то пошло не так')


def get_names(url):
	result = requests.get(url)
	if result.status_code == 200:
		return result.json()
	else:
		print('Что-то пошло не так')


if __name__ == '__main__':
	data = get_names('http://api.data.mos.ru/v1/datasets/2009/rows?api_key=3a700437b2cbe9ffb2cd6d9b1b7260a5')
	print(data)