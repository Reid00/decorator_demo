# -*- encoding: utf-8 -*-
'''
@File        :logger.py
@Time        :2021/04/27 15:18:29
@Author      :Reid
@Version     :1.0
@Desc        :日志的设置
'''

# here put the import lib
import logging
import logging.handlers
from pathlib import Path

class Logger:

    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, filename, level='info', when='D', back_count=3):

        fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(Logger.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = logging.handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=back_count,
                                                       encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器

        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)


def set_logger():
    root_logger = logging.getLogger()    # 获取现有的logger
    for h in root_logger.handlers:      #清除现有的handler
        root_logger.removeHandler(h)
    log_format="[%(asctime)s]-%(name)s-%(levelname)s-%(message)s"
    log_file = Path(__file__).with_suffix('.log')
    # log_file = __file__
    file_hanlder = logging.handlers.TimedRotatingFileHandler(filename=log_file, when='D', encoding='utf-8') # 需要导入logging.handlers 这是logging 的子模块
    # file_hanlder = logging.FileHandler(filename=log_file, mode='a', encoding='utf-8')
    logging.basicConfig(handlers={file_hanlder}, format=log_format, level=logging.INFO)


def test():
    set_logger()
    try:
        result = 10 / 0
    except Exception:
        logging.error('Faild to get result', exc_info=True)


if __name__ == '__main__':
    test()