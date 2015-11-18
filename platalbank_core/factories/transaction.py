import factory
import factory.fuzzy

from .. import models
from .account import AccountFactory
from .event import EventFactory

class TransactionFactory(factory.Factory):
    class Meta:
        model = models.Transaction

    state            = models.Transaction.PENDING
    amount           = factory.fuzzy.FuzzyInteger(1)
    label            = factory.Faker('sentence')
    debited_account  = factory.SubFactory(AccountFactory)
    credited_account = factory.SubFactory(AccountFactory)
    event            = factory.SubFactory(EventFactory)
    # TODO: author   = models.ForeignKey(settings.AUTH_USER_MODEL)
