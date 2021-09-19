from flask import *
import pandas as pd
from werkzeug.utils import secure_filename
import os
import business

app = Flask(__name__)

UPLOAD_PATH = 'static/'

FILE_NAME = 'user-feedback.csv'

@app.route('/')
def start():

    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_files():

    uploaded_file = request.files['file']

    filename = secure_filename(uploaded_file.filename)

    fileext = filename.split('.')[-1]

    if filename != '' and fileext == 'csv':

        uploaded_file.save(os.path.join(UPLOAD_PATH, FILE_NAME))

    else:

        return "Please send CSV File", 500

    return '', 204

@app.route('/home')
def home():

    content_col = request.values.get('content_col')

    business.process()

    result = {
        'content_col' : content_col
    }

    return render_template('index.html', result = result)

@app.route('/top/<state>')
def home(state):

    if state == 'positive':

        df_positive = pd.read_csv('static/positive.csv')

        df_positive = df_positive[:10]

        return render_template('table.html',tables=[df_positive.to_html(classes='female')],
                titles = ['positive reviews'])

    if state == 'negative':

        df_negative = pd.read_csv('static/negative.csv')

        df_negative = df_negative[:10]

        return render_template('table.html',tables=[df_negative.to_html(classes='male')],
                titles = ['negative reviews'])

    return 'the hell man'


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
