"""
This is a setup.py script generated by py2applet

To make the distribution type the following in terminal
	python setup.py py2app

To make the distribution in windows:
	python setup.py build

On Windows side ConverterGUI.py, change:
	self.path = str(url.path()) to self.path = str(url.path())[1:]
 
This distribution utility will package everything into the distribution.  To
reduce the size of the application, manually delete:
1)  All frameworks except Python, QtCore and QtGui in the Frameworks folder
2)  mpl-data folder from the Resources folder
3)  email, matplotlib and scipy folder from resources/lib/python2.7/
4)  _bsddb.so,_sqlite3.so, and unicodedata.so from resources/lib/python2.7/lib-dynload
"""

from setuptools import setup

APP = ['ConverterGUI.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': False, 'includes':['PyQt4.QtCore','PyQt4.QtGui', 'PyQt4._qt','numpy','copy','re','datetime','sys','ELD_Cell','ELD_Chip','ELD_Field','ELD_Pattern','GDS2v3','GDSII','GDSII_ARef','GDSII_Boundary','GDSII_Box','GDSII_Library','GDSII_Node','GDSII_Path','GDSII_SRef','GDSII_Structure','GDSII_Text','v3','v3_Director','v3_ID','v3_Pat','v3_TX','v3_TXB','fracture','arrayFracture']}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
