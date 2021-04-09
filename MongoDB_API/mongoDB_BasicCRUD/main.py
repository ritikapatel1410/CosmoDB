'''
 @Author: Ritika Patidar
 @Date: 2021-04-09 09:07:00
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-04-09 09:07:00  
 @Title : perform different mode of mongodb  
'''

import sys
import os
sys.path.insert(0, os.path.relpath('LogFile'))
import loggerfile 
from cosmoDB_MongoDB import mongoDB

def main():
    """
        Description:
            this function is define for mode of mongodb CRUD operation
        Parameter:
            None
        Return:
            None
    """
    ObjmongoDB=mongoDB()
    try:
        mode=int(input("=========================\nenter mode of mongodb\n=========================================\n0 : insert data\n=================================\n1 : update data\n===================================\n2 : find data\n===========================================\n3 : delete document\n========================================\n4 : drop collection\n=======================================\nenter : "))
        if(mode==0):
            ObjmongoDB.insert_data()
        elif(mode==1):
            ObjmongoDB.update_data()
        elif(mode==2):
            ObjmongoDB.find_data()
        elif(mode==3):
            ObjmongoDB.delete_document()
        elif(mode==4):
            ObjmongoDB.drop_collection()
        loggerfile.Logger("info","select mode successfully")
    except Exception as error:
        loggerfile.Logger("error","{0} error occured".format(error))

main()