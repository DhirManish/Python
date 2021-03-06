#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  numbersystemtable.py
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

def draw():
	# '<' for left align, '^' for center align, '>' for right align
	for i in '====':
		print '{0:{fill}{align}5}'.format(i, fill='~', align='^'),
	print

def header():
	# '<' for left align, '^' for center align, '>' for right align
	for i in 'dxob':
		print '{0:{fill}{align}5}'.format(i, fill=' ', align='>'),
	print

def main():	
	header()
	draw()
	
	for num in range(0, 16):
		for base in 'dXob':
			print '{0:5{base}}'.format(num, base=base),
		print
	
	draw()
		
	return 0

if __name__ == '__main__':
	main()

