from flask import Flask, render_template, request
from flask_socketio import SocketIO
import os
app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
socketio = SocketIO(app)

CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']

@app.route('/next')
def next():
	return "Next"

@app.route('/69')
def nice():
	return "nice"


elements = []



@app.route('/elements',methods=["GET","POST"])
def element_all():
	if request.method == "GET":
		return {'payload':elements}
	elif request.method == "POST":
		elements.append(request.json)
		return {'payload':elements}


@app.route('/elements/<int:id>',methods=["GET","PUT","DELETE"])
def element(id):
	if request.method == "GET":
		return elements[id]
	elif request.method == "PUT":
		elements[id] = request.json[id]
		return elements[id]
	elif request.method == "DELETE":
		elements.remove(id)
		return "OK"

@app.route('/push_template')
def push():
	return render_template('/push_template.html')


# @app.route('/callback',methods=["GET"])
# def callback():
# 	print(request.json)
# 	print(request.args)
# 	# session_code = request.env['rack.request.query_hash']['code']
# 	requests.post('https://github.com/login/oauth/access_token',params={'accept':'json'},data={'client_id':CLIENT_ID,'client_secret':CLIENT_SECRET,'code':session_code})




# 	# extract the token and granted scopes
# 	access_token = JSON.parse(result)['access_token']



# 	# requests.get('https://api.github.com/events',params=payload)
# 	# requests.post('https://httpbin.org/post',params=payload,data={'key':'value'})




@app.route('/')
def index():
    return render_template('/template.html',my_string="jujujujujujuj",my_list=[45,2,5,3,45])

if __name__ == '__main__':
	socketio.run(app,debug=True)
    # app.run(debug=True)






















