from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image # for reading image files
from webcolors import rgb_to_hex


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/uploader", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        my_img = Image.open(f.filename)
        img_array = np.array(my_img)
        colors, count = np.unique(img_array.reshape(-1, img_array.shape[-1]), axis=0, return_counts=True)
        ten_colors = colors[np.argsort(-count)][:10]
        color_list = []
        hex_list = []
        for x in range(10):
            color_tuple = tuple(ten_colors[x])
            color_list.append(color_tuple)
        for i in range(len(color_list)):
            hex = rgb_to_hex(color_list[i])
            hex_list.append(hex)
        return render_template("image.html", colors=hex_list, img=f.filename)












if __name__ == '__main__':
    app.run(debug=True)















