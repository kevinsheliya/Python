import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("Arithmatic APP")

def add(a,b):
    c=a+b
    logger.debug(f"Addition {a} + {b} = {c}")
    return c 


def sub(a,b):
    c=a-b
    logger.debug(f"Addition {a} - {b} = {c}")
    return c


def mul(a,b):
    c=a*b
    logger.debug(f"Addition {a} * {b} = {c}")
    return c


def div(a,b):
    try:
        c=a/b
        logger.debug(f"Addition {a} / {b} = {c}")
        return c
    except ZeroDivisionError:
        logger.debug("division by zero error")
        return None
    
add(10,2)
sub(10,2)
mul(10,2)
div(10,0)    
