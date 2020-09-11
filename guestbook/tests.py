from django.test import TestCase

import guestbook.models as guestbook_models

# Create your tests here.

def test_guestbookModel_fetchall():
    results = guestbook_models.fetchlist()
    print(results)

def run():
    test_guestbookModel_fetchall()

if __name__ == '__main__':
    run()