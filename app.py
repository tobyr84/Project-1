from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

#changed to the template for local host v2.0

#update from work 2.0

@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run()

