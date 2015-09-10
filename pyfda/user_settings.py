# -*- coding: utf-8 -*-
"""
filterbroker.py

Created on Wed Dec 03 06:13:50 2014

http://stackoverflow.com/questions/13034496/using-global-variables-between-files-in-python
oder
http://pymotw.com/2/articles/data_persistence.html

@author: Christian Muenker
"""

# TODO: dmNames need to be built automatically!

from __future__ import division, unicode_literals
# importing user_settings runs the module once, defining all variables
# module variables, similar to class variables, are global

mpl_rc = {'lines.linewidth': 1.5,
            'font.size':14, 'legend.fontsize':12, 
            'axes.labelsize':14, 'axes.titlesize':16, 'axes.linewidth':1}
            
css_rc = {'QTabBar':'QTabBar{font-size:12px; font-weight:bold;}',
          'QApplication':'QWidget{font-size:12px; font-family: Tahoma;}',
          'QWidget':('QWidget{Background: #CCCCCC; color:black; font-size:14px;'
                     'font-weight:bold; border-radius: 1px;}')
          }

N_FFT = 2048 # number of FFT points for plot commands (freqz etc.)


css = """
/*height: 14px;*/
/*
QDialog{
Background-image:url('img/xxx.png');
font-size:14px;
color: black;
}
*/


QToolButton:hover{
Background: #DDEEFF;
}
"""