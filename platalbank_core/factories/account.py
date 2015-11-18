import factory

from .. import models

class AccountFactory(factory.Factory):
    class Meta:
        model = models.Account

    balance       = 0
    description   = factory.Faker('text', max_nb_chars=models.Account.DESCRIPTION_MAX_LENGTH)
    short_name    = factory.Faker('user_name')
    # TODO: owner = models.ForeignKey("LegalPerson")
