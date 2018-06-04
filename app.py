from flask import Flask
from flask import request, render_template
import subprocess, os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	ip = request.remote_addr
	if request.method == 'POST':
		code = request.form.get('code')
		if "os" in code or "subprocess" in code:
			return render_template("index.html", success="Código contém bibliotecas não permitidas!")
		f = open(str(ip), 'w+')
		f.write(str(code))
		return render_template("index.html", success="Código enviado com sucesso!")
	else:
		return render_template("index.html")

@app.route('/run', methods=['POST', 'GET'])
def run():
	if request.method == 'POST':
		try:
			output = subprocess.check_output(["python /home/unclear/Projetos/pyweb-flask/" + str(request.remote_addr)], shell=True, stderr=subprocess.STDOUT)
			output = output.decode("utf-8")
		except subprocess.CalledProcessError as e:
			return render_template("index.html", output=e.output.decode("utf-8"))
		return render_template("index.html", output=output)
	else:
		return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
