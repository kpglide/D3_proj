from flask import Flask
from flask import render_template

app = Flask(__name__)
	
app.config.update(
	SERVER_NAME = 'localhost:8080'
)

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')
			
if __name__ == "__main__":
	app.run(debug=True)