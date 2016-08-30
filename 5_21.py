# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:59:20 2016

@author: mingzheng
"""

#5.21.py
#double-subscript list eample

def printGrades(grades):
    students=len(grades)
    exams=len(grades[0])

    print 'the list is:'
    print '             '
    
    for i in range(exams):
        print "[%d]" % i
        
    for i in range(students):
        print 'grades[%d]' % i
        for j in range(exams):
            print grades[i][j],"",
        print

#main program

grades=[[77,68,86,73],[96,87,89,81],[70,90,86,81]]
print printGrades(grades)