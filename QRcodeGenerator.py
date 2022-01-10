import qrcode as qr 



from PyQt6 import uic,QtWidgets
def salvar():
    
    path=QtWidgets.QFileDialog.getSaveFileName()[0]
    print(path)
    pass

def GerarQrCode():
    
    
    link=QrcodeTela.lineEdit.text()
    if  link=="":
        QrcodeTela.lineEdit.setText("Digite Algo")
        
        QrcodeTela.status.setText("Digite o link para gerar o arquivo")
    else:
        Imagem_qrcode=qr.make(link)
        path=QtWidgets.QFileDialog.getSaveFileName()[0]
        print(path)
    
        Imagem_qrcode.save(f"{path}.png") 
        QrcodeTela.lineEdit.setText("")
        
        QrcodeTela.status.setText("Arquivo Gerado com Sucesso ! ")
    

app=QtWidgets.QApplication([])
QrcodeTela=uic.loadUi("QrCodeGen.ui")
QrcodeTela.pushButton.clicked.connect(GerarQrCode)
#QrcodeTela.actionSalva.triggered.connect(salvar)

QrcodeTela.show()
app.exec()