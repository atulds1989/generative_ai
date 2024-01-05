#this app is for index.html

# from flask import Flask, render_template, send_file

# app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# @app.route('/get_image')
# def get_image():
#     image_path = r'C:\Users\hp\OneDrive\Pictures\Screenshots\asura.jpg'
#     return send_file(image_path, mimetype='image/jpeg')

# # if __name__ == '__main__':
# #     app.run(debug=True)




###########################
#this app is for home.html and result.html
    
from flask import Flask, render_template, request, send_file, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/process_image')
def process_image():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            image.save('static/' + image.filename) 

            return render_template('result.html', image_filename=image.filename)
        else:
            return "No image provided in the form."

@app.route('/get_image/<image_filename>')
def get_image(image_filename):
    return send_file('static/' + image_filename, mimetype='image/jpeg')
    

if __name__ == '__main__':
    app.run(debug=True)
