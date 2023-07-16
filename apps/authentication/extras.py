from django.contrib.auth import get_user_model


User = get_user_model()

def delete_tenant_data(tenant_email):
    if User.objects.filter(email=tenant_email).exists():
        User.objects.filter(email=tenant_email).delete()
