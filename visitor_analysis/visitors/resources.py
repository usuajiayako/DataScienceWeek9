from import_export import resources
from .models import Visitor

class VisitorResource(resources.ModelResource):
    class Meta:
        model = Visitor
        