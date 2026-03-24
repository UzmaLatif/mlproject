import sys
import logging

logging.basicConfig(level=logging.INFO)

def error_message_detail(error):
    # Extract traceback details
    exc_type, exc_obj, exc_tb = sys.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = f"Error occurred in python script [{file_name}] at line number [{line_number}] error message [{str(error)}]"
    
    return error_message


class CustomException(Exception):
    def __init__(self, error):
        super().__init__(error)
        self.error_message = error_message_detail(error)

    def __str__(self):
        return self.error_message


