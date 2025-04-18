from logger import logging

def add(a,b):
    logging.debug("the addition function calling")
    return a+b 

logging.debug("The addition performing")
add(10,12)

def mul(a,b):
    logging.debug("The mul functuion calling")
    return a*b


logging.debug("Multiplication perform")
mul(10,2)