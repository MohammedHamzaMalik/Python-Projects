import string
import random

def random_password_generator():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 8
    return ''.join(random.choice(chars) for x in range(size, 20))

def random_password_generator_ico():
	random_password_generator_ico = """
	#############################################################
	# PYTHON - Random Password Generetor (RPG) #
	#############################################################
	"""
	print(random_password_generator_ico)