import pandas as pd;
import random

argdict={'percentage':None,'data_location':None,'data':None,'savename':None,'missingindexset':None,'mvnum':None}

def mvgenerator(argdict):
    preinputs(argdict);
    generator(argdict);
    data=argdict['data'];
    savename=input("Please provide path and file name with extensionto save datasheet : ")
    if savename=="":data.to_csv("FinalDatasheet.csv");
    else:data.to_csv(savename)
    print(data.isnull().sum().sum())
    
def preinputs(argdict):
    percentage=float(input("Please provide percentage of data you want missing : "));
    data_location=input("Enter location of data with file exensions : ");
    argdict.update([('percentage',percentage),('data_location',data_location)]);
   
def generator(argdict):
    percentage=argdict['percentage'];
    data=pd.read_csv(argdict['data_location']);
    shape=list(data.shape);
    mvnum=int(percentage*shape[0]*shape[1]//100);
    column=data.columns;
    i=1;missingset=set();
    while (i<=mvnum):
        row=random.randint(0,shape[0]-1);
        columnindex=random.randint(0,shape[1]-1);
        if (row,columnindex) in missingset:i=i-1;
        else:
            data[column[columnindex]][row]=None;
            missingset.update({(row,columnindex)});
        i=i+1;
    argdict.update([('missingindexset',missingset),('mvnum',mvnum),('data',data)])

mvgenerator(argdict)