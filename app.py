from flask import Flask, send_file, render_template, jsonify
from tester import test_download_endpoint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download_file():
    filename = 'data.csv'
    return send_file(filename, as_attachment=True)

@app.route('/test', methods=['GET'])
def test_endpoint():
    result = test_download_endpoint()
    if result['status'] == 'success':
        return send_file('downloaded_file.csv', as_attachment=True)
    else:
        return jsonify(result), 400

if __name__ == '__main__':
    app.run(debug=True)
