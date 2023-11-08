import random 
import string
import unittest

def generate_password(length): 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password



def is_valid_password(password ,length):
    return len(password) == length



class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password(self) :
        password_length = 12
        password = generate_password(password_length) 
        self.assertTrue(is_valid_password(password, password_length)) 


    def test_generated_password_with_zero_length(self) :
        password_length = 0
        password = generate_password(password_length)
        self.assertTrue(is_valid_password(password ,password_length))

    def test_generate_password_with_large_length(self):
        password_length = 1000
        password = generate_password(password_length)
        self.assertTrue(is_valid_password(password, password_length))


if __name__ == "__main__" :
    unittest.main()           

   

