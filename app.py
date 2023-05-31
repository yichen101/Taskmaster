from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # Creates Flask instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # Add config, telling app where database is located
db = SQLAlchemy(app) # Initialise database

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    deadline = db.Column(db.String(20)) # db.Date causing issue
    priority = db.Column(db.String(10))

    def __repr__(self):  # Return string when new element created
        return '<Task %r>' % self.id
    
    
@app.route('/', methods=['POST','GET']) # This route accepts two methods, can send data to database
def index():
    if request.method == 'POST':
        task_content = request.form['content'] # Input of form where id='content'
        task_deadline = request.form['deadline']
        task_priority = request.form['priority']
        new_task = Todo(content=task_content, deadline=task_deadline, priority=task_priority)

        try:
            db.session.add(new_task) #Add task to database
            db.session.commit()
            return redirect('/')
        except:
            return 'Error with adding task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() #Get data from database
        return render_template('index.html', tasks=tasks)
    

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Error with deleting task'

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    
    if request.method == 'POST':
        task.content = request.form['content']
        task.deadline = request.form['deadline']
        task.priority = request.form['priority']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Error with updating task'
        
    else:
        return render_template('update.html', task=task)   

if __name__ == "__main__":
    app.run(debug=True)
