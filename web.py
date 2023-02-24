from flask import Flask, render_template, send_file, request
from io import BytesIO
from getImage import getImage
from makeMeme import generate_meme
app = Flask(__name__)

@app.route('/')
def serve_image():
    query = request.args.get('image')
    img_buffer = getImage(query)
    meme = generate_meme(img_buffer, "NO MORE", query.upper().replace("_", " "))
    return send_file(BytesIO(meme), mimetype='image/jpeg')
