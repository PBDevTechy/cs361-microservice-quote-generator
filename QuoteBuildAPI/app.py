from flask import Flask, request, jsonify

app = Flask(_name_)

# home page
@app.route('/')
def home():
    return "QuoteBuild API is running..."

# starter 
@app.route('/generate-quote')
def generate_quote():
    return "Quote route working."

# run
if __name__ == 'main';
    app.run(debug=True)
