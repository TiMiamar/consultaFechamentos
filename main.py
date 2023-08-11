import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt, QModelIndex, QAbstractListModel, QDate
from PySide6.QtUiTools import QUiLoader
import mysql.connector
from PySide6.QtGui import QFont, QIntValidator
from datetime import  datetime
import variavel

class ResultListModel(QAbstractListModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            result = self._data[index.row()]
            return f"Nome: {result[0]}, Data: {datetime.strftime(result[1], '%d/%m/%Y')}, Valor: R$ {int(result[2])}"
        elif role == Qt.FontRole:
            font = QFont()
            font.setBold(True)
            return font
        return None
class MainWindow(QMainWindow):

    def __init__(self, ui_file):
        super().__init__()

        # Obtém o diretório atual do script
        dir_path = os.path.dirname(os.path.abspath(__file__))

        # Obtém o caminho completo do arquivo .ui
        ui_file_path = os.path.join(dir_path, ui_file)

        # Carregar o arquivo .ui
        loader = QUiLoader()
        self.window = loader.load(ui_file_path)

        self.setWindowTitle("Consulta Fechamentos")
        self.setCentralWidget(self.window)

        self.window.pesquisa.clicked.connect(self.perform_search)

        self.setGeometry(0,0,792,386)

        current_date = QDate.currentDate()
        self.window.data_inicial.setDate(current_date)
        self.window.data_final.setDate(current_date)

        self.window.min_value.setValidator(QIntValidator())
        self.window.max_value.setValidator(QIntValidator())


        for item in variavel.lojas:
            self.window.comboBox.addItem(item)

        self.window.comboBox.setCurrentIndex(11)


    def perform_search(self):
        min_value = self.window.min_value.text()
        max_value = self.window.max_value.text()
        msg = QMessageBox()
        msg.setWindowTitle("Erro")

        if min_value == "":
            msg.setText("Insira um valor")
            msg.exec_()
            return

        if min_value > max_value:
            msg.setText("O valor inicial está maior que o final")
            msg.exec_()
            return

        min_date = self.window.data_inicial.text()
        max_date = self.window.data_final.text()
        fdata_inicial = datetime.strptime(min_date, "%d/%m/%Y")
        fdata_final = datetime.strptime(max_date, "%d/%m/%Y")
        fdata_final2 = datetime.strftime(fdata_final, "%Y-%m-%d 23:59:59")


        if self.window.bt_conciliado.isChecked():
            a = "1"
            b = "1"
            c = "=1"
        elif self.window.bt_nao_conciliado.isChecked():
            a = "0"
            b = "0"
            c = "is null"
        else :
            a = "1"
            b = "0"
            c = "is null"


        combo_box_text = self.window.comboBox.currentText()
        combo_box_loja = self.window.comboBox.currentIndex()


        if combo_box_loja == 0:
            loja  ="='69FFA076-7185-4805-BE1B-56D32305F531'"
        elif combo_box_loja == 1:
            loja ="='F2AC4502-775D-46A2-AFA0-B053AAB24FCC'"
        elif combo_box_loja == 2:
            loja = "='40EB8341-9B73-4491-90AD-B791B38631C1'"
        elif combo_box_loja == 3:
            loja = "='64BB7EEB-E6D3-46E9-8602-39935FDD2308'"
        elif combo_box_loja == 4:
            loja = "='DEDC340C-528D-462D-94EE-E5BC3BC25707'"
        elif combo_box_loja == 5:
            loja = "='51CF1246-B25B-4B4E-8491-EF20FA725196'"
        elif combo_box_loja == 6:
            loja = "='A22FC411-59F5-4751-95E0-346981C1F4C8'"
        elif combo_box_loja == 7:
            loja = "='B4FFAB85-D9E1-4B82-BAB1-652E94B50921'"
        elif combo_box_loja == 8:
            loja = "='D9461635-46E8-436E-91DF-69723E7C5D65'"
        elif combo_box_loja == 9:
            loja = "='638B3AA7-ACF8-4556-B66D-A52666272B09'"
        elif combo_box_loja == 10:
            loja = "='6F181543-5839-4775-8738-1296F8E27ED0'"
        elif combo_box_loja == 11:
            loja = "is not null"
        # Realizar a conexão com o banco de dados
        db = mysql.connector.connect(
            host="edi.miamarmake.com.br",
            port="11306",
            user="bi",
            password="bi123",
            database="ideiaerp"
        )

        # Realizar a consulta no banco de dados
        cursor = db.cursor()
        query = """SELECT
e.empresa_nome,fc.datahora, fcs.valorinformado, fc.flagfechamentoconciliado
FROM fechamentocaixa AS fc
JOIN fechamentocaixasaldo AS fcs ON fc.fechamentocaixa_id  = fcs.fechamentocaixa_id
JOIN empresa AS e on fc.empresa_id = e.empresa_id


WHERE
	 fcs.nomecondicaopagamento = 'DINHEIRO' 
AND fcs.valorinformado BETWEEN %s AND %s
AND fc.datahora BETWEEN %s AND %s
AND (fc.flagfechamentoconciliado = %s or fc.flagfechamentoconciliado = %s or fc.flagfechamentoconciliado """+c+""")
and fc.empresa_id """+loja+"""

order by e.empresa_nome, fc.datahora"""
        cursor.execute(query, (min_value, max_value, fdata_inicial, fdata_final2,a,b))
        results = cursor.fetchall()


        model = ResultListModel(results)
        self.window.listView.setModel(model)
        if not results :
            msg.setText("Nenhum fechamento encontrado")
            msg.exec_()
        # Fechar a conexão com o banco de dados
        cursor.close()
        db.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file = "pesquisa.ui"

    window = MainWindow(ui_file)
    window.show()

    sys.exit(app.exec())
