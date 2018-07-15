from flask import Flask
from flask import render_template
from localip import local_ip_address

print("\n\nType this > {}:5000 < in your browser to connect.\n\n".format(local_ip_address))

app = Flask(__name__)


@app.route("/")
def show():
    return render_template("remote.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0')

