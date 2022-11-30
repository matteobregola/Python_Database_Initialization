# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 08:27:32 2022

@author: matte
"""


class db_init:
    
    mode=None
    source=None
    destination=None
    
    def __init__(self):
        print("Class intialized...")
    
    def setbase(self,mode,source,destination):
        self.setmode(mode)
        self.setsource(source)
        self.setdestination(destination)
        
        
    def __setmode(self,mode):
        """
            Possible modes:
                txt
                csv
                url
                input
        """
        mode=mode.lower()
        if mode=="txt":
                self.mode="txt"
                
        else :
            if mode=="csv":  
                self.mode="csv"
                
            else:
                if mode=="site":
                    self.mode="site"
                    
                else:
                    if mode=="input":
                        self.mode="input"
                        
                    else:
                        raise Exception(" Invalid mode: ", mode, " is not accepted \n")
     
        
        
        
        
    def __setsource(self,source):
        """
            The source must be a valid url, a file or an input
            For taking an input as source insert "input"
        """
        mode=self.mode
        
        if mode=="txt":
            if(source[-4:len(source)])==".txt":
                    self.source=source
            else:
                raise Exception("Extension not supported")
                
            if mode=="csv":  
                if(source[-4:len(source)])==".csv":
                    self.source=source
                else:
                    raise Exception("Extension not supported")
                    
                
            else:
                if mode=="site":
                    self.source=source
                    
                else:
                    raise Exception(" Invalid mode: ", mode, " is not accepted \n")
           
            
    def __setdestination(self,destination):
        """
            The destination must be a .txt file
        """
        if destination[-4:len(destination)]==".txt":
            self.destination=destination
        else:
            raise Exception(" Invalid destination: ", destination, " is not accepted \n")
            
    
   
    
    
            
            
    
    def setinfo(self, insertion="regular"):
        """
            Chose the name of the table where you want to put the data and the attributes
            attributes.
            
            Insertion regular is the default, with this mode all the values of the 
            attributes are considered as numeric types without quotations
            
            Insertion advanced: can be set to specify the need of quotations for
            specific attributes and the type of separation for txt file and csv files.
        """
        
        tablename=input("Select TableName: ")
        self.table=tablename
        
        n=int(input("Number of attributes: "))
        attributes=[]
        types=[]
       
        if insertion=="regular":
        
            for i in range(n):
                attributes.append(input(f"Insert Name of Attribute {i}: "))
            
            
            self.collectdata("regular",attributes,types)
        
        
        
        
        
    def __collectdata(self,insertion, attributes, types):
        """
            Once collected the info about the tables 
            it's necessary to collect the data based on the mode
            the insertion can ba regular or advaced. 
            advanced need to be implemented
        """
        
        if(self.mode=="input"):
            print("You selected to collect data from input: ")
            n=int(input("Number of rows: "))
            
            attrnum=len[attributes]
            
            data={}
            #DATA contains rownumber, rowattr=[value1,value2...] 

            if(insertion=="regular"):   
                
                for i in range(n):
                    print(f"row{i}")
                    rowattr=[]
                    # create an array to store the attributes values
                    
                    for j in range(attrnum):
                        n=input(f"{attributes[j]} : ")
                        rowattr.append(n)
                        # adding each value to the array
                    
                    #when the collection is done i insert the row in the data
                    data[i]=rowattr
                
                print("--Insetion ended--")
            
            """
            else:
                ##TODO
                continue 
            """
        if(self.mode=="txt"):
            print(f"You selected to collect data from {self.source}")
            
            data={}
                #DATA contains rownumber, rowattr=[value1,value2...] 
            with open(self.source, "r", encoding="utf-8") as txt_file:
                row=0
                
                
                for row in txt_file:
                    data[row]=row.split(",")
                    
                print("--Insetion ended--")
        """   
        else:
            ##TODO
        """
                
    
    