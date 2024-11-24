
import sys
from PyQt5.QtWidgets import QApplication
from gui_pyqt5 import SchoolManagementSystem

def main():
    app = QApplication(sys.argv)
    window = SchoolManagementSystem()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()