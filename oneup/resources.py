from import_export import resources, fields
from .models import Outsourcing, Manufacture, Logistics, As

class OutResource(resources.ModelResource):
    class Meta:
        model = Outsourcing
        fields = ('id', 'ossn', 'osqu', 'osdate')
        labels = {
            'id':'번호',
            'ossn':'부품코드',
            'osqu':'납품수량',
            'osdate':'납품일시',
        }

class ManResource(resources.ModelResource):
    class Meta:
        model = Manufacture

class LogResource(resources.ModelResource):
    class Meta:
        model = Logistics

class AsResource(resources.ModelResource):
    class Meta:
        model = As