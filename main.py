from flask import Flask, render_template, request, url_for


app = Flask(__name__)




@app.route('/', methods=["GET", "POST"])
def index():
    username = ''
    email = ''
    if request.method=="POST":
        username_error = ''
        password_error = ''
        email_error = ''

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        verify = request.form["verify"]


        if len(email) > 0:
            count_amp = 0
            count_sp = 0
            count_punto = 0
            for  c in email:
                if c == '@':
                    count_amp +=1
                if c == ' ':
                    count_sp +=1
                if c == '.':
                    count_punto +=1

            if not ( count_amp == 1 and count_punto == 1 and count_sp == 0):
                email_error = 'Email address must contain one "@", one period, and no spaces'
            if (len(email) < 3 or len(email) > 20):
                email_error = 'Email address must contain between 3 and 20 characters'

        if len(username)==0:
            username_error = 'You must provide a username'
        if ' ' in username:
            username_error = 'Spaces not allowed in username'
        if len(username) < 3:
            username_error = 'Username must contain at least three characters'
        if len(username) > 20:
            username_error = 'Username must contain no more than 20 characters'
        if len(password)==0:
            password_error = 'You must provide a password'
        else:
            if not password==verify:
                password_error = 'Passwords do not match'

        print('53',username_error)
        print('54',email_error)
        print('55',password_error)

        if username_error or email_error or password_error:
            return render_template('index.html',username=username, email=email, username_error=username_error, email_error=email_error,password_error=password_error  )
        else:
            return render_template('welcome.html', username=username)

    return render_template('index.html')





if __name__ == "__main__":
    app.run()
