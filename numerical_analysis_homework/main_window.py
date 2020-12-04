import sys, os
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, QtCore, uic
from PyQt5.QtGui import QPalette, QColor
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from utils.integrator import Integrator
from utils.other import extract_points

class Main_window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(Main_window, self).__init__()
        script_dir = os.path.dirname(os.path.realpath(__file__))
        uic.loadUi(
            os.path.abspath(os.path.join(script_dir, os.pardir))  # Parent directory
            + os.path.sep
            + "resource"
            + os.path.sep
            + "main_window.ui",
            self,
        )
        self.addToolBar(NavigationToolbar(self.plot.canvas, self))
        # self.setWindowIcon(QtGui.QIcon(
        #     os.path.abspath(os.path.join(script_dir, os.pardir))  # Parent directory
        #     + os.path.sep
        #     + "resources"
        #     + os.path.sep
        #     + "icon.png"))

        self.plot_btn.clicked.connect(self.on_plot_btn_click)

    def insert_table_row(self, row_index, row):
        self.table.insertRow(row_index)
        self.row_index = row_index

        for index, item in enumerate(row):
            self.table.setItem(row_index, index, QtWidgets.QTableWidgetItem(
                f"{item:.6e}"))

    def plot_on_canvas(self, points_to_plot):
        self.plot.canvas.axes[0].clear()
        self.plot.canvas.axes[0].plot(points_to_plot.xs, points_to_plot.v_1s, 'g')
        self.plot.canvas.axes[0].plot(points_to_plot.xs, points_to_plot.v_2s, 'r')
        self.plot.canvas.axes[0].legend(('v_1(x)', 'v_2(x)'),loc='upper right')
        self.plot.canvas.axes[0].set_title('Численное решение')
        self.plot.canvas.axes[0].set_xlabel("x")
        self.plot.canvas.axes[0].set_ylabel("v_1(x)/v_2(x)")

        self.plot.canvas.axes[1].clear()
        self.plot.canvas.axes[1].plot(points_to_plot.v_1s, points_to_plot.v_2s, 'm')
        self.plot.canvas.axes[1].set_title('Фазовый портрет')
        self.plot.canvas.axes[1].set_xlabel("v_1")
        self.plot.canvas.axes[1].set_ylabel("v_2")

        self.plot.canvas.draw()


    def on_plot_btn_click(self) -> None:

        row = 0
        # Clear output table
        while (self.table.rowCount() > 0):
                self.table.removeRow(0)

        step = float(self.step_input.text())
        x_max = float(self.x_max_input.text())
        eps = float(self.eps_input.text())
        max_iters = float(self.max_iters_input.text())

        k = float(self.k_input.text())
        c = float(self.c_input.text())
        m = float(self.m_input.text())

        # Initial conditions
        x = 0
        y = np.array([10, 0], dtype=np.longdouble)

        A = np.matrix([
            [      0.,       1.],
            [-(k / m), -(c / m)]
        ], dtype=np.longdouble)

        integrator = Integrator(A, eps, step)
        points_info = []

        iter_counter = 0
        while True:
            new_point_info = integrator.next_point(x, y)
            points_info.append(new_point_info)
            x = new_point_info['x']
            y = new_point_info['y']

            self.table.insertRow(row)
            for index, item in enumerate(new_point_info.values()):
                self.table.setItem(row, index, QtWidgets.QTableWidgetItem(
                        f"{item:.4e}" if isinstance(item, float) else f"{item}"))

            iter_counter += 1
            row += 1

            if x >= x_max or iter_counter > max_iters:
                break

        self.table.setVerticalHeaderLabels((str(i) for i in range(row + 1)))
        self.plot_on_canvas(extract_points(points_info))



def main() -> None:
    app = QtWidgets.QApplication(sys.argv)

    # Force the style to be the same on all OSs:
    app.setStyle("Fusion")

    # Now use a palette to switch to dark colors:
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    window = Main_window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()