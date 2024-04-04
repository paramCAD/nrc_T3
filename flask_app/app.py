from flask import Flask, send_file, render_template
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download_file():
    """
    Download the contents of data.csv file.
    ---
    responses:
      200:
        description: OK
        content:
          text/csv:
            schema:
              type: string
              example: "id,name,age\n1,John,30\n2,Susan,25"
    """
    filename = 'data.csv'
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
