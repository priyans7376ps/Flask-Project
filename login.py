from flask import Flask , redirect, request, url_for, Response,session

app= Flask(__name__)
app.secret_key= "superkeys"

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method=="POST":
        username= request.form.get("username")
        password= request.form.get("password")

        if username == "Priyanshu" and password=="1234":
            session["user"]= username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid , Try again !!!!", mimetype="text/plain")
    

    return """
                                        <h2>Login Form</h2>
                                        <form method = "POST">
                                         Username : <input type = "text" name="username"><br><br>
                                         Password : <input type = "password" name ="password"><br><br>
                                         <input type = "submit" value ="login"> 
                                        </form>
                                          """


@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
               <h1>Hello Mr/Mrs {session["user"]} </h1><br><br>
               <h3> Thank You For Visit My page </h3>
               <a href ="{url_for('info')}">Info</a>
               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
               <a href ="{url_for('logout')}">Logout</a>
             """
    return redirect(url_for("home"))


@app.route("/info")
def info():
    if "user" in session:
        return f'''
        <h1><pre> 
        Information About Login form </pre></h1><br>
        <h3><pre>
         A login form is a secure user interface element on a website or app 
         where users enter their credentials to access a protected account.
         Here are 6 key facts about login forms:
         Authentication: It verifies the user's identity by matching their credentials against a database.
         Essential Fields: Standard forms include input fields for a username (or email) and a password.
         Security & Privacy: Features like encrypted password fields, "show password" toggles, and 
         two-factor authentication (2FA) keep data secure.
         User Convenience: Many include a "Remember Me" checkbox to keep users logged in across sessions.
         Accessibility: They often feature "Forgot Password?" 
         links and options to sign in via third-party accounts like Google or Facebook.
        </pre></h3><br><br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
                        <a href ="{url_for('welcome')}">BACK</a>
         '''
    return redirect(url_for("welcome"))


@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("home"))
