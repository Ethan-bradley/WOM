from django.contrib import admin
from .models import Post
from .models import Player
from .models import Tariff
from .models import Hexes
from .models import Economic
from .models import Game, IndTariff, Army, Country, Policy, PolicyGroup

admin.site.register(Post)
admin.site.register(Player)
admin.site.register(Tariff)
admin.site.register(Hexes)
admin.site.register(Economic)
admin.site.register(Game)
admin.site.register(IndTariff)
admin.site.register(Army)
admin.site.register(Country)
admin.site.register(PolicyGroup)
admin.site.register(Policy)
# Register your models here.
