import cv2
import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from qr_extraction import extract_qr_codes

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filename = secure_filename(file.filename)
        file_path = f"{app.config['UPLOAD_FOLDER']}/{filename}"
        file.save(file_path)
        qr_codes = extract_qr_codes(file_path)
        return f"QR Codes found: {', '.join(qr_codes)}"


if __name__ == '__main__':
    app.run(debug=True)
