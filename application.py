from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("application-form.html")

# Did not end up using - what's the purpose of seperating this out?
# @app.route('/application-form')
# # def ():
#     """Handles submission of form in application-form.html"""


@app.route('/application', methods=["POST"])
def response():
    """Takes inputs from form and returns acknowlegement of submission"""

    first = request.form.get("first")
    last = request.form.get("last")
    position = request.form.get("position")
    salary = request.form.get("salary")
    return render_template('application-response.html',
                           first=first,
                           last=last,
                           position=position,
                           salary=salary)

if __name__ == "__main__":
    app.run(debug=True)
