class error_handling:
    @staticmethod
    def error_handling(num):
        if not isinstance(num, int):
            raise ValueError('Work with Positive Integers Only')
        else:
            return "All is Well!"
        
