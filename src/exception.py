import sys

class CustomException(Exception):
    def __init__(self, error, sys):
        super().__init__(str(error))
        self.error_message = self.get_detailed_error_message(error, sys)

    def get_detailed_error_message(self, error, sys):
        _, _, exc_tb = sys.exc_info()

        if exc_tb is None:
            return str(error)

        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        return f"Error in [{file_name}] at line [{line_number}] : {str(error)}"

    def __str__(self):
        return self.error_message