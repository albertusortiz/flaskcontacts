from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Connection
app.config['MYSQL_HOST'] = '162.241.61.214'
app.config['MYSQL_USER'] = 'albertus_flask'
app.config['MYSQL_PASSWORD'] = 'rVccaiW6PNPpzXD'
app.config['MYSQL_DB'] = 'albertus_flaskcontacts'
mysql = MySQL(app)

# Session
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(fullname)
        print(phone)
        print(email)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact Added Successfully')
        return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
    return 'Edit Contact'

@app.route('/delete')
def delete_contact():
    return 'Delete Contact'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)