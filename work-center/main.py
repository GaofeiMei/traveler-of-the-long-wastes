from PySide6.QtQuick import QQuickView
from PySide6.QtGui import QGuiApplication
import sys

app = QGuiApplication(sys.argv)

view = QQuickView()
view.setSource("main.qml")
view.show()

sys.exit(app.exec())