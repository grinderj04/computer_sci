# -*- coding: utf-8 -*-
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)
  
# Create figure with 2 subplots
fig, ax = plt.subplots(1, 3)
# Show the image data in the first subplot
ax[0].imshow(img)
ax[2].imshow(img)
ax[1].imshow(img, interpolation='none') # Override default
ax[0].set_xlim(35, 45)
ax[0].set_ylim(80, 70)
ax[1].set_xlim(45, 55)
ax[1].set_ylim(80, 70)
ax[2].set_xlim(54, 65)
ax[2].set_ylim(80, 70)
# Show the figure on the screen
fig.show()
