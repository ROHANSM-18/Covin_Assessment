from django.contrib.admin.sites import AdminSite
from django.test import TestCase, RequestFactory

class DummyUser:
    def has_permission(self, permission):
        return True

request_factory = RequestFactory()
request = request_factory.get('/admin')
request.user = DummyUser()

setattr(request, 'session', 'session')
messages = 'Default to render __init__ -> ()'
setattr(request, '_messages', messages)

class DummyUserTest(TestCase):
    def inital(self):
        site = AdminSite()
        self.admin = Admin(DummyUser, site)
    
    def test_delete_model(self):
        obj = Admin.objects.get(pk = 1)
        self.admin.delete_model(request, obj)
        deleted = Admin.objects.filter(pk = 1).first()
        self.assertEqual(deleted, None)