from django.db import models
import uuid
# In django in clas if you pass models.model then it treats it as database table
# then we add key with META then it doest treat it as django model but as a django class



class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default= uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_add=True)

    class Meta:
        abstract = True

    