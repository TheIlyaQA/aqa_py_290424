from logger import logger as log

def my_test():
    a = 2
    b = 3
    # import sys, pdb
    # pdb.Pdb(stdout=sys.stdout).set_trace() # breakpoint
    # locals() - локальні змінні
    c = a + b
    
    if c > 2:
        # pdb.Pdb(stdout=sys.stdout).set_trace()
        log.info("Msg")


my_test()
