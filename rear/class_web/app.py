"""
    主程序运行文件
"""

from class_web import make_app

app = make_app()

if __name__ == '__main__':
    app.run()