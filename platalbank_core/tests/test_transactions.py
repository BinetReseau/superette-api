from platalbank_core.factories import TransactionFactory

from rest_framework.test import APITestCase

class TransactionTests(APITestCase):
    def test_transaction(self):
        t = TransactionFactory.create(
            amount                    = 500,
            debited_account__balance  = 4200,
            credited_account__balance = 1337
        )
        self.assertEqual(t.debited_account.balance, 3700)
        self.assertEqual(t.credited_account.balance, 1837)

        # Test what happens when save is called twice
        t.save()
        self.assertEqual(t.debited_account.balance, 3700)
        self.assertEqual(t.credited_account.balance, 1837)
