from django.db import models
import datetime
from django.utils import timezone
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from py2neo import Graph
from neomodel import StructuredNode, StringProperty, DateProperty,IntegerProperty,RelationshipFrom,RelationshipTo,Relationship


class BD(StructuredNode):
    date = DateProperty(index=True)

class IndexComponent(StructuredNode):
    name=StringProperty(index=True)
    id = models.IntegerField(default=0)
    bbgTicker = StringProperty()
    businessCenter =StringProperty()
    name = StringProperty()


class AlgoIndex(StructuredNode):
    name = StringProperty()
    businessCenter = StringProperty()
    id = models.IntegerField(default=0)
    members = RelationshipFrom(IndexComponent, 'memberOf')

AlgoIndex._default_manager = AlgoIndex.nodes











