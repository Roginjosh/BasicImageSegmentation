from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np
import matplotlib.pyplot as plt

NUM_SAMPLES = 100
data = np.random.normal(loc=1, scale=1, size=NUM_SAMPLES)
bins = np.linspace(data.min(), data.max(), 33)
x_pos = np.digitize(data, bins[1:-1])  

data = np.random.normal(loc=1, scale=1, size=NUM_SAMPLES)
bins = np.linspace(data.min(), data.max(), 33)  
y_pos = np.digitize(data, bins[1:-1])  

data = np.random.normal(loc=1, scale=1, size=NUM_SAMPLES)
bins = np.linspace(data.min(), data.max(), 10) 
rad = np.digitize(data, bins[1:-1]) 

samples = np.array([x_pos, y_pos, rad+1])

if len(os.listdir(os.path.join('data'))) == 0:    
    for i in range(samples.shape[1]):
        [x,y,r] = samples[:,i]
    # Create a blank white image
        img = Image.new('RGB', (32, 32), color='white')
        draw = ImageDraw.Draw(img)

        # Draw a rectangle and some text
        draw.circle([x,y], r, fill='red', outline='red')

        name = f'Image_{i+1}_{x}_{y}__{r}.png'
        # Save the image
        img.save(os.path.join('data', name))
else:
    print("Not going to create more data.")