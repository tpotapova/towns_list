import redis
import json
from bottle import route, run, template, response,static_file

@route('/')
def index_main():
    return template('index.html', left_brackets = '{{', right_brackets = '}}')
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/home/potap/towns/static/')
@route('/towns')
def index():
	r = redis.Redis(host='localhost', port=6379, db=0)
	output = []
	for i in range(1,r.dbsize()+1):
		output.append(r.get(i))
	response.content_type = 'application/json'
	output_json = json.dumps(output)
	return output_json

run(host='0.0.0.0', port=8080)
