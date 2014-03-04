#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  classexmp.py
#  
#  Copyright 2014 Ajay Bhatia <ajay@dumb-box>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class Employee:
	count = 0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.count += 1
				
	def displayEmployee(self):
		print "Name : %s\tSalary : %d" % (self.name, self.salary)

def displayCount():
	print "Total Employee(s) %d" % Employee.count

def main():
	emp1 = Employee("David", 100000)
	emp2 = Employee("Zeuz", 48000)
	
	emp1.displayEmployee()
	emp2.displayEmployee()
	
	displayCount()
	
	print "Employee.__doc__:", Employee.__doc__
	print "Employee.__name__:", Employee.__name__
	print "Employee.__module__:", Employee.__module__
	print "Employee.__bases__:", Employee.__bases__
	print "Employee.__dict__:", Employee.__dict__
	
	return 0

if __name__ == '__main__':
	main()

