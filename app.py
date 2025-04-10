# from flask import Flask, render_template

# app = Flask(__name__, 
#             template_folder='app/templates',
#             static_folder='app/static')

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# 주석을 추가
# 텍스트 



from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')