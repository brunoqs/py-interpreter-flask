from flask import Flask
from flask import request, render_template
import subprocess, os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		code = request.form.get('code')
		f = open('file.py', 'w+')
		f.write(str(code))
		#os.system("echo " + code + " > /home/unclear/Projetos/pyweb-flask/file.py")
		#output = subprocess.check_output(["python /home/unclear/Projetos/pyweb-flask/file.py"], shell=True)
		#output = output.decode("utf-8")
		return render_template("index.html")
	else:
		return render_template("index.html")

@app.route('/run', methods=['POST', 'GET'])
def run():
	if request.method == 'POST':
		output = subprocess.check_output(["python /home/unclear/Projetos/pyweb-flask/file.py"], shell=True)
		output = output.decode("utf-8")
		return render_template("index.html", output=output)
	else:
		return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
