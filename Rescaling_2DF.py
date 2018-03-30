import pandas as pd


class rescaling_df:
    def __init__(self):
        pass
    
    # Перевод из одного масштаба в другой
    def rescale(self,X,A,B,C,D,force_float=False):
        retval = ((float(X - A) / (B - A)) * (D - C)) + C
        return retval


    # Масштабирование и объединение
    # Масштабирование производится по первому столбцу каждого DataFrame. В итоговом DataFrame масштаб из df2
    def rescale_df(self, df1, df2):

        df1.iloc[:,0] = df1.iloc[:,0].apply(lambda x: self.rescale(x, df1.iloc[:,0].min(), df1.iloc[:,0].max(), df2.iloc[:,0].min(), df2.iloc[:,0].max()))
        df1.set_index(df1.columns[0], inplace = True)
        df2.set_index(df2.columns[0], inplace = True)
        ind = df2.index
        fin = df2.merge(df1, left_index=True, right_index=True, how = 'outer').interpolate()
        fin = fin.loc[ind, :]
        fin.reset_index(inplace = True)

        return fin
    
