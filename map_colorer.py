from scipy import misc
import tkFileDialog as tk
import pandas as pd

def main():
	print('Choose an image to analyze.')
	filename = tk.askopenfilename()

	input_map = misc.imread(filename)

	image_df = build_image_df(input_map)

def build_image_df(image):
	df = pd.DataFrame( index=range(len(image)), columns=range(len(image[0])) )
	for i in df.index:
		df.loc[i] = [ (r,g,b,a) for r,g,b,a in image[i] ]
	return df

if __name__ == '__main__':
	main()