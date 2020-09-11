from django.test import TestCase

import user.models as user_models
# Create your tests here.


def test_usermodels_insert():
    user_models.insert("우성", "test@email.com", "1234", "남")

def test_usermodels_fetchone():
    result = user_models.fetchone('test1@email.com', '1234')
    print(result)

# test_usermodels_insert()

test_usermodels_fetchone()