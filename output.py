GREEN_SUCCESS = '\033[1;32m'
RED_FAILURE = '\033[1;31m'
YELLOW_INFO = '\033[1;33m'
GREY_INFO = '\033[30;47m'
RESET = '\033[0;0;0m'
# TODO(Kunal): Create a better system to theme this shit

def out(outstr, type):
    '''
    1 - GREEN\n
    2 - RED\n
    3 - YELLOW\n
    4 - GREY\n
    '''
    if type == 'success' or type == 1:
        return GREEN_SUCCESS + outstr + RESET
    elif type == 'fail' or type == 2:
        return RED_FAILURE + outstr + RESET
    elif type == 'warn' or type == 3:
        return YELLOW_INFO + outstr + RESET
    elif type == 'info' or type == 4:
        return GREY_INFO + outstr + RESET

