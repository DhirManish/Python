#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  compoundinterest.py
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

def compoundinterest(p=0, r=0.0, m=0, t=0):
	return p * (1 + (r / m))**(m * t)

def main():
	p = input("Principal Amount? ")
	r = input("Rate of Interest? ") / 100
	m = input("Months After Calculated? ")
	t = input("Total Years? ")
	print "Compound interest + PA = {:f} after applying {:.2%} as ROI :-)".format(compoundinterest(p, r, m, t), r)
	
	return 0

if __name__ == '__main__':
	main()

