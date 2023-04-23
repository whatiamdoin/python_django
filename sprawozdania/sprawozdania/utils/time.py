from datetime import datetime


def get_time():
    time = datetime.now().strftime('%H_%M_%S')
    return time
