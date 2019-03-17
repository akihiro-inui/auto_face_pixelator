import os
import io
import numpy as np
import cv2
import jsonpickle
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response, helpers
from image_process import mosaic
from werkzeug import secure_filename


app = Flask(__name__)

UPLOAD_FOLDER = './images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'PNG', 'JPG'])
IMAGE_WIDTH = 640
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        img_file = request.files['img_file']

        # Exception
        if img_file and allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
        else:
            return ''' <p>This file format is not currently supported</p> '''

        # Read image as binary
        f = img_file.stream.read()
        bin_data = io.BytesIO(f)
        file_bytes = np.asarray(bytearray(bin_data.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # Small image
        raw_img = cv2.resize(img, (IMAGE_WIDTH, int(IMAGE_WIDTH*img.shape[0]/img.shape[1])))

        # Save raw(small) image
        #raw_img_url = os.path.join(app.config['UPLOAD_FOLDER'], 'raw_' + filename)
        #cv2.imwrite(raw_img_url, raw_img)

        # Apply mosaic effect
        mosaic_img = mosaic(raw_img)

        # Save modified image
        #mosaic_img_url = os.path.join(app.config['UPLOAD_FOLDER'], 'mosaic_' + filename)
        #cv2.imwrite(mosaic_img_url, mosaic_img)

        # build a response dict to send back to client
        #response = {'message': 'image received. data={}x{}'.format(mosaic_img.shape[1], mosaic_img.shape[0])}
        # encode response using jsonpickle

        img_crop_pil = Image.fromarray(mosaic_img)
        byte_io = io.BytesIO()
        img_crop_pil.save(byte_io, format="PNG")
        #byte_io.close()
        #img.save(buf, 'png')
        response = helpers.make_response(byte_io.getvalue())
        response.headers["Content-type"] = "Image"
        response_pickled = jsonpickle.encode(response)

        return Response(response=response_pickled, status=200, mimetype="application/json")


@app.route('/images/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.debug = True
    app.run(app.run(host='0.0.0.0', port=8000))
