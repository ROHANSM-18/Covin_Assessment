from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class Admin(permission):
    def authenticate(self):
        self.user = authenticate(username='john', password='secret')
        if self.user is not None:
            admin.site.register(self.user, AdminPanel)
        else:
            admin.site.error('User non-existent')
            create(self.user)

    def create(self, request):
        username = request.REQUEST.get('username', None)
        password = request.REQUEST.get('password', None)

        user = User.objects.create_user(username = username, password = password)
        user.save()

        return render_to_response('home.html', context_instance = RequestContext(request))

    def delete_user(self, request, username):
        try:
            user = User.objects.get(username = username)
            user.delete()
            messages.success(request, "User is deleted!")
        except:
            messages.error(request, "Couldn't delete user!")
        return render(request, 'index.html')