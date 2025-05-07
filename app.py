from flask import Flask, render_template, request, send_file
from braillelogic import text_to_braille_images
import cv2
import numpy as np
import io
import base64

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    braille_data = []

    if request.method == 'POST':
        text = request.form.get('text')
        braille_images = text_to_braille_images(text)

        for char, img in braille_images:
            # Call Arduino communication function
            braille_pattern = get_braille_pattern_for_char(char.lower())
            send_braille_to_arduino(braille_pattern)

            # Encode image for web
            _, buffer = cv2.imencode('.png', img)
            image_encoded = base64.b64encode(buffer).decode('utf-8')
            braille_data.append({'char': char, 'image': image_encoded})

if __name__ == '__main__':
    app.run(debug=True)
