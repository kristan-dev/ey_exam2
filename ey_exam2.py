import pandas as pd
import numpy

def load_datagrid(data_as_csv):
  return pd.read_csv(data_as_csv)

def sort_dataframe(smaller_dataframe: pd.DataFrame):
  #NOTE: Sorts the dataframe's values in ascending order based on all columns
  smaller_2darray = smaller_dataframe.to_numpy()
  # smaller_2darray = smaller_2darray[smaller_2darray[:,0].argsort()]
  smaller_2darray = smaller_2darray [ :, smaller_2darray[1].argsort()]

  columns = list(smaller_dataframe.columns)
  sorted_dataframe = smaller_dataframe.sort_values(by=columns, ascending=True) # Sort dataframe by all columns

  return sorted_dataframe

def dissimilarity(dataframe:pd.DataFrame, row: int, column: int):
  smaller_dataframe = dataframe.iloc[0:row, 0:column] #NOTE: given col and row, get smaller 2d grid/ dataframe
  sorted_dataframe = sort_dataframe(smaller_dataframe=smaller_dataframe) #NOTE: use pandas to sort_values to sort contens by all columns
  return sorted_dataframe


if(__name__ == '__main__'):
  this_dataframe = load_datagrid(data_as_csv="datagrid.csv")
  # print(this_dataframe)
  new_dataframe = dissimilarity(dataframe=this_dataframe, row=10, column=4)
  # print(new_dataframe)
  pass