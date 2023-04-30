import pandas as pd;
import random

argdict={'percentage':None,'data_location':None,'column':None,'row':None,'data':None,'savename':None,'missingindexset':None,'mvnum':None}

def mvgenerator(argdict):
    preinputs(argdict)
    generator(argdict)
    data=argdict['data']
    savename=input("Please provide path and file name with extension to save datasheet : ")
    if savename=="":data.to_csv("FinalDatasheet.csv")
    else:data.to_csv(savename)
    print("Missing Values : ",data.isnull().sum().sum())
        
def preinputs(argdict):
    percentage=float(input("Please provide percentage of data you want missing (for specific cell provide 100 % ) : "))
    data_location=input("Enter location of data with file exensions : ")
    data=pd.DataFrame(pd.read_csv(data_location))
    column=False;row=False
    ask=input('Do you want to add missing values in any specific column or row ( Y / N ) : ').casefold()
    if ask=='y':
        exit=0
        while (exit==0):
            colrow=input("Please provide if you want use column or row \n[ 'col' : column / 'row' : row / 'exit' : exit options]: ").casefold()
            if colrow=='col':column=input("Please provide column name : ")
            elif colrow=='row':row=int(input("Please provide row number : "))
            elif colrow=='exit':exit=1
            else:print("Wrong Input")
    argdict.update([('percentage',percentage),('data_location',data_location),('data',data),('column',column),('row',row)])
    

def generator(argdict):
    percentage=argdict['percentage']
    data=argdict['data']
    shape=list(data.shape)
    if argdict['column'] ==False:column=argdict['column']
    else:column=argdict['column'];shape[1]=1
    if argdict['row']==False:row=argdict['row']
    else:row=argdict['row'];shape[0]=1
    columnlist=list(data.columns)
    mvnum=int(percentage*shape[0]*shape[1]//100)
    i=1;missingset=set()
    while (i<=mvnum):
        if argdict['row']!=False:row=argdict['row']
        else:row=random.randint(1,shape[0])
        if argdict['column']!=False:columnindex=columnlist.index(column);columnindex+=1
        else:columnindex=random.randint(1,shape[1])
        if (row,columnindex) in missingset:i=i-1
        else:
            data.loc[row-1,columnlist[columnindex-1]]=None
            missingset.update({(row,columnindex)})
        i=i+1
    print("Total data where missing values is getting generated : ",shape[0]*shape[1])
    argdict.update([('missingindexset',missingset),('mvnum',mvnum),('data',data)])
    print(missingset)

mvgenerator(argdict)
