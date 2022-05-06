import logging

class LogGen:
    @staticmethod
    def genlog():
        logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='../Logs/automate.log')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

# # log = genlog()
# log = LogGen.genlog()
#
# log.info("hello info")