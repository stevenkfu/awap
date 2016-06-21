from web.models import Team
from django.contrib.auth.hashers import check_password, make_password

class TeamAuthBackend(object):

    def authenticate(self, name=None, password=None):
        try:
            team = Team.objects.get(name=name)
            if check_password(password, team.password):
                print("LOG HIM IN")
                return team
            else:
                return None
        except Team.DoesNotExist:
            return None

    def get_user(self, name):
        try:
            return Team.objects.get(name=name)
        except Team.DoesNotExist:
            return None
