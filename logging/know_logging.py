'''https://youtu.be/g8nQ90Hk328'''
'''logging'''
''' all caps is constants, capitalized first letter is classes, the all lowercase is methods'''
# print(dir((logging)))

import logging
#5 changing the logger format message google:LOGGER FORMAT
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
#1 create and configure logger, 3 passed the level, 6 passed the format of the message , 7 filemode for appending or overwriting
logging.basicConfig(filename = "lumberjack.log", level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')
logger = logging.getLogger() #4we can name the logger but we're working with the root logger now

#2 test the logger, this is the message that gety's passed in the log format
logger.debug("this is a harmless debug message.")
logger.info("just some useful info.")
logger.warning("i'm sorry, but i can't do that")
logger.error("Did you just try to divide by zero?")
logger.critical("the entire internt is down")

'logger will only write messages with alevel greater or equal to the set level, our message is info but basicConfig default log level is 30'
#3 loggingModule = {'NOTSET':0, 'DEBUG':10, 'INFO':20, 'WARNING':30, 'ERROR':40, 'CRITICAL':50}
# print(logger.level) #there is 6 levels

import math
def quadratic_formula(a, b, c):
    """ return the solution to the equation ax^2 + bx + c = 0."""
    #compute discriminant
    logger.debug("# comput the discriminant")
    disc = b**2 - 4*a*c
    #compute the two roots
    logger.debug("#compute the two roots")
    root1 = (-b + math.sqrt(disc)/(2*a))
    root2 = (-b - math.sqrt(disc)/(2*a))

    # return the roots
    logger.debug("return the roots")
    return (root1,root2)
roots =  quadratic_formula(1,0,4)
print(roots)