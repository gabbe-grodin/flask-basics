from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('index.html')

# def index():
#     return render_template("index.html", phrase="hello", times=5)

# @app.route('/success')
# def success():
#     return "success"


# @app.route('/hello/<name>')
# def hello(name):
#     print(name)
#     return "Hello, " + name

# @app.route('/users/<username>/<id>')
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id

# @app.route('/hello/<name>/<int:num>') 
# def hello_again(name, num):
#     # return f"Hello, {name * num}"
#     return render_template("hello.html",name=name,num=num)

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)



if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8000)

