from flask import Flask, render_template, request
import os
app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


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
		print(elements)
		return {'payload':elements}
	elif request.method == "POST":
		elements.append(request.json)
		return {'payload':elements}


@app.route('/elements/<int:id>',methods=["GET","PUT","DELETE"])
def element(id):
	if request.method == "GET":
		return elements[id]
	elif request.method == "PUT":
		elements[id] = request.json
		return elements[id]
	elif request.method == "DELETE":
		del elements[id]
		return "OK"

@app.route('/push_template')
def push():
	return render_template('/push_template.html')

@app.route('/application/json')
def jspage():
	return elements;


@app.route('/debug')
def debug():
	res = ""
	for path,dirs,files in os.walk("."):
		res += path + "\n"
		for f in files:
			res += "-" + f + "\n"
	return res


@app.route('/')
def index():
    return render_template('/template.html',my_string="jujujujujujuj",my_list=[45,2,5,3,45])

if __name__ == '__main__':
    app.run(debug=True)




