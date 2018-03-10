import graphene
from graphene_django import DjangoObjectType
from .models import Event
from django.db.models import Q

class EventType(DjangoObjectType):
    class Meta:
        model = Event

# Query to get data from the server
class Query(graphene.ObjectType):
    events = graphene.List(EventType,
                           search=graphene.String(),
                           first=graphene.Int(),
                           skip=graphene.Int(),
                           last=graphene.Int(),
                           )

    def resolve_events(self, info, search=None, first=None, skip=None, last=None, **kwargs):
        qs = Event.objects.all()

        # Search records which partially matches name and url
        if search:
            filter = (
                Q(url__icontains=search) |
                Q(name__icontains=search)
            )
            qs = qs.filter(filter)

        # Skip n records
        if skip:
            qs = qs[skip::]

        # Get the first n records
        if first:
            qs = qs[:first]

        # Get the last n records
        if last:
            last_n = qs.order_by('-id')[:last]
            qs = reversed(last_n)
        return qs


# Create new Event
class CreateEvent(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    url = graphene.String()

    class Arguments:
        url = graphene.String()
        name = graphene.String()


    def mutate(self, info, name, url):
        event = Event(url=url, name=name)
        event.save()

        return CreateEvent(
            id=event.id,
            name=event.name,
            url=event.url,
        )


# Create event to the server
class Mutation(graphene.ObjectType):
    create_event = CreateEvent.Field()