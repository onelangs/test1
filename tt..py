# -*- coding: utf-8 -*-
"""
Created on Thu May  5 00:39:02 2016

@author: huang
"""

class testcls:
    @classmethod
    def setUPClass(cls):       
        cls.a='amn'

        print('classmethon:',cls.a)
        
        
if __name__ == '__main__':
    testcls.setUPClass()
    
        