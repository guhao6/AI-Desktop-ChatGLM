# 导入需要的库：界面、AI调用、配置、界面文件
from keys import key
from langchain_community.chat_models import ChatZhipuAI
import sys
from PySide6.QtWidgets import *
from langchain_core.messages import HumanMessage, SystemMessage
from stats2 import Ui_Form

# 主窗口类
class AIClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI工作台")
        self.resize(600, 600)

        self.history_list = []
        self.config = {
            "api_key": key,
            "model": "glm-4",
            "theme": "light",
            "font_size": 10
        }

        self.system_prompts = {
            "通用大模型": "你是全能AI助手，友好简洁。",
            "代码大模型": "你是专业编程助手，输出完整代码。",
            "文生图大模型": "你是绘画提示词生成器。",
            "翻译模型": "你是专业翻译助手。",
            "AI绘图": "你是一个专业的AI绘画提示词生成器，根据用户的描述，生成详细、专业的AI绘画提示词，包括风格、构图、光影、细节等。",
            "文本翻译": "你是一个专业的翻译助手，支持中英互译，翻译结果准确、地道，同时标注翻译要点。",
        }
        # 加载UI界面
        self.ui = Ui_Form()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.ui.setupUi(self.central_widget)
        # 模型下拉框选项
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(["通用大模型","代码大模型","文生图大模型","翻译模型"])

        self.bind_all_functions()
        self.apply_theme()  # 启动时应用主题

    # 绑定所有按钮、菜单功能
    def bind_all_functions(self):
        self.ui.listWidget.currentRowChanged.connect(self.switch_page)
        self.ui.pushButton_3.clicked.connect(self.clear_chat)
        self.ui.pushButton_2.clicked.connect(self.open_settings)
        self.ui.pushButton.clicked.connect(self.send_message)
        self.ui.horizontalSlider.valueChanged.connect(self.slider_changed)
        self.ui.comboBox.currentIndexChanged.connect(self.model_switched)
        self.statusBar().showMessage("就绪")

    #主题切换核心
    def apply_theme(self):
        if self.config["theme"] == "dark":
            # 黑色主题
            self.setStyleSheet("""
                QMainWindow, QWidget { background-color: #1e1e1e; color: #ffffff; }
                QTextBrowser, QPlainTextEdit, QLineEdit {
                    background-color:#2d2d2d; color:#ffffff; border:1px solid #555;
                }
                QPushButton {
                    background-color:#3b8aff; color:white; padding:6px 12px; border:none; border-radius:5px;
                }
                QPushButton:hover { background-color:#5294ff; }
                QComboBox { background-color:#2d2d2d; color:white; border:1px solid #555; }
                QComboBox QAbstractItemView { background-color:#2d2d2d; color:white; }
                QListWidget { background-color:#2b2b2b; color:white; }
                QTableWidget { background-color:#2d2d2d; color:white; }
                QLabel { color:white; }
                QStatusBar { background-color:#2a2a2a; color:white; }
            """)
        else:
            # 白色主题
            self.setStyleSheet("""
                QMainWindow, QWidget { background-color: #ffffff; color: #000000; }
                QTextBrowser, QPlainTextEdit, QLineEdit {
                    background-color:#ffffff; color:#000000; border:1px solid #ddd;
                }
                QPushButton {
                    background-color:#3b8aff; color:white; padding:6px 12px; border:none; border-radius:5px;
                }
                QPushButton:hover { background-color:#5294ff; }
                QComboBox { background-color:#fff; color:#000; border:1px solid #ddd; }
                QListWidget { background-color:#f5f5f5; color:#000; }
                QTableWidget { background-color:#fff; color:#000; }
                QLabel { color:#000; }
                QStatusBar { background-color:#f5f5f5; color:#000; }
            """)

    #设置窗口
    def open_settings(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("系统设置")
        dlg.resize(350, 280)
        layout = QVBoxLayout(dlg)
        # API Key、模型、主题、字号设置
        l1 = QLabel("API Key")
        t1 = QLineEdit(self.config["api_key"])

        l2 = QLabel("模型")
        c2 = QComboBox()
        c2.addItems(["glm-4","glm-3-turbo"])

        l3 = QLabel("界面主题")
        c3 = QComboBox()
        c3.addItems(["light","dark"])
        c3.setCurrentText(self.config["theme"])

        l4 = QLabel("字体大小")
        c4 = QComboBox()
        c4.addItems(["9","10","11","12"])

        btn_clear = QPushButton("清空历史记录")
        btn_save = QPushButton("保存配置")

        layout.addWidget(l1)
        layout.addWidget(t1)
        layout.addWidget(l2)
        layout.addWidget(c2)
        layout.addWidget(l3)
        layout.addWidget(c3)
        layout.addWidget(l4)
        layout.addWidget(c4)
        layout.addWidget(btn_clear)
        layout.addWidget(btn_save)

        # 保存配置
        def save():
            self.config["api_key"] = t1.text().strip()
            self.config["model"] = c2.currentText()
            self.config["theme"] = c3.currentText()
            self.config["font_size"] = int(c4.currentText())
            self.apply_theme()
            self.statusBar().showMessage("配置已保存")
            dlg.close()

        btn_save.clicked.connect(save)
        btn_clear.clicked.connect(lambda: self.history_list.clear())
        dlg.exec()

    #其余功能不变
    def model_switched(self, index):
        name = self.ui.comboBox.currentText()
        self.ui.textBrowser.append(f"\n【切换】{name}")
        self.scroll_to_bottom()

    # 切换左侧菜单：对话、绘图、翻译、历史、设置
    def switch_page(self, index):
        menu = ["AI对话","AI绘图","文本翻译","历史记录","系统设置"]
        self.ui.textBrowser.append(f"\n→ {menu[index]}")
        self.scroll_to_bottom()
        if index ==3: self.show_history()

    # 显示聊天历史
    def show_history(self):
        self.ui.textBrowser.clear()
        self.ui.textBrowser.append("====== 历史记录 ======")
        for i,item in enumerate(self.history_list,1):
            self.ui.textBrowser.append(f"\n{i}. 用户：{item['user']}")
            self.ui.textBrowser.append(f"AI：{item['ai']}")
        self.scroll_to_bottom()

    # 发送消息给AI（核心功能）
    def send_message(self):
        text = self.ui.plainTextEdit.toPlainText().strip()
        if not text: return

        model_name = self.ui.comboBox.currentText()
        prompt = self.system_prompts[model_name]

        self.ui.textBrowser.append(f"\n【{model_name}】\n用户：{text}")
        self.ui.plainTextEdit.clear()
        QApplication.processEvents()

        # 调用AI模型
        try:
            chat = ChatZhipuAI(api_key=self.config["api_key"],model=self.config["model"])
            msg = [SystemMessage(content=prompt),HumanMessage(content=text)]
            res = chat.invoke(msg)

            # 显示回答并保存历史
            self.ui.textBrowser.append(f"AI：{res.content}")
            self.history_list.append({"user":text,"ai":res.content,"model":model_name})
        except Exception as e:
            self.ui.textBrowser.append(f"错误：{e}")

        self.scroll_to_bottom()

    # 清空聊天
    def scroll_to_bottom(self):
        bar = self.ui.textBrowser.verticalScrollBar()
        bar.setValue(bar.maximum())

    # 滑块变化显示创意度
    def clear_chat(self):
        self.ui.textBrowser.clear()

    # 自动滚动到底部
    def slider_changed(self, v):
        self.statusBar().showMessage(f"创意度：{v}%")

# 程序入口：启动运行
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AIClientWindow()
    w.show()
    sys.exit(app.exec())