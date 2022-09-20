# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle-1 import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Right
    
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    
    # Isosceles    
    def testIsoscelesA(self): 
        self.assertEqual(classifyTriangle(3,3,4),'Isosceles','3,3,4 is a Isosceles triangle')
        
    def testIsoscelesB(self): 
        self.assertEqual(classifyTriangle(4,4,5),'Isosceles','4,4,5 is a Isosceles triangle')
    
    #Equilateral
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is an Equilateral triangle')
       
    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 is an Equilateral triangle')    

    #NotATriangle
        
    def testInvalidTriangleA(self): 
        self.assertEqual(classifyTriangle(2,2,5),'NotATriangle','2,2,5 is not a triangle')
       
    def testInvalidTriangleA(self): 
        self.assertEqual(classifyTriangle(0,5,5),'NotATriangle','0,5,5 is not a triangle')    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

