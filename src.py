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