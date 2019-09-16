from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from pokedex.nodes import PokemonNode, TypeNode


class Query(object):
    pokemon = relay.Node.Field(PokemonNode)
    pokemons = DjangoFilterConnectionField(PokemonNode)
    type = relay.Node.Field(TypeNode)
    types = DjangoFilterConnectionField(TypeNode)


class Mutation(object):
    pass
