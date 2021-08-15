import logging

class LogGen:
    @staticmethod
    def logGeneration():
        # logging.basicConfig(filename=".\\Logs\\Automation.log",format='%(asctime)s -  %(name)s - %(levelname)s - %(message)s', datefmt='%m%d%Y %I:%M:%S %p')
        # logger=logging.getLogger()
        # logger.setLevel(logging.INFO)
        # return logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fileHandler = logging.FileHandler(".\\Logs\\Automation.log", mode='a')
        fileHandler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        return logger
