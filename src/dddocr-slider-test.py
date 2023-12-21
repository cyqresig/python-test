import ddddocr

det = ddddocr.DdddOcr(det=False, ocr=False)

# with open('target.png', 'rb') as f:
with open('target-slider-tx.png', 'rb') as f:
    target_bytes = f.read()

with open('background-slider-tx.png', 'rb') as f:
    background_bytes = f.read()

res = det.slide_match(target_bytes, background_bytes)

print(res)