import configparser

def read_db_params():
    config = configparser.ConfigParser()
    config.read('config/local.env')
    return config