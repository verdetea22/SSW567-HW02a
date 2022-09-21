# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    #Right
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    
    
    #Equilateral
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is an Equilateral triangle')
        
    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(6,6,6),'Equilateral','6,6,6 is an Equilateral triangle')    
    
    
    #Scalene
    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(7,8,10),'Scalene','7,8,10 is a Scalene triangle')
        
    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','4,5,6 is a Scalene triangle')    
        
        
    #Isoceles
    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(5,5,7),'Isoceles','5,5,7 is an Isoceles triangle')
        
    def testIsocelesTriangleB(self): 
        self.assertEqual(classifyTriangle(6,6,8),'Isoceles','6,6,8 is an Isoceles triangle')          
 
 
    #NotATriangle
    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 is Not A Triangle 1+2=<3')
        
    def testIsocelesTriangleB(self): 
        self.assertEqual(classifyTriangle(1,5,6),'NotATriangle','1,5,6 is Not A Triangle because 1+5=<6')       
        
        
    #InvalidInput    
    def testInvalidTriangleA(self): 
        self.assertEqual(classifyTriangle(0,2,3),'InvalidInput','0,2,3 is an Invalid Input because 0 isnt acceptable')
        
    def testInvalidTriangleB(self): 
        self.assertEqual(classifyTriangle(2.5,5,6),'InvalidInput','2.5,5,6 is an Invalid Input because floats arent acceptable')  
    
    def testInvalidTriangleB(self): 
        self.assertEqual(classifyTriangle(-9,5,6),'InvalidInput','-9,5,6 is an Invalid Input because negative inputs arent acceptable')         
           
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

