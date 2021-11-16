import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/', methods=['GET'])
def loginform():
    html_form = '''
        <html>
            <head><title>DevSecOps demo</title></head>
            <body>
                <h1>Log in</h1>

                <form action="./authenticate/" method="post">
                    Username <input name="user_name" type="text" /><br />
                    Password <input name="user_password" type="password" /><br />
                    <input type="submit" value="Log in">
                </form>

            </body>
        </html>
    '''
    return html_form

@app.route('/authenticate/', methods=['POST'])
def verify_password():

    the_password = "R5$s9*!k_959h2wvligw40*-+27Q4"

    html_response = "<h1>Checking login for " + request.form["user_name"] + "</h1>"

    if(request.form["user_password"] != the_password):
        html_response+="Wrong password"
    else:
        html_response+="Correct password"
    
    html_response+='''<br />Click <a href="/">here</a> to return to the login page'''

    return html_response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8181)
