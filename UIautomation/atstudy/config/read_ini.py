# 封装成别人可以使用的代码
import configparser
import os


class ReadIni:  # file_name指定文件名，node指定节点名
    def __init__(self, file_name=None, node=None):
        self.file_name = file_name
        self.node = node
        if file_name is None:
            self.file_name = os.path.dirname(os.path.dirname(__file__))+'/config/config.ini'
        if node is None:
            self.node = 'config'
        self.cf = self.load_ini(self.file_name)

    def load_ini(self, file_name):  # 加载配置文件
        cf = configparser.ConfigParser()  # 获取解析配置对象
        cf.read(file_name, encoding='utf-8')
        return cf

    def get_value(self, key):  # 获取配置文件中的指定内容‘key’
        return self.cf.get(self.node, key)


# 进行单元测试
if __name__ == '__main__':
    print(ReadIni().get_value('browser'))
