import factory

from .. import models

class EventFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Event

    label         = factory.Faker('sentence')
    through_khube = factory.Faker('boolean')
    writable      = True
    # TODO: owner = models.ForeignKey("LegalPerson")
