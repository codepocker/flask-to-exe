
from flask import Flask, request
import webview


app = Flask(__name__)
window = webview.create_window('CodePocker!', app)

@app.route('/', methods=['GET', 'POST'])
def get_name():
    if request.method == 'POST':
        name = request.form['name']
        return 'Hello %s' % name
    return '''
    <form method="POST">
        <input type="text" name="name" placeholder="Enter Your Name" />
        <input type="submit" />
    </form>
    '''

if __name__ == '__main__':
    #app.run(debug=True)
    webview.start()


