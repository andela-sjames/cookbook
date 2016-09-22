# cookbook/ingredients/schema.py

import graphene
from graphene import relay, ObjectType
from graphene.contrib.django.filter import DjangoFilterConnectionField
from graphene.contrib.django.types import DjangoNode

from ingredients.models import Category, Ingredient
from graphene.contrib.django.debug import DjangoDebug


class CategoryNode(DjangoNode):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        filter_order_by = ['name']


class IngredientNode(DjangoNode):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        filter_order_by = ['name', 'category__name']


class Query(ObjectType):
    category = relay.NodeField(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.NodeField(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)

    debug = graphene.Field(DjangoDebug, name='__debug')

    class Meta:
        abstract = True
