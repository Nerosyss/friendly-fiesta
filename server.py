from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    # serves css, js, images from project root and subfolders
    directory = os.path.dirname(filename)
    # if path includes a folder, let send_from_directory handle it
    if '/' in filename or '\\' in filename:
        parts = filename.replace('\\', '/').split('/')
        return send_from_directory(os.path.join(*parts[:-1]), parts[-1])
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500, debug=True)
