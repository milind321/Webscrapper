import requests
from bs4 import BeautifulSoup
import time as t

URL = 'https://www.topstockresearch.com/PivotPoint/IntradaySupportAndResistanceUsingPivotPoint.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_="table table-bordered table-striped table-hover")
#print(type(results))

stock_elems = results.find_all("tr")
#print(stock_elems)

# creating list        
obj_list = [] 

class Stocks_data:
    def __init__(self,name,S3,S2,S1,Pivot,R1,R2,R3):
        self.name = name
        self.R1 = R1
        self.R2 = R2
        self.R3 = R3
        self.S1 = S1
        self.S2 = S2
        self.S3 = S3
        
for x in stock_elems:
    my_list = [] 
    for y in x:
        for z in y:
            if type(results) is type(z): 
                #print("Both class have different object type.") 
                for comp_name in z:
                    print(comp_name)
                    my_list.append(comp_name) 
            else: 
                #print("Same Object type") 
                print(z) 
                if my_list:
                    #print("List is not empty")
                    my_list.append(z)
               
    #t.sleep(2)
      
    try:
        if my_list:
            print(my_list)
            obj_list.append(Stocks_data(my_list[0],my_list[2],my_list[3],my_list[4],my_list[5],my_list[6],my_list[7],my_list[8])) 
    except:
        print("An exception occurred")  
            
#global obj_list
for obj in obj_list: 
    print(obj.name)
        