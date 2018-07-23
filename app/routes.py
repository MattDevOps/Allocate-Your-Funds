@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template('index.html', title='Home Page')
