from quart import Quart, render_template, send_file, request
from io import BytesIO
from getImage import getImage
from makeMeme import generate_meme
import asyncio
app = Quart(__name__)

@app.route('/')
async def index():
    return await render_template('index.html')
    

@app.route('/<path:path>')
async def serve_image(path):
    image = path.split('/')[0]
    image = image.upper().replace("_", " ")
    
    search = request.args.get("q") 
    
    query = search.replace("_", " ") if search else image 

        
    try:
        img_buffer = await getImage(query)
        meme = await generate_meme(img_buffer, "NO MORE", image)
    except Exception as e:
        print(f"An error occurred: {e}")
        logo = open("error.png", "rb")
        logo_buffer = logo.read()
        logo.close()
        meme = logo_buffer
    return await send_file(BytesIO(meme), mimetype='image/jpeg')