import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.logger import logging



def error_message_deatil(error,error_detail:sys):
    _,_,exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script  name [{0}] line number [{1}] error message [{2}]".format(file_name, exec_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):        
        super().__init__(error_message)
        self.error_message = error_message_deatil(error_message, error_detail)

    def __str__(self):
        return self.error_message
        
