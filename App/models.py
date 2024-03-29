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
	large = models.BooleanField(default=False)

	def __str__(self):
		return self.name
#Game Class
class Game(models.Model):
	name = models.CharField(max_length=100)
	host = models.ForeignKey(User, on_delete=models.CASCADE)
	num_players = models.IntegerField(default=5)
	curr_num_players = models.IntegerField(default=0)
	color = models.CharField(max_length=50, default='#ffffff')
	neutral = models.CharField(max_length=100,default="Neutral")
	board_size = models.IntegerField(default=7)
	years_per_turn = models.IntegerField(default=1)
	load_complete = models.BooleanField(default=False)
	online = models.BooleanField(default=False)
	game_started = models.BooleanField(default=False)
	#players = ManyToManyField("Player")
	#hexes = ManyToManyField("Hexes")
	#TradeEngine = PickledObjectField()
	GameEngine = PickledObjectField(default="")
	GoodsPerCapita = models.ImageField(default='default_graph.png', upload_to='graphs')
	Inflation = models.ImageField(default='default_graph.png', upload_to='graphs')
	Resentment = models.ImageField(default='default_graph.png', upload_to='graphs')
	Employment = models.ImageField(default='default_graph.png', upload_to='graphs')
	InterestRate = models.ImageField(default='default_graph.png', upload_to='graphs')
	GoodsBalance = models.ImageField(default='default_graph.png', upload_to='graphs')
	ScienceArr = models.ImageField(default='default_graph.png', upload_to='graphs')


class Player(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	host = models.BooleanField()
	game = models.ForeignKey("Game", on_delete=models.CASCADE, default="")
	country = models.ForeignKey("Country", on_delete=models.CASCADE, default="")
	#Whether ready or not for the next turn
	ready = models.BooleanField(default=False)
	color = models.CharField(max_length=50, default='#ffffff')
	robot = models.BooleanField(default=False)
	projection_unloaded = models.BooleanField(default=True)
	#Country = PickledObjectField()
	#Government Variables:
	IncomeTax = models.FloatField(default=0.05)
	CorporateTax = models.FloatField(default=0.0)
	Welfare = models.FloatField(default=0.0)
	AdditionalWelfare= models.FloatField(default=0)
	Education = models.FloatField(default=0.01)
	Military = models.FloatField(default=0.01)
	Bonds = models.FloatField(default=0)
	Interest_Rate = models.FloatField(default=0.1)

	#Science Investment
	InfrastructureInvest = models.FloatField(default=0.0)
	#CapitalInvestment = models.FloatField(default=0.0)
	ScienceInvest = models.FloatField(default=0.0)
	TheoreticalInvest = models.FloatField(default=0.0)
	PracticalInvest = models.FloatField(default=0.0)
	AppliedInvest = models.FloatField(default=0.0)

	#Restrictions
	investment_restriction = models.FloatField(default=0.0)


	#Graph Images
	GoodsPerCapita = models.ImageField(default='default_graph.png', upload_to='graphs')
	Inflation = models.ImageField(default='default_graph.png', upload_to='graphs')
	RealGDP = models.ImageField(default='default_graph.png', upload_to='graphs')
	Employment = models.ImageField(default='default_graph.png', upload_to='graphs')
	GovBudget = models.ImageField(default='default_graph.png', upload_to='graphs')
	tradeBalance = models.ImageField(default='default_graph.png', upload_to='graphs')
	GDPPerCapita = models.ImageField(default='default_graph.png', upload_to='graphs')
	InterestRate = models.ImageField(default='default_graph.png', upload_to='graphs')
	Capital = models.ImageField(default='default_graph.png', upload_to='graphs')
	GoodsProduction = models.ImageField(default='default_graph.png', upload_to='graphs')
	GDP = models.ImageField(default='default_graph.png', upload_to='graphs')
	GDPGrowth = models.ImageField(default='default_graph.png', upload_to='graphs')

	def __str__(self):
		return self.name

	def get_country(self):
		return self.game.GameEngine.get_country_by_name(self.country.name)

	def modify_country(self, attr, set_am):
		self.game.GameEngine.modify_country_by_name(self.country.name, attr, set_am)
		self.game.save()

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
	tariffAm = models.FloatField(default=0.1)
	sanctionAm = models.FloatField(default=0)
	moneySend = models.FloatField(default=0)
	militarySend = models.FloatField(default=0)
	nationalization = models.FloatField(default=1.0)

class PlayerProduct(models.Model):
	curr_player = models.ForeignKey("Player", on_delete=models.CASCADE, default="")
	name = models.CharField(max_length=100)
	game = models.ForeignKey("Game", on_delete=models.CASCADE, default="")
	#players = models.ManyToManyField("Player")
	#for i in range(0,4):
	#	i = models.DecimalField(max_digits=70, decimal_places=50)
class Product(models.Model):
	controller = models.ForeignKey("PlayerProduct", db_index=True, on_delete=models.CASCADE)
	#key = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	exportRestriction = models.FloatField(default=1)
	subsidy = models.FloatField(default=0.125)

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
	resentment = models.DecimalField(default=0.0,max_digits=70, decimal_places=50)
	oil = models.IntegerField(default=0)
	iron = models.IntegerField(default=0)
	coal = models.IntegerField(default=0)
	wheat = models.IntegerField(default=0)
	university_level = models.IntegerField(default=1)
	MODES = [('Fo', 'Food'), ('Ed', 'Education'), ('Cl', 'Clothes'), ('Se', 'Services'), 
                        ('Ho', 'Housing'), ('Co', 'Construction'), ('He', 'Healthcare'), ('Mi', 'Military'), 
                        ('ME', 'MedicalEquipment'), ('St', 'Steel'), ('Cr', 'Crops'), ('Ir', 'Iron'), 
                        ('Coa', 'Coal'), ('Oi', 'Oil'), ('Tr', 'Transport'), ('Ma', 'Machinery'), 
                        ('De', 'Deposits'), ('Ph', 'Physics'), ('Bi', 'Biology'), ('Ch', 'Chemistry'), ('No','None')]

	specialty = models.CharField(max_length=3,choices=MODES,default='No')
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
	max_movement = models.IntegerField(default=2)

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

class MapInterface(models.Model):
	game = models.ForeignKey("Game", on_delete=models.CASCADE)
	controller = models.ForeignKey("Player", on_delete=models.CASCADE, default="")
	POLITICAL = 'PO'
	RESOURCES = 'RE'
	MODES = [
	(POLITICAL, 'Political'),
	(RESOURCES, 'Resources'),
	]
	mode = models.CharField(max_length=2,choices=MODES,default=POLITICAL)

class GraphInterface(models.Model):
	game = models.ForeignKey("Game", on_delete=models.CASCADE)
	controller = models.ForeignKey("Player", on_delete=models.CASCADE, default="")
	INCOMETAX = 'Income_Tax'
	CORPORATETAX = 'Corporate_Tax'
	WELFARE = 'Welfare'
	EDUCATION = "EducationSpend"
	SCIENCE = "Science"
	INFRASTRUCTURE = "Infrastructure"
	MILITARY = "MilitarySpend"
	MONEY = "InterestRate"
	IRON = "Iron"
	CROPS = "Crops"
	COAL = 'Coal'
	OIL = 'Oil'
	FOOD = 'Food'
	CONSUMER = 'Services'
	STEEL = 'Steel'
	MACHINERY = 'Machinery'
	IRONPROD = "IronP"
	WHEATPROD = "WheatP"
	COALPROD = 'CoalP'
	OILPROD = 'OilP'
	FOODPROD = 'FoodP'
	CONSUMERPROD = 'ServicesP'
	STEELPROD = 'SteelP'
	MACHINERYPROD = 'MachineryP'
	MODES = [
	(INCOMETAX, 'Income Tax'),
	(CORPORATETAX, 'Corporate Tax'),
	(WELFARE, 'Welfare'),
	(EDUCATION, 'Education'),
	(SCIENCE, 'Science'),
	(INFRASTRUCTURE, 'Infrastructure Spending'),
	(MILITARY, 'Military Spending'),
	(MONEY, 'Interest Rates'),
	(IRON,'Iron Prices'),
	(CROPS, 'Crop Prices'),
	(COAL, 'Coal Prices'),
	(OIL, 'Oil Prices'),
	(FOOD, 'Food Prices'),
	(CONSUMER, 'Services Prices'),
	(STEEL, 'Steel Prices'),
	(MACHINERY, 'Machinery Prices'),
	(IRONPROD,'Iron Production'),
	(WHEATPROD, 'Wheat Production'),
	(COALPROD, 'Coal Production'),
	(OILPROD, 'Oil Production'),
	(FOODPROD, 'Food Production'),
	(CONSUMERPROD, 'Services Production'),
	(STEELPROD, 'Steel Production'),
	(MACHINERYPROD, 'Machinery Production')
	]
	mode = models.CharField(max_length=20,choices=MODES,default=INCOMETAX)

class GraphCountryInterface(models.Model):
	game = models.ForeignKey("Game", on_delete=models.CASCADE)
	controller = models.ForeignKey("Player", on_delete=models.CASCADE, default="")
	country = models.ForeignKey("Country", on_delete=models.CASCADE, default="")
	large = models.BooleanField(default=False)

class Notification(models.Model):
	game = models.ForeignKey("Game", on_delete=models.CASCADE)
	message = models.TextField()
	year = models.IntegerField(default=0)