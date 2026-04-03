import random
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
password_list = random.sample(characters, 10)
random.shuffle(password_list)
password = "".join(password_list)
print(password)
