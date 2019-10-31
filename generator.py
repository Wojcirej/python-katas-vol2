from sys import argv

from lib.kata_generator import KataGenerator
from lib.kata_generator_logger import KataGeneratorLogger
from lib.kata_generator_templater import KataGeneratorTemplater

argv.pop(0)
kata_name = argv.pop(0)
params = argv
logger = KataGeneratorLogger()
templater = KataGeneratorTemplater(kata_name, params)
KataGenerator(kata_name, logger, templater, params).call()
