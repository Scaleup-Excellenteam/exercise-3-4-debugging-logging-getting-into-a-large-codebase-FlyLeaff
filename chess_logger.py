import logging

class ChessLogger:
    """
    this class is made to eliminate the log setup and such from the main as its already busy, no need to explain the functions or doc them
    cuz they simply call out the log.respective function
    """
    def __init__(self):
        self.logger = logging.getLogger('chess_logger')
        self.logger.setLevel(logging.DEBUG)
        
        file_handler = logging.FileHandler('log.log_chess')
        console_handler = logging.StreamHandler()
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
    def info(self, message):
        self.logger.info(message)
        
    def debug(self, message):
        self.logger.debug(message)
        
    def warning(self, message):
        self.logger.warning(message)
        
    def error(self, message):
        self.logger.error(message)
        
    def critical(self, message):
        self.logger.critical(message)
