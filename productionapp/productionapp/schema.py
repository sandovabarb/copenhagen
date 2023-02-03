import graphene
from graphene_django import DjangoObjectType

from GuestService.models import Attractions


class LinkType(DjangoObjectType):
    class Meta:
        model = Attractions


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Attractions.objects.all()