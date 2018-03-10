from flask import Flask, abort, request
from datetime import datetime

app = Flask(__name__)

#from news_list import all_news
from req import get_weather, get_names

apikey = '009e49851ff8a6a2a9829caa3d79736b'
city_id = 524901







@app.route('/names/')
def names_by_year():
	url =  'http://api.data.mos.ru/v1/datasets/2009/rows?api_key=3a700437b2cbe9ffb2cd6d9b1b7260a5'
	names = get_names(url)
	names_list = []
	
	year_id = request.args.get('year')
	print(year_id)
	year_id = str(year_id)
	
	for row in names:
		names_list.append(row.get('Cells'))

	result = '<table><tr><th>Имя</th><th>Количество человек</th><th>Год</th><th>Месяц</th></tr>'
	
	
	for name in names_list:
		if str(name.get('Year')) == year_id:
			result += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (name.get('Name'), name.get('NumberOfPersons'), name.get('Year'), name.get('Month'))  
		else:
			result += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (name.get('Name'), name.get('NumberOfPersons'), name.get('Year'), name.get('Month'))  

	result += '</table>'	
	return result



#@app.route('/names')
#def all_names():
#	url =  'http://api.data.mos.ru/v1/datasets/2009/rows?api_key=3a700437b2cbe9ffb2cd6d9b1b7260a5'
#	names = get_names(url)
#	names_list = []
#	for row in names:
#		names_list.append(row.get('Cells'))
#	result = '<table><tr><th>Имя</th><th>Количество человек</th><th>Год</th><th>Месяц</th></tr>'
#	for name in names_list:
#		result += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (name.get('Name'), name.get('NumberOfPersons'), name.get('Year'), name.get('Month'))  
#	result += '</table>'
#	return(result)
#	for name in names:
#	print(name)
	
@app.route('/')
def index():
	url =  'http://api.openweathermap.org/data/2.5/weather?id=%s&appid=%s&units=metric' % (city_id, apikey)
	weather = get_weather(url)
	cur_date = datetime.now().strftime('%d.%m.%Y')
	result = '<p><b>Teмпература:</b> %s</p>' % weather['main']['temp']
	result += '<p><b>Город:</b> %s</p>' % weather['name']
	result += '<p><b>Дата:</b> %s</p>' % cur_date

	return result

@app.route('/news')
def all_the_news():
	colors = ['green', 'red', 'blue', 'magenta']
	try:
		limit = int(request.args.get('limit'))
	except:
		limit = 10
	color = request.args.get('color') if request.args.get('color') in colors else 'black'
	return '<h1 style="color: %s">News: <small>%s</small></h1>' % (color, limit)

@app.route('/news/<int:news_id>')
def news_by_id(news_id):
	news_to_show = [news for news in all_news if news['id'] == news_id]
	if len(news_to_show) == 1:
		result = "<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>"
		result = result % news_to_show[0]
		return result
	else:
		abort(404)


if __name__   == '__main__':
	app.run(port=5019, debug=True)