from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from database import db, User, initialize_db
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
upload_folder = os.path.join('static', 'images')

if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)
    
app.config['UPLOAD_FOLDER'] = upload_folder
initialize_db(app)

def allowed_file(filename):
    return '.' in filename

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', data=users)

@app.route('/user', methods=['POST'])
def addUser():
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']
    image_blob = None  # Inicializar a None

    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            filename = secure_filename(image.filename)
            uploaded_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(uploaded_path)
            with open(uploaded_path, 'rb') as file:
                image_blob = file.read()
    else:
        filename = None

    date_column = datetime.now()
    numeric_column = request.form.get('peso')

    if username and name and password:
        new_user = User(
            username=username,
            name=name,
            password=password,
            image_filename=filename,
            image_blob=image_blob,
            numeric_column=numeric_column,
            date_column=date_column
        )
        db.session.add(new_user)
        db.session.commit()

    return redirect(url_for('home'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    user_to_edit = db.session.query(User).get(id)
    
    if user_to_edit:
        if request.method == 'POST':
            user_to_edit.username = request.form['username']
            user_to_edit.name = request.form['name']
            user_to_edit.password = request.form['password']
            user_to_edit.numeric_column = request.form.get('peso')
            db.session.commit()
            return redirect(url_for('home'))

    return render_template('index.html', data=User.query.all())

@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete = User.query.get(id)
    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)
