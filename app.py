from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/profile')
# def show_user_profile():
#     return render_template('inner-page.html')
        
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
