import sys
from src.logger import logging   # use your custom logger

def error_message_detail(error):
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


# For testing purpose
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Exception occurred")
        raise CustomException(e)