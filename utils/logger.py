import logging
#File contains utilities for setting up logging in progress.....

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    #Get logger object from the discord logger
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
     # Create a file handler to write log messages to 'discord.log' with UTF-8 encoding and write mode
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
