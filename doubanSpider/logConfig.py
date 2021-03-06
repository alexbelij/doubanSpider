import logging


class MyLogger(object):

    def __init__(self):
        # # 设置日志打印格式
        # formatter = logging.Formatter(
        #     '%(asctime)s - %(levelname)s - %(filename)s-%(funcName)s[line:%(lineno)d] - %(message)s')
        # 配置日志信息
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(filename)s-%(funcName)s[line:%(lineno)d] - %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename='spider.log',
                            filemode='a')
        # 定义一个Handler打印INFO及以上级别的日志到sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # 设置日志打印格式
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s-%(funcName)s[line:%(lineno)d] - %(message)s')
        console.setFormatter(formatter)
        # 将定义好的console日志handler添加到root logger
        logging.getLogger('').addHandler(console)

        errorlog = logging.FileHandler("error.log")
        errorlog.setLevel(logging.ERROR)
        errorlog.setFormatter(formatter)
        logging.getLogger('').addHandler(errorlog)

        debuglog = logging.FileHandler("spider.log")
        debuglog.setLevel(logging.DEBUG)
        debuglog.setFormatter(formatter)
        logging.getLogger('').addHandler(debuglog)

logger = MyLogger()
