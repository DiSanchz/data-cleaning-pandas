def row_nan_out(x,y):
    #this function eliminate all rows of a dataframe for which a given column's value is null
    #argument "x" is supposed to capture the df's name and "y" the name of the refference column
    x_nans = x[y].isna()
    
    if "True" in x_nans:
        print("Se encontaron valores nulos a eliminar en los datos.")
        for i in range(0, len(x_nans)):
            if x_nans[i] == True:
                x.drop(i, axis=0, inplace=True)
        return x

    else:
        print("No se encontraron valores nulos en los datos proporcionados.")
        return x