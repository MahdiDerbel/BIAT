import pandas as pd
import openpyxl
import uuid
file_obj = open("BIAT.txt", "r") #BEDEL ESM FICHIER HOUNI 
  

file_data = file_obj.read()
  

lines = file_data.splitlines()
file_obj.close()
df = pd.DataFrame()
list_date_valeur=[]
list_Libelle_operation=[]
list_Reference=[]
list_Date_opération=[]
list_Montant=[]
index=lines.index('Montant\t')+1
i=0
list=[i for i in lines[index].split('\t') if i]
while index<len(lines)-3:
    if len(list)==5:
        list_date_valeur.append(list[0])
        list_Libelle_operation.append(list[1])
        list_Reference.append(list[2])
        list_Date_opération.append(list[3])
        list_Montant.append(list[4])
        i=i+1
        index=index+1
        print(index)
        print(list_date_valeur)
        list = [j for j in lines[index].split('\t') if j]
    elif len(list)==2:
        list_Libelle_operation.append(list[0])
        list_Montant.append(list[1])
        list_Reference.append('Nan')
        list_Date_opération.append('Nan')
        list_date_valeur.append(list[0])
        i=i+1
        index=index+1
        list = [j for j in lines[index].split('\t') if j]
        
            
    elif len(list)==1:
        if len(list_Libelle_operation)>=1:
            
            value=list_Libelle_operation[-1]+list[0]
            list_Libelle_operation.pop()
            list_Libelle_operation.append(value)
            index=index+1
            list = [j for j in lines[index].split('\t') if j]
            
        else:
            list_Libelle_operation.append(list[0])
            index=index+1
            list = [j for j in lines[index].split('\t') if j]
            
    elif len(list)==0:
        index=index+1
        i=i+1
        list = [j for j in lines[index].split('\t') if j]
print(list_Montant)
print(list_Date_opération)
print(list_Reference)
print(list_Libelle_operation)
print(list_date_valeur)
df.insert(0, "Montant",list_Montant,allow_duplicates=True)
df.insert(0, "Date opération",list_Date_opération,allow_duplicates=True)
df.insert(0, "Référence",list_Reference,allow_duplicates=True)
df.insert(0, "Libelle operation",list_Libelle_operation,allow_duplicates=True)
df.insert(0, "Date valeur", list_date_valeur,allow_duplicates=True)

filename='{}.xlsx'.format(uuid.uuid1())
df.to_excel(filename)
