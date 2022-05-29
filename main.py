# This is a sample Python script.
import logging
from LogClass import LogConfigActivator
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

LogConfigActivator()
logger_01 = logging.getLogger('test_01')
logger_02 = logging.getLogger('test_02')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    logger_02.info('def print_hi start')
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logger_01(' start main def')
    print_hi('PyCharm')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
