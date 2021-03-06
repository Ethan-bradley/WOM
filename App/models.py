from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from collections import OrderedDict
from picklefield.fields import PickledObjectField

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Country(models.Model):
	name = models.CharField(max_length=100)
	color = models.CharField(max_length=50, default='#ffffff')

	def __str__(self):
		return self.name

class Game(models.Model):
	name = models.CharField(max_length=100)
	host = models.ForeignKey(User, on_delete=models.CASCADE)
	num_players = models.IntegerField(default=5)
	curr_num_players = models.IntegerField(default=0)
	color = models.CharField(max_length=50, default='#ffffff')
	#players = ManyToManyField("Player")
	#hexes = ManyToManyField("Hexes")
	#TradeEngine = PickledObjectField()
	GameEngine = PickledObjectField(default="")

class Player(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	host = models.BooleanField()
	game = models.ForeignKey("Game", on_delete=models.CASCADE, default="")
	country = models.ForeignKey("Country", on_delete=models.CASCADE, default="")
	#Whether ready or not for the next turn
	ready = models.BooleanField(default=False)
	color = models.CharField(max_length=50, default='#ffffff')
	#Country = PickledObjectField()
	#Government Variables:
	IncomeTax = models.FloatField(default=0.2)
	CorporateTax = models.FloatField(default=0.1)
	Welfare = models.FloatField(default=0.7)
	Education = models.FloatField(default=0.3)
	Military = models.FloatField(default=0)
	Bonds = models.FloatField(default=0)
	MoneyPrinting = models.IntegerField(default=200)

	#Graph Images
	GoodsPerCapita = models.ImageField(default='default_graph.png', upload_to='graphs')
	Inflation = models.ImageField(default='default_graph.png', upload_to='graphs')
	RealGDP = models.ImageField(default='default_graph.png', upload_to='graphs')
	Employment = models.ImageField(default='default_graph.png', upload_to='graphs')

	def __str__(self):
		return self.name

	def get_country(self):
		return self.game.GameEngine.get_country_by_name(self.country.name)

	def get_trade_var(self, var):
		return self.game.GameEngine.get_trade(self.game.GameEngine.get_country_index(self.country.name), var)

class Tariff(models.Model):
	curr_player = models.ForeignKey("Player", on_delete=models.CASCADE, default="")
	name = models.CharField(max_length=100)
	game = models.ForeignKey("Game", on_delete=models.CASCADE, default="")
	#players = models.ManyToManyField("Player")
	#for i in range(0,4):
	#	i = models.DecimalField(max_digits=70, decimal_places=50)
class IndTariff(models.Model):
	controller = models.ForeignKey(Tariff, db_index=True, on_delete=models.CASCADE)
	#key = models.CharField(max_length=100)
	key = models.ForeignKey("Player", on_delete=models.CASCADE)
	tariffAm = models.FloatField(default=0)

class Hexes(models.Model):
	hexNum = models.IntegerField()
	game = models.ForeignKey("Game", on_delete=models.CASCADE)
	controller = models.ForeignKey("Player", on_delete=models.CASCADE)
	color = models.CharField(max_length=50, default='#ffffff')
	start_country = models.ForeignKey("Country", on_delete=models.CASCADE, default='')
	name = models.CharField(max_length=50, default='none')
	center = models.BooleanField(default=False)
	water = models.BooleanField(default=False)
	xLocation = models.IntegerField(default=0)
	yLocation = models.IntegerField(default=0)
	population = models.IntegerField()
	capital = models.IntegerField(default=0)
	oil = models.IntegerField(default=0)
	iron = models.IntegerField(default=0)
	coal = models.IntegerField(default=0)
	wheat = models.IntegerField(default=0)
	def __str__(self):
		return self.name

class Economic(models.Model):
	hexnum = models.OneToOneField("Hexes", on_delete=models.CASCADE)
	controller = models.CharField(max_length=100)
	player_controller = models.OneToOneField("Player", on_delete=models.CASCADE)
	factory_num = models.IntegerField()
	resentment = models.DecimalField(max_digits=70, decimal_places=50)
	steel_prod = models.DecimalField(max_digits=70, decimal_places=50)
	oil_prod = models.DecimalField(max_digits=70, decimal_places=50)
	welfare = models.DecimalField(max_digits=70, decimal_places=50)
	population = models.DecimalField(max_digits=70, decimal_places=50)

class Army(models.Model):
	game = models.ForeignKey("Game", on_delete=models.CASCADE)
	size = models.IntegerField()
	controller = models.ForeignKey("Player", on_delete=models.CASCADE)
	naval = models.BooleanField()
	location = models.ForeignKey("Hexes", on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	moved = models.BooleanField(default=False)
	max_movement = models.IntegerField(default=1)

	def __str__(self):
		return self.name

class PolicyGroup(models.Model):
	game = models.ForeignKey("Game", on_delete=models.CASCADE)
	player = models.ForeignKey("Player", on_delete=models.CASCADE)
	name = models.CharField(max_length=50, default='none') 

class Policy(models.Model):
	policy_group = models.ForeignKey("PolicyGroup", on_delete=models.CASCADE)
	game = models.ForeignKey("Game", on_delete=models.CASCADE, default="")
	player = models.ForeignKey("Player", on_delete=models.CASCADE, default="")
	name = models.CharField(max_length=50, default='none')
	applied = models.BooleanField(default=False)
	SavingsEffect = models.FloatField(default=0)
	ConsumptionEffect = models.FloatField(default=0)
	WelfareEffect = models.FloatField(default=0)
	InequalityEffect = models.FloatField(default=0)
	HealthSpend = models.FloatField(default=0)
	Healthcare = models.IntegerField(default=0)
	ConsumerLoans = models.FloatField(default=0)
	Education = models.FloatField(default=0)
	GovGoods = models.FloatField(default=0)
	WageEffect = models.FloatField(default=0)
	PopEffect = models.FloatField(default=0)

class Pops(models.Model):
	game = models.ForeignKey("Game", on_delete=models.CASCADE)
	EducationLevel = models.IntegerField(default=0)
	Income = models.FloatField(default=0)
	Occupation = models.CharField(max_length=50, default='Unemployed')
	Population_size = models.IntegerField(default=0)
	trust = models.IntegerField(default=100)
	Faction = models.ForeignKey("Faction", on_delete=models.CASCADE, default="")

class Faction(models.Model):
	game = models.ForeignKey("Game", on_delete=models.CASCADE)
	name = models.CharField(max_length=50, default='NoName')
	controller = models.ForeignKey("Player", on_delete=models.CASCADE, default="")

class PolicySupport(models.Model):
	game = models.ForeignKey("Game", on_delete=models.CASCADE)
	controller = models.ForeignKey("Player", on_delete=models.CASCADE, default="")
	Faction = models.ForeignKey("Faction", on_delete=models.CASCADE, default="")
	PolicyAssociated = models.ForeignKey("Policy", on_delete=models.CASCADE, default="")
	