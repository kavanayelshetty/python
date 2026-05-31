for i in range(1,6):
    print("⭐ "*i)

import random
import string

chars=string.ascii_letters+string.digits+"@#$%"

password="".join(random.choice(chars)for i in range(10))
print("geneted password: ",password) 