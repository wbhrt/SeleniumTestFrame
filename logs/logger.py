import logging
import os
import time

class Logger(object):
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        #写入日志
        t = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_name = log_path + t +'.log'
        l = logging.FileHandler(log_name)
        l.setLevel(logging.INFO)
        # 输出到控制台
        con = logging.StreamHandler()
        con.setLevel(logging.INFO)
        #输出格式
        format = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        l.setFormatter(format)
        con.setFormatter(format)

        self.logger.addHandler(l)
        self.logger.addHandler(con)

    def getlog(self):
        return self.logger

