from django.core.management.base import BaseCommand, CommandError

from factory.fuzzy import FuzzyChoice

from platalbank_core.models import *
from platalbank_core.factories import *

class Command(BaseCommand):
    help = 'Populates the database with generated data. Can be called several times.'

    def add_arguments(self, parser):
        parser.add_argument('-a', '--accounts', metavar='N', type=int, default=100,
                                   help='number of accounts to create')
        parser.add_argument('-e', '--events', metavar='N', type=float, default=0.5,
                                   help='number of events per account to create')
        parser.add_argument('-t', '--transactions', metavar='N', type=float, default=50.,
                                   help='number of transactions per event to create')

    def handle(self, *args, **options):
        accounts     = options['accounts']
        events       = int(options['events'] * accounts)
        transactions = int(options['transactions'] * events)

        AccountFactory.create_batch(accounts)
        EventFactory.create_batch(events)
        TransactionFactory.create_batch(
            size             = transactions,
            event            = FuzzyChoice(Event.objects.all()),
            credited_account = FuzzyChoice(Account.objects.all()),
            debited_account  = FuzzyChoice(Account.objects.all())
        )
