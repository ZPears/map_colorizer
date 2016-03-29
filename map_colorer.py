from scipy import misc
import tkFileDialog as tk
import pandas as pd
import numpy as np
import distance_calculator as dc

def main():
	print('Choose an image to analyze.')
	filename = tk.askopenfilename()

	input_map = misc.imread(filename)

	image_df = build_image_df(input_map)

	destination_coords = [ int(np.mean(image_df.index)), int(np.mean(image_df.columns)) ]

def build_image_df(image):
	df = pd.DataFrame( index=range(len(image)), columns=range(len(image[0])) )
	for i in df.index:
		df.loc[i] = [ (r,g,b) for r,g,b,a in image[i] ]
	return df

def recalc_pixels(image_df, ):
	for i in image_df.index:
		for j in image_df.columns:


if __name__ == '__main__':
	main()