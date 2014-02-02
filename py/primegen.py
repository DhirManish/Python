#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  primegen.py
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

import sys
from math import sqrt

def main(argv):
	n = int(argv)
	print sorted(set(range(2, n + 1)).difference(set((p * f) for p in range(2, int(sqrt(n)) + 1) for f in range(2, (n / p) + 1))))

if __name__ == '__main__':
	try:
		main(sys.argv[1])
	except IndexError:
		print "Usage: primegen.py <limit>"
