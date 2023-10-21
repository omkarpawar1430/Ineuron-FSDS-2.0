# Importing necessary lib
import os
import logging

# Create logger and configure logging:
logging.basicConfig(filename='name.log', filemode='w', format='%(levelname)s%(asctime)s%(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create name checking function:
def name_check(name):
    logger.debug(f'Checking name: {name}')
    if len(name) == 0:
        logger.error("Name cannot be blank")
        return False
    elif not name.isalpha():
        logger.error("Name must contain only alphabets")
        return False
    else:
        logger.info("Name is valid")
        return True

# Save that checked name in to data.txt:
def save_name(name, email):
    with open("data.txt", "a") as f:
        f.write(f"name = {name}, mail id = {email}.\n")
        logger.info("Data saved successfully")


