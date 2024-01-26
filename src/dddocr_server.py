import importlib
import uvicorn
from fastapi import FastAPI, Query

dddocr_slider = importlib.import_module("dddocr-slider")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/dddocr-slider")
async def server2(bg=Query(None), target=Query(None)):
    # return {
    #     bg,
    #     target
    # }
    [x1, y1, x2, y2] = dddocr_slider.ocr_slider(bg, target)
    return {
        'x1': x1,
        'y1': y1,
        'x2': x2,
        'y2': y2
    }

# test
# http://127.0.0.1:8080/dddocr-slider?bg=/Users/chenyiqin/work/maoyan/projects/hotevents/captchaImages/slider-2/background/0279050000d008480000000bb947d63e46b5.png&target=/Users/chenyiqin/work/maoyan/projects/hotevents/captchaImages/slider-2/sprite-target/0279050000d008480000000bb947d63e46b5.png

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
