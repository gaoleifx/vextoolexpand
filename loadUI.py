try:
    from vextoolexpand import initUI
    from vextoolexpand.initUI import Ui_Form
    from vextoolexpand import utility
    from vextoolexpand.syntax_highlighter import VEXHighlighter
except:
    import initUI
    from initUI import Ui_Form
    import utility
    from syntax_highlighter import VEXHighlighter

from imp import reload
from operator import truediv
from shelve import Shelf
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QFont

import sys
import hou
import os
import json
import re
import vexpressionmenu

reload(initUI)

class loadUI(QtWidgets.QFrame, Ui_Form):

    def __init__(self):
        super().__init__()
        self._path = '{0}/vex/'.format(self.rootpath())
        self._prePath = '{0}/presets/'.format(self.rootpath())
        self._file = ''
        self._text1 = ''
        self._text2 = ''
        self._text3 = ''
        self._text4 = ''
        self._text5 = ''
        self._text6 = ''

        #Ui_Form.__init__(self)
        
        self.setupUi(self)
        self.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
        self.setLayout(self.gridLayout)

        # 设置QTextEdit的字体为粗体
        bold_font = QFont()
        bold_font.setBold(True)

        # 为每个QTextEdit设置粗体字体
        for i in range(1, 7):
            text_edit = getattr(self, f"textEdit_{i}")
            text_edit.setFont(bold_font)

        # 为6个文本编辑器添加语法高亮
        for i in range(1, 7):
            text_edit = getattr(self, f"textEdit_{i}")
            VEXHighlighter(text_edit.document())
        
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 30, 716, 532))

        
        ###set item1#######
        self.setComboBox(self.comboBox_1)
        self.comboBox_1.setLineEdit(self.lineEdit_1)
        self.lineEdit_1.setText(self.comboBox_1.itemText(0))
        self.comboBox_1.activated.connect(lambda:self.updateCode(self.lineEdit_1, self.textEdit_1, self._text1))
        self.btn_to_1.clicked.connect(lambda:self.toWrangle(self.textEdit_1, self.lineEdit_1))
        self.btn_save_1.clicked.connect(lambda:self.saveCode(self.lineEdit_1.text(), self.lineEdit_1, self.textEdit_1))
        self.btn_update_1.clicked.connect(self.updateCode(self.lineEdit_1, self.textEdit_1, self._text1))
        self.btn_from_1.clicked.connect(lambda:self.fromWrangle(self.textEdit_1))

        ###set item2#######
        self.setComboBox(self.comboBox_2)
        self.comboBox_2.setLineEdit(self.lineEdit_2)
        self.lineEdit_2.setText(self.comboBox_2.itemText(1))
        self.comboBox_2.activated.connect(lambda:self.updateCode(self.lineEdit_2, self.textEdit_2, self._text2))
        self.btn_to_2.clicked.connect(lambda:self.toWrangle(self.textEdit_2, self.lineEdit_2))
        self.btn_save_2.clicked.connect(lambda:self.saveCode(self.lineEdit_2.text(), self.lineEdit_2, self.textEdit_2))
        self.btn_update_2.clicked.connect(self.updateCode(self.lineEdit_2, self.textEdit_2, self._text2))
        self.btn_from_2.clicked.connect(lambda:self.fromWrangle(self.textEdit_2))

        ###set item3#######
        self.setComboBox(self.comboBox_3)
        self.comboBox_3.setLineEdit(self.lineEdit_3)
        self.lineEdit_3.setText(self.comboBox_2.itemText(2))
        self.comboBox_3.activated.connect(lambda:self.updateCode(self.lineEdit_3, self.textEdit_3, self._text3))
        self.btn_to_3.clicked.connect(lambda:self.toWrangle(self.textEdit_3, self.lineEdit_3))
        self.btn_save_3.clicked.connect(lambda:self.saveCode(self.lineEdit_3.text(), self.lineEdit_3, self.textEdit_3))
        self.btn_update_3.clicked.connect(self.updateCode(self.lineEdit_3, self.textEdit_3, self._text3))
        self.btn_from_3.clicked.connect(lambda:self.fromWrangle(self.textEdit_3))

        ###set item4#######
        self.setComboBox(self.comboBox_4)
        self.comboBox_4.setLineEdit(self.lineEdit_4)
        self.lineEdit_4.setText(self.comboBox_4.itemText(3))
        self.comboBox_4.activated.connect(lambda:self.updateCode(self.lineEdit_4, self.textEdit_4, self._text4))
        self.btn_to_4.clicked.connect(lambda:self.toWrangle(self.textEdit_4, self.lineEdit_4))
        self.btn_save_4.clicked.connect(lambda:self.saveCode(self.lineEdit_4.text(), self.lineEdit_4, self.textEdit_4))
        self.btn_update_4.clicked.connect(self.updateCode(self.lineEdit_4, self.textEdit_4, self._text4))
        self.btn_from_4.clicked.connect(lambda:self.fromWrangle(self.textEdit_4))

        ###set item5#######
        self.setComboBox(self.comboBox_5)
        self.comboBox_5.setLineEdit(self.lineEdit_5)
        self.lineEdit_5.setText(self.comboBox_5.itemText(4))
        self.comboBox_5.activated.connect(lambda:self.updateCode(self.lineEdit_5, self.textEdit_5, self._text5))
        self.btn_to_5.clicked.connect(lambda:self.toWrangle(self.textEdit_5, self.lineEdit_5))
        self.btn_save_5.clicked.connect(lambda:self.saveCode(self.lineEdit_5.text(), self.lineEdit_5, self.textEdit_5))
        self.btn_update_5.clicked.connect(self.updateCode(self.lineEdit_5, self.textEdit_5, self._text5))
        self.btn_from_5.clicked.connect(lambda:self.fromWrangle(self.textEdit_5))

        ###set item6#######
        self.setComboBox(self.comboBox_6)
        self.comboBox_6.setLineEdit(self.lineEdit_6)
        self.lineEdit_6.setText(self.comboBox_6.itemText(5))
        self.comboBox_6.activated.connect(lambda:self.updateCode(self.lineEdit_6, self.textEdit_6, self._text6))
        self.btn_to_6.clicked.connect(lambda:self.toWrangle(self.textEdit_6, self.lineEdit_6))
        self.btn_save_6.clicked.connect(lambda:self.saveCode(self.lineEdit_6.text(), self.lineEdit_6, self.textEdit_6))
        self.btn_update_6.clicked.connect(self.updateCode(self.lineEdit_6, self.textEdit_6, self._text6))
        self.btn_from_6.clicked.connect(lambda:self.fromWrangle(self.textEdit_6))
        
        
        ##################
        self.show()

    def showInfo(self):
        print('hello houdini')

    def toWrangle(self, textEdit : QtWidgets.QTextEdit, lineEdit):
        self.vexnode(textEdit.toPlainText(), lineEdit)

    def vexnode(self, text : str, lineEdit):
        node = hou.selectedNodes()[0]
        if node is None:
            print('please select wrangle node')
        else:
            node.parm('snippet').set(text)
            node.removeSpareParms()
            node.setName(lineEdit.text(), True)

            vexpressionmenu.createSpareParmsFromChCalls(node, 'snippet')
        
            parmJsonPath = self._prePath + lineEdit.text() + '.json'
            # print(parmJsonPath)
            self.loadNodeParms(parmJsonPath)
            
    # 获取当前脚本所在的目录
    def rootpath(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return current_dir
    
    # 读取脚本所在目录下的root.json文件
    def readRoot(self, jsonPath):
        with open(jsonPath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def fromWrangle(self, textEdit):
        node = hou.selectedNodes()[0]
        code = node.parm('snippet').eval()
        textEdit.setText(code)

    def saveCode(self, file, lineEdit, textEdit):
        if os.path.exists(self._path):
            pass     
        else:
            os.makedirs(self._path, exist_ok=True)
            
        path = self._path + file + '.vfl'   
        title = lineEdit.text()
        text = textEdit.toPlainText()

        with open(path, 'w') as f:
            f.write(text)

        self.saveNodeParms(lineEdit)
        print('Save code successful')

    def saveNodeParms(self, lineEdit):
        node = hou.selectedNodes()[0]
        
        if os.path.exists(self._prePath):
            pass
        else:
            os.makedirs(self._prePath)
            
        parmsPath = self._prePath + lineEdit.text() + '.json'
        parms = node.spareParms()
        parmDict = {}
        for parm in parms:
            rampName = ""
            parmName = parm.name()
            if type(node.parm(parmName).eval()) is hou.Ramp:
                rampName = parmName
                rampDict = {}
                ramp = node.parm(parmName).eval()
                basisList = []
                for ba in ramp.basis():
                    basisList.append(ba.name())
                rampDict['isColor'] = ramp.isColor()
                rampDict['basis'] = tuple(basisList)
                rampDict['keys'] = ramp.keys()
                rampDict['values'] = ramp.values()
                
                #print(ramp.basis()[0].name())
                parmDict[parmName] = rampDict
            else:
                if re.match(r'color_ramp', parmName) == None:
                    parmDict[parmName] = node.parm(parmName).eval()


        json.dump(parmDict, open(parmsPath, 'w'))
        
        
    def loadNodeParms(self, parmJsonPath):
        node = hou.selectedNodes()[0]
        if os.path.exists(parmJsonPath):
            try:
                datas = utility.readJson(parmJsonPath)
                parms = datas.keys()
                for parm in parms:
                    parmValue = node.parm(parm).eval()
                    typea = type(parmValue)
                    if typea is hou.Ramp:
                        rampValue = datas[parm]
                        bas = rampValue['basis']
                        basis = [utility.rampTypeValue()[ba] for ba in bas]
                        keys = rampValue['keys']
                        values = rampValue['values']
                        av = hou.Ramp(tuple(basis), tuple(keys), tuple(values))
                        node.parm(parm).set(av)
                    else:
                        node.parm(parm).set(datas[parm])
                    print(f"Parameter {parm} set to {datas[parm]}")
            except Exception as e:
                print(f"Error loading parameters: {e}")
        else:
            print('预设参数文件不存在')

    def updateCode(self, lineEdit, textEdit, text):
        path = self._path + lineEdit.text() + '.vfl'
        parmJsonPath = self._prePath + lineEdit.text() + '.json'
        if os.path.exists(path):
            with open(path, 'r') as f:
                data = f.read()
                f.seek(0, 0)
                head = lineEdit.text()
                lineEdit.setText(head)
                textEdit.setText(data)
                
        else:
            pass


    def setComboBox(self, comboBox:QtWidgets.QComboBox):
        path = self._path
        for root, folders, files in os.walk(path):
            for file in files:
                ext = os.path.splitext(file)
                if ext[1] == '.vfl':
                    comboBox.addItem(ext[0])


    @property
    def text1(self):
        return self._text1
    @text1.setter
    def text1(self, text):
        self._text1 = text



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = loadUI.load()
    sys.exit(app.exec_())
