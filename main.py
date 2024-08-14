from flask import Flask,render_template , request, redirect, url_for


app = Flask(__name__)
app.config['SECRET_KEY']='649F34JD75SW7TX3843T25'


todos = []

@app.route('/')
def home():
    return render_template("index.html", todos = todos)

@app.route('/add', methods =['POST'])
def add_todo():
    todo_item = request.form.get('todo')
    if todo_item:
        todos.append(todo_item)
    return redirect(url_for('home'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_todo(index):
    if 0 <= index <len(todos):
        todos.pop(index)
    return redirect(url_for('home'))


if __name__=='__main__':
    app.run(debug=True, port=5002)