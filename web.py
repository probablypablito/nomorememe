from flask import Flask, render_template, send_file, request
from io import BytesIO
from getImage import getImage
from makeMeme import generate_meme
import asyncio
app = Flask(__name__)

@app.route('/')
def index():
    query = request.args.get('image')
    if (query == None): return render_template('index.html')
    img_buffer = asyncio.run(getImage(query))
    meme = generate_meme(img_buffer, "NO MORE", query.upper().replace("_", " "))
    return send_file(BytesIO(meme), mimetype='image/jpeg')
    

@app.route('/<path:path>')
def serve_image(path):
    image = path.split('/')[0]
    image = image.upper().replace("_", " ")
    try:
        img_buffer = asyncio.run(getImage(image))
        meme = generate_meme(img_buffer, "NO MORE", image)
    except:
        logo = open("logo.png", "rb")
        logo_buffer = logo.read()
        logo.close()
        meme = generate_meme(logo_buffer, "", "[IMAGE NOT FOUND]")
    return send_file(BytesIO(meme), mimetype='image/jpeg')
    return image


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)