from flask import *
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_PATH = 'static/'

FILE_NAME = 'user-feedback.csv'

@app.route('/')
def start():

    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_files():

    uploaded_file = request.files['file']

    filename = secure_filename(uploaded_file.filename)

    fileext = filename.split('.')[-1]

    if filename != '' and fileext == 'csv':

        uploaded_file.save(os.path.join(UPLOAD_PATH, filename))

    else:

        return "Please send CSV File", 500

    return '', 204

@app.route('/home')
def home():

    content_col = request.values.get('content_col')

    result = {
        'content_col' : content_col
    }

    return render_template('index.html', result = result)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
