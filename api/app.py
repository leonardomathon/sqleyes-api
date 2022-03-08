from flask import Flask, request

from sqleyes.main import main

app = Flask(__name__)

@app.errorhandler(404)
def error_404(e):
    return '<h1>404 Route not found</h1>', 404

@app.route('/')
def index():
    return '<h1>SQLEyes API server</h2>'

@app.route('/analyze', methods=['POST'])
def analyze_query():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        query = request.json['query']

        # Run detector
        return repr(main(query)), 201
        
    else:
        return 'Content-Type not supported!'
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)