import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QLabel
from crawler.simple_crawler import SimpleCrawler


class CheckBoxApp(QWidget):
    def __init__(self):
        super().__init__()

        # 윈도우 설정
        self.setWindowTitle('CheckBox Selection App')
        self.setGeometry(100, 100, 300, 200)

        # 레이아웃 설정
        self.layout = QVBoxLayout()

        # 체크박스 생성 (텍스트는 사용자에게 보이는 부분, objectName은 프로그램이 사용할 값)
        self.checkbox1 = QCheckBox('Option 1', self)
        self.checkbox1.setObjectName('OT_1')

        self.checkbox2 = QCheckBox('Option 2', self)
        self.checkbox2.setObjectName('OT_2')

        self.checkbox3 = QCheckBox('Option 3', self)
        self.checkbox3.setObjectName('OT_3')

        # 버튼 생성
        self.button = QPushButton('Show Selected', self)

        # 라벨 생성
        self.result_label = QLabel('', self)

        # 체크박스와 버튼을 레이아웃에 추가
        self.layout.addWidget(self.checkbox1)
        self.layout.addWidget(self.checkbox2)
        self.layout.addWidget(self.checkbox3)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.result_label)

        # 클릭 이벤트 연결
        self.button.clicked.connect(self.show_selected)

        # 메인 레이아웃 설정
        self.setLayout(self.layout)

    def show_selected(self):
        # 선택된 체크박스 목록 생성
        selected_options = []
        for checkbox in [self.checkbox1, self.checkbox2, self.checkbox3]:
            if checkbox.isChecked():
                # 체크박스가 체크되었을 때 objectName 값을 사용
                selected_options.append(checkbox.objectName())

        # 선택된 항목을 라벨에 표시
        checkboxString = SimpleCrawler.test_method(selected_options)
        self.result_label.setText('Selected: ' + checkboxString)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckBoxApp()
    window.show()
    sys.exit(app.exec())
