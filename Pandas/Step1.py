import pandas as pd

df=pd.read_csv('pokemon_data.csv')
# df_xlsx=pd.read_excel('pokemon_data.xlsx')
#                                     #Definimos el delimitador
# df_txt=pd.read_csv('pokemon_data.txt',delimiter='\t')
# print(df.head(3)) #show the 3 first rows
# print(df.tail(3)) #show the  3 last row
# print(df_xlsx.head(10))
# print(df_txt.head(4))
#Read the Columns Files
#print(df.columns)
#Read a particular column
# print(df["Name"])
# print(df["Name"][0:5])
#print(df.Name) 
#List of Columns
#print(df[["Name","Type 1","HP"]])
#print a particular row
#print(df.iloc[2:4])
#print a particular row and column, like a name
#print(df.iloc[2,1])
#Iterate rows 
# for index, row in df.iterrows():
#     print(index,row["Name"])
#Look a particular data  in an Column
#print(df.loc[df['Name']=="Bulbasaur"])

#Sort Values
#print(df.sort_values('Name'))
#print(df.sort_values('Name',ascending=False))#De esta manera ordenara de manera descendente, esto es porqe por defecto ordena de manera ascendente
#print(df.sort_values(['Type 1','HP']))
#print(df.sort_values(['Type 1','HP'],ascending=[1,0]))#De esta manera ordena de forma ascendente Type 1 y Descendente HP
#Adding a Column(Agregamos una nueva columna al DataFrame)
# df["Total"]=df["HP"]+df["Attack"]+df["Defense"]+df["Sp. Atk"]+df["Sp. Def"]+df["Speed"]
# print(df.head(6))
# #Borrar Columnas
# df=df.drop(columns=['Total','Legendary'])
# print(df.head(5))
#Crear una nueva columna como la anterior pero de otra                                                                                                                                     Eje
# df["Total"]=df.iloc[:,4:10].sum(axis=1)#Le decimos que sume todos los valoes de la columna 4 a la 9, luego le especificamos la opracion a realizar, en este caso es una suma, y le decimos Axis=1 que seria que el resultado lo devuelva en una columna
# #Reoridenar las columnas de otra manera, para ello podemos pasar el nombre de las columnas a una lista y posteriormente jugamos como queramos con esta lista
# cols=list(df.columns)
# print(df[cols[0:4]+[cols[-1]]+cols[4:12]])
# #Pasamos nuestro DF modificado a un CSV
# #df.to_csv('Modified.csv',index=False)
# #df.to_excel('Modified.xlsx',index=False)
# df.to_csv('Modified.txt',index=False,sep='\t')#sep='\t' esto significa que separe por espacios en vez de por ejemplo por coma o por puntos y comas
#Filtering Data
# new_df=df.loc[(df['Type 1']=="Fire") &(df['Type 2']=="Flying") & (df['Speed']> 90)]
# #new_df.to_csv('new_df.txt',index=False,sep='\t')
# #Resetear Index en caso de que querramos redcir en numero de Rows o algo por el estilo
# new_df=new_df.reset_index()
# new_df.to_csv('new_df(IndexReset).txt',sep='\t')
#Filtrar por ejemplo campos que contengan ciertos caracteres como la funcion Like de  SQL
# new_df_like=df.loc[df['Name'].str.contains('Mega')]
# new_df_like=df.loc[~df['Name'].str.contains('Mega')] #Le decimos que no nos filtre los Name que contengan Mega
# print(new_df_ike)

#Modificar registros en el DF
# df.loc[df['Type 1']=='Fire','Type 1'] = 'Flamer' #Le decimos que cuando aparezca el valor de Fire en el campo Type 1 lo remplace por Flamer
# df.loc[df['HP']>60,['Generation','Legendary']]='TEST VALUE'#Le decimos que cambie el valor de varios campos
# df.loc[df['HP']>60,['Generation','Legendary']]=['Test 1','Test 2']
# print(df)
#Agregation Functions
#average=df.groupby(['Type 1']).mean()#De esta manera nos da el promedi de todos los campos con valores numericos
average=df.groupby(['Type 1']).count()
average2=df.groupby(['Name']).mean().sort_values('HP')
print(average)
