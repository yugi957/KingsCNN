from flask import Flask, request, send_file, jsonify
from PIL import Image
import io
from eye_utils import *

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    file = request.files['image']
    image = Image.open(file.stream)
    # Process your image here using your Python code
    processed_image = to_FEN(image)
    # Assuming processed_image is a PIL Image object
    if(isinstance(processed_image, list)):
        return jsonify(processed_image)

    img_io = io.BytesIO()
    processed_image.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.route('/debug-corners', methods=['POST'])
def debug_corners():
    file = request.files['image']
    image = Image.open(file.stream)
    # Process your image here using your Python code
    processed_image = to_FEN(image, debug='corners')
    # Assuming processed_image is a PIL Image object
    img_io = io.BytesIO()
    processed_image.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.route('/debug-pieces', methods=['POST'])
def debug_pieces():
    file = request.files['image']
    image = Image.open(file.stream)
    # Process your image here using your Python code
    processed_image = to_FEN(image, debug='pieces')
    # Assuming processed_image is a PIL Image object
    img_io = io.BytesIO()
    processed_image.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True)