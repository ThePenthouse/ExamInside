from flask import Flask, session, redirect, url_for, request, render_template, jsonify, flash
from flask_mysqldb import MySQL


app = Flask(__name__)


app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'rootroot'
app.config['MYSQL_DB'] = 'examinside'
app.secret_key = 'aks64_hsc'

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template('home.html', title='Welcome')


@app.route("/home")
def home():
    return render_template('home.html', title='Welcome')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html', title='Gallery')


@app.route("/feedback")
def feedback():
    return render_template('feedback.html', title='Feedback')


@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')


@app.route("/tclogin",)
def tclogin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM examinside.user")
    data = cur.fetchall()
    return render_template('tclogin.html', data= data, title='Welcome')


@app.route('/tclogin', methods = ['GET', 'POST'])
def teacherlogin():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        email = request.form['email']
        password = request.form['password']
        cur.execute("SELECT * from user where Email = %s and Password = %s", (email, password))
        current_user = cur.fetchone()
        if not current_user:
            flash('Invalid email or password!', 'error')
        else:
            session['User_id'] = current_user[0]
            session['Username'] =  current_user[1]
            session['Email'] = current_user[2]
            session['Contact'] =  current_user[4]
            session['Profile_pic'] =  current_user[5]
            flash('Logged in as %s' % session['Email'])
            return redirect(url_for('tchome'))

    return render_template('tclogin.html', title='Login')



@app.route('/tcsignup', methods = ['GET', 'POST'])
def tcsignup():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        Email = request.form['Email']
        Password = request.form['Password']
        Username = request.form['Username']
        Contact = request.form['Contact']
        Profile_pic = request.form['Profile_pic']
        cur.execute("SELECT * from user where Email = %s and Password = %s", (Email, Password))
        current_user = cur.fetchone()
        if not current_user:
            cur.execute("INSERT INTO user(Username, Email, Password, Contact, Profile_pic) VALUES(%s, %s, %s, %s, %s)", (Username, Email, Password, Contact, Profile_pic))
            mysql.connection.commit()
            cur.close()
            flash('Account created successfully!', 'success')
            return redirect(url_for('tclogin'))
        else:
            session['User_id'] = current_user[0]
            session['Username'] = current_user['Username']
            session['Email'] =  current_user[2]
            session['Password'] =  current_user[3]
            session['Contact'] = current_user[4]
            session['Profile_pic'] = current_user[5]
            flash('Logged in as %s' % session['Email'])
            flash('This email is already registered!')
            return redirect(url_for('tchome'))

    return render_template('tcsignup.html', title='Sign Up')


@app.route("/tchome", methods=['GET', 'POST'])
def tchome():
    if request.method == "POST":
        details = request.form
        ques = details['ques']
        option1 = details['option1']
        option2 = details['option2']
        option3 = details['option3']
        option4 = details['option4']
        ans = details['ans']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO question(ques, option1, option2, option3, option4, ans) VALUES (%s, %s, %s, %s, %s, %s)", (ques, option1, option2, option3, option4, ans))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('exam'))
    return render_template('tchome.html', title='Questions')


@app.route("/teacherques", methods=['GET', 'POST'])
def teacherques():
    if request.method == "POST":
        details = request.form
        ques = details['ques']
        option1 = details['option1']
        option2 = details['option2']
        option3 = details['option3']
        option4 = details['option4']
        ans = details['ans']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO question(ques, option1, option2, option3, option4, ans) VALUES (%s, %s, %s, %s, %s, %s)", (ques, option1, option2, option3, option4, ans))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('exam'))
    return render_template('teacherques.html', title='Questions')



@app.route('/question', methods=['GET', 'POST'])
def getteacherques():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM examinside.question")
    return jsonify(data=cur.fetchall())



@app.route('/exam', methods=['GET', 'POST'])
def exam():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from examinside.question")
    data = cur.fetchall()
    return render_template('exam.html', data= data, title='Exam')


@app.route("/stlogin",)
def stlogin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM examinside.user")
    data = cur.fetchall()
    return render_template('stlogin.html', data= data, title='Welcome')


@app.route('/stlogin', methods = ['GET', 'POST'])
def studentlogin():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        email = request.form['email']
        password = request.form['password']
        cur.execute("SELECT * from user where Email = %s and Password = %s", (email, password))
        current_user = cur.fetchone()
        if not current_user:
            flash('Invalid email or password!', 'error')
        else:
            session['User_id'] = current_user[0]
            session['Username'] =  current_user[1]
            session['Email'] = current_user[2]
            session['Contact'] =  current_user[4]
            session['Profile_pic'] =  current_user[5]
            flash('Logged in as %s' % session['Email'])
            return redirect(url_for('sthome'))

    return render_template('stlogin.html', title='Login')



@app.route('/stsignup', methods = ['GET', 'POST'])
def stsignup():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        Email = request.form['Email']
        Password = request.form['Password']
        Username = request.form['Username']
        Contact = request.form['Contact']
        Profile_pic = request.form['Profile_pic']
        cur.execute("SELECT * from user where Email = %s and Password = %s", (Email, Password))
        current_user = cur.fetchone()
        if not current_user:
            cur.execute("INSERT INTO user(Username, Email, Password, Contact, Profile_pic) VALUES(%s, %s, %s, %s, %s)", (Username, Email, Password, Contact, Profile_pic))
            mysql.connection.commit()
            cur.close()
            flash('Account created successfully!', 'success')
            return redirect(url_for('stlogin'))
        else:
            session['User_id'] = current_user[0]
            session['Username'] = current_user['Username']
            session['Email'] =  current_user[2]
            session['Password'] =  current_user[3]
            session['Contact'] = current_user[4]
            session['Profile_pic'] = current_user[5]
            flash('Logged in as %s' % session['Email'])
            flash('This email is already registered!')
            return redirect(url_for('sthome'))

    return render_template('stsignup.html', title='Sign Up')


@app.route('/sthome', methods=['GET', 'POST'])
def sthome():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from examinside.question")
    data = cur.fetchall()
    return render_template('sthome.html', data= data, title='Exam')


@app.route('/logout')
def logout():
    session.pop('User_id', None)
    session.pop('Username', None)
    session.pop('Email', None)
    session.pop('Contact', None)
    session.pop('Profile_pic', None)
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)






