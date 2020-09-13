from django.test import TestCase

import board.models as board_models

# Create your tests here.

def board_models_dbTest():
    board_models.conn()

def board_models_insertTest():
    pass

def board_models_fetchTest():
    results = board_models.fetchlist(1)
    print(results)

def board_models_g_no():
    result = board_models.get_max_g_no()
    print(result)

def board_models_o_no():
    result = board_models.get_max_o_no(7)
    print(result)

def board_models_depth():
    result = board_models.get_max_depth(1, 1)
    print(result)

board_models_fetchTest()


