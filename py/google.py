#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  google.py
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

import os, urllib

def main():
	google = os.popen('zenity --entry --text="Enter what you want to google: " --title="My Google Search"').read()
	google = urllib.quote(google)
	os.system('firefox http://www.google.com/search?q=%s' % (google))

if __name__ == '__main__':
	main()
