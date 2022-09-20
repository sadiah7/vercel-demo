from flask import *

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("/form.html")

@app.route("/form", methods=["POST"])
def form():
    fn = request.form.get("fn")
    ln = request.form.get("ln")
    un = request.form.get("un")
    pas = request.form.get("pas")
    print(fn,ln,un,pas)

    return render_template("/done.html")



if __name__ == '__main__':
    app.run()
