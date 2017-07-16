# -*- coding: utf-8 -*- 
#인코딩 설정

import time
from pywinauto import application
###############################################################################
def getWindow(app, windowText, exactMatch=True):
	ws = app.windows_()
	for w in ws:
		if w.WindowText() == windowText:
			return w
	return None

###############################################################################
def NotepadTest():
	app=application.Application.start("notepad.exe")

	memo = getWindow(app, u"제목 없음 - 메모장")
	memo.TypeKeys('abcde')

	time.sleep(2)
	app.notepad.TypeKeys("%FX")
	time.sleep(1)

	saveDG = getWindow(app, u"메모장")
	saveDG.TypeKeys("%N")

###############################################################################
if __name__ == '__main__':
	NotepadTest()
###############################################################################
def printWindows(app):
	ws = app.windows_()
	for w in ws:
		print 'WindowText=<%s>, Text=<%s>' % (w.WindowText(), w.Texts())
