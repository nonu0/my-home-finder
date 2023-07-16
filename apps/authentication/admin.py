from typing import Any, Optional
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.query import QuerySet
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField
from django.http.request import HttpRequest
from apps.authentication.extras import delete_tenant_data

User = get_user_model()

class AccountAdmin(admin.ModelAdmin):
    using = 'default'
    list_display = ('email','username')
    list_display_link = ('email','username')
    list_filter = ('email','username')
    search_list = ('username')
    list_per_page = 25

    def save_model(self, request: Any, obj: Any, form: Any, change: Any):
        obj.save(using=self.using)

    def delete_model(self, request: HttpRequest, obj: Any) -> None:
        email = obj.email
        obj.delete(using=self.using)
        delete_tenant_data(email)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).using(self.using)
    

    def formfield_for_foreignkey(self, db_field: ForeignKey[Any], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:
        return super().formfield_for_foreignkey(db_field, request,using=self.using, **kwargs)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request,using=self.using, **kwargs)
    
admin.site.register(User,AccountAdmin)