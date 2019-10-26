from sys import argv

from lib.kata_generator import KataGenerator
from lib.kata_generator_logger import KataGeneratorLogger

argv.pop(0)
kata_name = argv.pop(0)
params = argv
logger = KataGeneratorLogger()
KataGenerator(kata_name, logger, params).call()
