from django.db import models
from django.conf import settings
from open_humans.models import OpenHumansMember


class RunkeeperMember(models.Model):
    """
    Store OAuth data for a Runkeeper member.
    This is a one to one relationship with a OpenHumansMember model
    You can find the OpenHumansMember model in open_humans/models.py

    There is a bi-directional link, called oh_member from this object. This could be used
    to fetch the OpenHumansMember object given a DataSourceMember object.
    """
    user = models.OneToOneField(OpenHumansMember, on_delete=models.CASCADE)
    # Your other fields should go below here
