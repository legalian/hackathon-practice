from flask import Flask, render_template
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


@app.route('/elements',methods=["GET","POST"])
def elements():
	if request.method == "GET":

	elif request.method == "POST":


@app.route('/elements/<int:id>',methods=["GET","PUT","DELETE"])
def element(id):
	if request.method == "GET":

	elif request.method == "PUT":

	elif request.method == "DELETE":
		




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




