import sys
import os 

from PIL import Image

images = []
filepaths = []
dir = "images"

filenames = os.listdir(dir)
for filename in filenames:
    filepaths.append(os.path.join(dir, filename))

for img in filepaths:
    images.append(Image.open(img))

images[0].save(
    "Rocco.gif", save_all=True, append_images=[images[1]], duration=350, loop=0
    )
    