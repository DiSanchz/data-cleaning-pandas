import pandas as pd
import numpy as np
import re

def row_nan_out(x,y):
    #this function eliminate all rows of a dataframe for which a given column's value is null
    #argument "x" is supposed to capture the df's name and "y" the name of the refference column
    #if the function does not find null values in the specified column it returns nothing
    x_nans = x[y].isna()
    
    for i in x_nans:
        if i == True:
            print("Se encontaron valores nulos a eliminar en los datos.")
            for j in range(0, len(x_nans)):
                if x_nans[j] == True:
                    x.drop(j, axis=0, inplace=True)
            return x

        else:
            pass
    return x
    #piensa en incluir algo de programación defensiva y gestion de errores para que-
    #-la función te quede niquelada

def first_year(x):
    #this function returns the first chain of four digits it encounters in a string (e.g. a year)
    
    y = re.search("\d{4}", str(x))
    if type(y) != type(None):
        return y.group()
    else:
        return np.nan


def index_b_count(w, x, v, h):
    #return a dictionary containing the ratio between the count of two given categorical variables for the rows of a df
    #whose index has a given value as value, and the index of refference of the dataframe as key
    #Where w is a dataframe, x is a list of indices, v is the column that will serve as basis for the count
    #and h is the column from which the values making up x have been taken
    emptydict = {}
    
    
    for i in x:
        w_temp = w[w[h] == i]
        if len(w_temp[v].value_counts().value_counts()) > 1:
            a = len(w_temp[v])
            b = w_temp[v].value_counts()[1]
            c = b/a
            emptydict[i] = c
        else:
            emptydict[i] = 0
            
    
    return emptydict

def gdp_points(x):
    #function that returns the desired gdp score
    return (x*100)/110000