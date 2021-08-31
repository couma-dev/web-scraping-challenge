from flask import Flask, jsonify, render_template, redirect


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")

def welcome():
    """List all available api routes."""
    return (
      
    )

if __name__ == '__main__':
    app.run(debug=True)