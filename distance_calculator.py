from scipy import misc
import tkFileDialog as tk
import pandas as pd

def find_nearest_road(image_df, row_index, col_index, max_row, max_col, destination):
	# check if min row is too small
	col_index -= 1 if col_index != 0 else col_index
	row_index -= 1 if row_index != 0 else row_index 
	# check if max row is too large
	max_row += 1 if max_row != len(image_df)-1 else max_row
	max_col += 1 if max_row != len(image_df.columns)-1 else max_col

	subset = image_df.loc[row_index:max_row, col_index,max_col]

	# check if min/max values include destination, quit if so
	# if destionation_row in rows range and destination_col in cols range, return destination
	elif find_non_zero_value(subset) == False:
		find_nearest_road(image_df, row_index, col_index, max_row, max_col, destination):
	else:
		return 

def find_non_zero_value(subset):
	subset = image_df.loc[min_row:max_row, min_col:max_col]
	if len(subset.loc[0,:].value_counts()) != 1:
		return 