from flask import Flask, request, jsonify, render_template
import requests
import json
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('upload.html')

stored_circle_data = []


@app.route('/process_circles/', methods=['POST'])
def process_circles():
    global stored_circle_data
    data = request.get_json()
    stored_circle_data = data.get('circles', [])
    return jsonify({'success': True})

@app.route('/show_graph/')
def show_graph_view():
    global stored_circle_data
    return render_template('show_graph.html', circles=json.dumps(stored_circle_data))

"""
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], f'test{filename[-4:]}')
        file.save(file_path)
        return f'File successfully uploaded: {file_path}', 200
    return 'Invalid file type', 400
"""

"""
@app.route('/process', methods=['POST'])
def process():
    try:  # GET INFORMATION FROM OTHER RUNNING FILE (PROCESS.PY)
        response = requests.get('http://process:8000')
        return jsonify({'message': response.text}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
"""

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=5000)
