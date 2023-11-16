from .models import Game, Player, IndTariff, Tariff, Army, Policy, PolicyGroup, Hexes, PlayerProduct, Product, Notification
from .forms import NewGameForm, IndTariffForm, JoinGameForm, AddIndTariffForm, AddTariffForm, NextTurn, ResetTurn
#from .GameEconModel import Country
#from .TradeModel import Trade
from .EconHelper import CreationManager, Manager, trade_diagram, Market
from .EconHelper import Government
from django.core.files import File
from .HexList import HexList
from .HexList2 import HexList2
from .ArmyCombat import ArmyCombat
from django.db.models.fields import *
import os
import matplotlib.pyplot as plt
import matplotlib
import math
import requests
import types
import matplotlib.cm as cm
import plotly.graph_objects as go
import plotly.express as px
import json

class CustomObject:
    def __init__(self, name, attributes):
        self.name = name
        self.__dict__.update(attributes)

class GameEngine():
	def __init__(self, num_players, nameListInput, gameName):
		online = True
		self.nameList = nameListInput
		self.EconEngines = []
		CountryList = nameListInput#['Neutral','Spain','UK','France','Germany','Italy']
		self.CountryNameList = CountryList
		self.nameList = CountryList
		self.gameName = gameName
		if not online:
			good_names = ['Deposits','Loans','UnskilledLabour','Farmer','Teacher','Miner','Doctor','Engineer','Metallurgist','Physicist','Education','Food','Clothes','Services','Housing','Construction','Healthcare','Military','MedicalEquipment','Steel','Crops','Iron','Coal','Oil','Transport','Machinery']+CountryList+['Money']
			good_types = ['Consumer','Loans','Labour',        'Labour',  'Labour', 'Labour',      'Labour','Labour','Labour','Labour',     'Consumer','Consumer','Consumer','Consumer','Consumer','Capital','Consumer','Other',    'Capital','Capital','Raw','Raw','Raw','Raw',           'Transport','Capital']+['ForeignCurrency' for i in range(len(CountryList))]+['Money']
			industry_types = ['Deposits','Loans','Labour',    'Labour',       'Labour', 'Labour',  'Labour','Labour','Labour','Labour', 'Education','Food',    'Food','Services','Construction','Construction','Health','Military','HealthEquipment','Steel','Agriculture','Iron','Coal','Oil','Transport','Machinery']+['ForeignCurrency' for i in range(len(CountryList))]+['Money']
			transportable_indexes = [11,12,17,18,19,20,21,22,23,25,len(good_names)-1]
			num_households = 30 #30
			num_corp_per_industry = [2 for i in range(len(good_names))] #10

			industry_types2 = ['Deposits','Loans','Labour',    'Labour',       'Labour', 'Labour',  'Labour','Labour','Labour','Labour', 'Education','Food',    'Food','Services','Construction','Construction','Health','Military','HealthEquipment','Steel','Agriculture','Iron','Coal','Oil','Transport','Machinery']+['ForeignCurrency' for i in range(len(CountryList))]+['Chemistry','Physics','Biology','Money']
			industry_value_dict = {
			    'Agriculture':[['Machinery',0.4], ['Farmer',0.2], ['Oil', 0.2]],
			    'Food':[['Construction', 0.2],['Machinery',0.3], ['Crops',0.3], ['UnskilledLabour',0.2]],
			    'Manufacturing':[['Machinery',0.35], ['Construction',0.1], ['Steel',0.15],['UnskilledLabour',0.45]],
			    'Military':[['Machinery',0.15], ['Construction',0.1], ['Steel',0.1], ['Oil',0.1], ['Metallurgist',0.2], ['Engineer',0.35]],
			    'Steel':[['Machinery',0.4], ['Iron',0.1],['Coal',0.1],['Metallurgist',0.4]],
			    'Services': [['Machinery',0.5], ['Oil',0.1], ['UnskilledLabour',0.4]],
			    'Health':[['MedicalEquipment',0.3], ['Construction',0.1], ['UnskilledLabour',0.1], ['Doctor',0.5]],
			    'HealthEquipment':[['Machinery',0.3],['Engineer',0.6]],
			    'Mining':[['Machinery',0.6], ['Miner',0.2]],
			    'Oil':[['Machinery',0.7], ['Miner',0.3]],
			    'Iron':[['Machinery',0.7], ['Miner',0.3]],
			    'Coal':[['Machinery',0.7], ['Miner',0.3]],
			    'Transport':[['Construction',0.33],['Oil',0.3], ['UnskilledLabour',0.37]],
			    'Construction':[['Machinery',0.3], ['Oil', 0.1], ['UnskilledLabour',0.2], ['Engineer',0.4]],
			    'Machinery':[['Machinery',0.4], ['Steel',0.1], ['Metallurgist',0.2], ['Engineer',0.3]],
			    'Deposits':[['Loans',0.4],['Construction',0.2]] + [[i,(1/len(CountryList))*0.2] for i in CountryList] + [['Engineer',0.2]],
			    'Loans':[['Loans',0.5], ['Deposits',0.5]],
			    'Education':[['Construction',0.3], ['Teacher',0.7]],
			    'Chemistry':[['Machinery',0.3], ['Engineer',0.7]],
			    'Biology':[['Machinery',0.3], ['Doctor',0.7]],
			    'Physics':[['Machinery',0.3], ['Physicist',0.7]],
			}
			researcher_indexes, industry_dict = self.create_industry_dict(good_names, good_types, industry_types2,industry_value_dict)
			education_array = [[2,0],[3,7],[4,2],[5,2],[6,4],[7,7],[8,10],[8,10]]
			final_goods = ['Education','Food','Clothes','Services','Housing','Construction','Healthcare','Military','Transport','Capital']
			temp = 0
			if num_players > 7:
				#for i in range(0,num_players):
				#self.EconEngines.append(Country())
				#temp = num_players - 7
				#num_players2 = 7
				hex_list = HexList2().hexList
				#hex_list = HexList().hexList2
				#for i in range(0,num_players2):
				#self.EconEngines[i].run_turn(13)
			else:
				hex_list = HexList().hexList
		
			M = Manager(hex_list, good_names, good_types, industry_types, num_households, num_corp_per_industry, industry_dict, CountryList, transportable_indexes, education_array, final_goods, researcher_indexes)
			self.EconEngines = M.CountryList
			self.TradeEngine = M
		self.ArmyCombat = ArmyCombat()
		self.var_list = ['Welfare','Education','Military','Infrastructure','Science']
		self.variable_list = ['Welfare','Education','Military','InfrastructureInvest','ScienceInvest']
		self.save_variable_list(self.var_list, num_players)
		#all_players = Player.objects.filter(game=g)
		countries = self.nameList
		self.TarriffsArr = {i:{k:[0.1 for i in range(0,8)] for k in countries} for i in countries}
		#import pdb; pdb.set_trace()
		self.SanctionsArr = {i:{k:[0 for i in range(0,8)] for k in countries} for i in countries}
		self.ForeignAid = {i:{k:[0 for i in range(0,8)] for k in countries} for i in countries}
		self.MilitaryAid = {i:{k:[0 for i in range(0,8)] for k in countries} for i in countries}
		if not online:
			M.run_turn(8) #3 #8 #1
		else:
		    url = "https://fgpbj614t7.execute-api.us-east-2.amazonaws.com/dev/econhelper?transactionId=124&newGame=True&gameName="+gameName+"&runEngine=False&years_run=1&num_players="+str(num_players)
		    header = {}
		    requests.get(url, headers=header)
		#trade_diagram(CountryList, self.TradeEngine.trade_balance, "trade")
	def run_more_countries(self, num_players):
		if num_players > 5:
			for i in range(7,num_players):
				self.EconEngines[i].run_turn(13)
	def run_more(self):
		print("Running more")
		self.TradeEngine.run_turn(2) #3
		trade_diagram(self.CountryNameList, self.TradeEngine.trade_balance, "trade")
	def run_start_trade(self, g, turn_num=7):
		self.run_engine(g)
		for i in range(0,turn_num-2):
			self.run_engine(g, False)
		self.run_engine(g)
	def start_capital(self, g):
		all_players = Player.objects.filter(game=g)
		for p in all_players:
			index = self.nameList.index(p.country.name)
			country = self.get_country(index)
			#self.apply_hex_number(g, p, country)
			self.start_hex_number(g, p, country)

	def run_engine(self, g, graphs=True, years_run=1, projection=False):
		online = g.online
		all_players = Player.objects.filter(game=g)
		# Define the headers, including "Content-Type" as "application/json"
		headers = {
				"Content-Type": "application/json"
		}
		"""if online:
			url = "https://fgpbj614t7.execute-api.us-east-2.amazonaws.com/dev/econhelper?transactionId=124&newGame=False&gameName="+gameName+"&runEngine=False&years_run=1&num_players=1"
			header = {}
			data = requests.get(url, headers=header).json()
			
			#import pdb; pdb.set_trace()
			myGame = self.create_objects_from_dict(data)['newObject']
			self.EconEngines = myGame.EconEngines
			self.TradeEngine = myGame.TradeEngine
			self.TradeEngine.CountryList = myGame.EconEngines"""
		if graphs and self.EconEngines[0].time > 5:
			self.set_vars(g, all_players, projection)
		if not projection:
			if g.num_players > 1:
				for p in all_players:
					f = ResetTurn(instance=p)
					pla = f.save(commit=False)
					pla.ready = False
					pla.projection_unloaded = True
					pla.save()
				neutral_player2 = Player.objects.filter(name="Neutral")[0]
				neutral_player2.ready = True
				neutral_player2.save()
			else:
				p = Player.objects.filter(user=g.host)[0]
				print(p.name)
				f = ResetTurn(instance=p)
				pla = f.save(commit=False)
				pla.ready = False
				pla.save()
			all_armies = Army.objects.filter(game=g)
			for a in all_armies:
				a.moved = False
			self.ArmyCombat.doCombat(g)
		#Running engine
		#self.fix_variables()"""	
		if not online:
			self.TradeEngine.run_turn(years_run)
			#e.save_GoodsPerCapita('default_graph.png')
		else:
			responseObject = {}
			json_payload = manager_to_json(self.TradeEngine)
			json_payload = json.dumps(json_payload)
			# Send the POST request with the JSON body
			api_url = "https://fgpbj614t7.execute-api.us-east-2.amazonaws.com/dev/econhelper?transactionId=124&newGame=False&gameName="+self.gameName+"&runEngine=True&years_run=1&num_players=1"
			requests.post(api_url, data=json_payload, headers=headers).json()
			#if data['statusCode'] == '200':
			#myGame = self.create_objects_from_dict(data)['newObject']
			#self.EconEngines = myGame.EconEngines
			#self.TradeEngine = myGame.TradeEngine
			#self.TradeEngine.CountryList = myGame.EconEngines
		print('running engine')
		#for p in all_players:
		#index = self.nameList.index(p.country.name)
		#country = self.get_country(index)
		#self.apply_hex_number(g, p, country)
		if graphs and not online:
			trade_diagram(self.CountryNameList, self.TradeEngine.trade_balance, "trade")
			#self.create_graphs(g, all_players)
			#self.create_compare_graph(self.EconEngines, self.nameList, 17, ['GoodsPerCapita','InflationTracker','ResentmentArr','EmploymentRate','ConsumptionArr','InterestRate','GoodsBalance','ScienceArr'],'',g.name, g)
		return [self.EconEngines, self.TradeEngine]

	import json

	def create_objects_from_dict(self, data):
	    objects = {}
	    for key, value in data.items():
	        if isinstance(value, dict):
	            if key == 'TradeEngine':
	                obj = CustomObject2(name=key, attributes=self.create_objects_from_dict(value))
	            else:
	                obj = CustomObject(name=key, attributes=self.create_objects_from_dict(value))
	            objects[key] = obj
	        elif isinstance(value, list):
	            temp_list = []
	            for index, item in enumerate(value):
	                if isinstance(item, dict):
	                    # Handle dictionaries within a list as child objects.
	                    obj_name = f"{key}[{index}]"
	                    temp_list.append(CustomObject(name=obj_name, attributes=self.create_objects_from_dict(item)))
	                else:
	                    # If the item is not a dictionary, create an attribute with the index as the name and the item as the value.
	                    temp_list.append(item)
	            objects[key] = temp_list
	        else:
	            # If the value is not a dictionary, create an attribute with the key as the name and the value as the value.
	            objects[key] = value

	    return objects

	def game_combat(self, g):
		self.ArmyCombat.doCombat(g)

	def run_graphs(self, g):
		all_players = Player.objects.filter(game=g)
		#self.create_graphs(g, all_players)
		self.create_compare_graph(self.EconEngines, self.nameList, 17, ['GoodsPerCapita','InflationTracker','ResentmentArr','EmploymentRate','ConsumptionArr','InterestRate','GoodsBalance','ScienceArr'],'',g.name, g)
	def get_country(self, index):
		return self.EconEngines[index]

	def get_country_by_name(self, name):
		index = self.nameList.index(name)
		country = self.get_country(index)
		return country

	def get_country_index(self, name):
		index = self.nameList.index(name)
		return index

	def modify_country_by_name(self, name, attr, set_am):
		index = self.nameList.index(name)
		country = self.get_country(index)
		setattr(country, attr, set_am)
		if getattr(country, attr) < 1:
			setattr(country, attr, set_am)

	def get_trade(self, index, var):
		if var == 0:
			return self.TradeEngine
		elif var == 1:
			return self.TradeEngine.currencyReserves[index]
		elif var == 2:
			return self.TradeEngine.exchangeRates[index]
		elif var == 3:
			return self.TradeEngine.Tariffs[index]

	def create_compare_graph(self, CountryList, CountryName, start, attribute_list, file_path, game_name, g):
		if (os.path.exists('.'+g.GoodsPerCapita.url) and g.GoodsPerCapita.name != 'default_graph.png'):
			os.remove('.'+g.GoodsPerCapita.url)
			os.remove('.'+g.Inflation.url)
			os.remove('.'+g.Resentment.url)
			os.remove('.'+g.Employment.url)
			os.remove('.'+g.Consumption.url)
			os.remove('.'+g.InterestRate.url)
			os.remove('.'+g.GoodsBalance.url)
			os.remove('.'+g.ScienceArr.url)
		a = []
		matplotlib.use('Agg')
		for j in range(0, len(attribute_list)):
			plt.clf()
			plt.title(attribute_list[j])
			for i in range(0,len(CountryList)):
				plt.plot(getattr(CountryList[i],attribute_list[j])[start:],label=CountryName[i])
				plt.ylabel(attribute_list[j])
				plt.xlabel('Years')
				plt.legend()
			plt.savefig(file_path+game_name+attribute_list[j])
			a.append(file_path+game_name+attribute_list[j])
			plt.clf()
		plt.close()

		with open(a[0] +'.png', 'rb') as f:
			g.GoodsPerCapita = File(f)
			g.save()
		os.remove(a[0] +'.png')

		with open(a[1] +'.png', 'rb') as f:
			g.Inflation = File(f)
			g.save()
		os.remove(a[1] +'.png')
		
		with open(a[2] +'.png', 'rb') as f:
			g.Resentment = File(f)
			g.save()
		os.remove(a[2] +'.png')

		with open(a[3] +'.png', 'rb') as f:
			g.Employment = File(f)
			g.save()
		os.remove(a[3] +'.png')

		with open(a[4] +'.png', 'rb') as f:
			g.Consumption = File(f)
			g.save()
		os.remove(a[4] +'.png')

		with open(a[5] +'.png', 'rb') as f:
			g.InterestRate = File(f)
			g.save()
		os.remove(a[5] +'.png')

		with open(a[6] +'.png', 'rb') as f:
			g.GoodsBalance = File(f)
			g.save()
		os.remove(a[6] +'.png')

		with open(a[7] +'.png', 'rb') as f:
			g.ScienceArr = File(f)
			g.save()
		os.remove(a[7] +'.png')

	def set_vars(self, g, all_players, projection=False):
		transfer_array = [[0 for j in range(0,len(self.EconEngines))] for i in range(0,len(self.EconEngines))]
		military_transfer = [[0 for j in range(0,len(self.EconEngines))] for i in range(0,len(self.EconEngines))]
		for p in all_players:
			index = self.nameList.index(p.country.name)
			country = self.get_country(index)

			#self.calculate_differences(g, p, country)
			#self.get_hex_numbers(g, p, country)

			country.IncomeTax = p.IncomeTax
			country.CorporateTax = p.CorporateTax
			#country.GovGoods = p.Education + p.Military
			#revenue = p.IncomeTax*country.money[0] + p.CorporateTax*country.money[4]
			
			country.interest_rate = p.Interest_Rate
			country.deposit_rate = p.Interest_Rate - 0.03
			
			#import pdb; pdb.set_trace();
			welfare = p.Welfare + p.AdditionalWelfare
			country.spending[country.EducationIndex] = p.Education
			country.spending[country.MilitaryIndex] = p.Military
			#country.GovWelfare = p.Welfare + p.AdditionalWelfare
			country.GovWelfare = welfare
			#Investment
			#total_gov_money = revenue + country.BondWithdrawl
			#total_investor_money = country.money[4]*country.InvestmentRate

			#country.GovernmentInvest = gov_invest #p.InfrastructureInvest + p.ScienceInvest
			#total_money = revenue*country.GovernmentInvest + total_investor_money
			country.InfrastructureInvest = p.InfrastructureInvest
			country.ResearchSpend = max(p.ScienceInvest, 0.005)
			#country.QuickInvestment = p.CapitalInvestment
			#import pdb; pdb.set_trace();

			self.TradeEngine.investment_restrictions[index] = p.investment_restriction

			#Rebellions!!!! EDIT THIS
			#if country.Resentment > 0.06:
			#self.rebel(g, p, country.Resentment)
			#Tarriffs
			#import pdb; pdb.set_trace()
			#try:
			tar = Tariff.objects.filter(game=g, curr_player=p)
			if len(tar) != 0:
				tar = tar[0]
				k = IndTariff.objects.filter(controller=tar)

				count = 0
				for t in k:
					count = self.TradeEngine.CountryNameList.index(t.key.country.name)
					#Save data to array
					self.TarriffsArr[t.key.country.name][p.country.name].append(t.tariffAm)
					self.SanctionsArr[t.key.country.name][p.country.name].append(t.sanctionAm)
					self.ForeignAid[t.key.country.name][p.country.name].append(t.moneySend)
					self.MilitaryAid[t.key.country.name][p.country.name].append(t.militarySend)
					#save data to engines.
					self.TradeEngine.Tariffs[index][count] = t.tariffAm
					self.TradeEngine.Sanctions[index][count] = t.sanctionAm
					transfer_array[index][count] = t.moneySend
					military_transfer[index][count] = t.militarySend
					#import pdb; pdb.set_trace()
					#ADD IN NATIONALIZATION
					#self.TradeEngine.foreign_investment[index][count] = self.TradeEngine.foreign_investment[count][index]*t.nationalization
					count += 1
			#Append variables
			#import pdb; pdb.set_trace()
			self.append_variable_list(self.var_list, self.variable_list, index, p)
			#Product subsidies/restrictions FIX THIS
			productP = PlayerProduct.objects.filter(game=g, curr_player=all_players[index])
			if len(productP) != 0:
				productP = productP[0]
				products = Product.objects.filter(controller=productP)
				country_index = self.nameList.index(p.country.name)
				for product in products:
					index = self.TradeEngine.good_names.index(product.name)
					self.TradeEngine.restrictions[country_index][index] = product.exportRestriction
					country.subsidies[index] = product.subsidy
			#except:
			#	print("Index out of range error!")
			
		#ADD these functions:
		def trade_money(self, transfer_array):
			#i is the destination country, j is the source country.
			Countries = self.CountryList
			for i in range(0, len(Countries)):
			  for j in range(0, len(Countries)):
			    #am = transfer_array[j][i]*(self.exchangeRateArr[j][-1]/self.exchangeRateArr[i][-1])
			    am2 = transfer_array[j][i]
			    Countries[i].goods_supply[self.currency_indexes[j]] += am2
			    Countries[j].Government_Savings -= am2
			    Countries[j].deficit -= am2

		#Transfer military goods between countries. Transfer array is similar to tariff array, each row represnting the transfer wishes of one country
		def trade_military_goods(self, transfer_array):
			#i is the destination country, j is the source country.
			Countries = self.CountryList
			for i in range(0, len(Countries)):
			  for j in range(0, len(Countries)):
			    am = transfer_array[j][i]
			    if Countries[j].goods_supply[Countries[j].MilitaryIndex] > am:
			      Countries[i].goods_supply[Countries[i].MilitaryIndex] += am
			      Countries[j].goods_supply[Countries[j].MilitaryIndex] -= am
			trade_money(TradeEngine, transfer_array)
			trade_military_goods(TradeEngine, military_transfer)
		if projection:
			return
		hex_list = Hexes.objects.filter(game=g, water=False)
		num_rebelled = 0
		for h in range(0, len(hex_list)):
			market_index = self.TradeEngine.location_names.index(hex_list[h].name)
			market = self.TradeEngine.market_list[market_index]
			market.universityLevel = 20*pow(2, hex_list[h].university_level - 1)
			if hex_list[h].specialty != 'None':
				market.specialty = hex_list[h].specialty
			hex_list[h].capital = int(market.output[-1])
			hex_list[h].population = int(market.population[-1])
			resentment = round(market.Resentment[-1],3)
			hex_list[h].resentment = resentment
			if resentment > 0.2 and len(hex_list) - num_rebelled > 1:
				num_rebelled += 1
				self.rebel(g, hex_list[h], resentment)
			hex_list[h].save()

	def save_variable_list(self, var_list, player_num):
		for i in var_list:
			#change to 17
			if i == "Education" or i == "Military":
				setattr(self,i,[[0.01 for i in range(0,8)] for i in range(player_num)])
			else:
				setattr(self,i,[[0.0 for i in range(0,8)] for i in range(player_num)])
	def append_variable_list(self, var_list, variable_list, index, player):
		for i in range(0,len(var_list)):
			getattr(self,var_list[i])[index].append(getattr(player, variable_list[i]))

	def create_graphs(self, g, all_players):
		for p in all_players:
			index = self.nameList.index(p.country.name)
			country = self.get_country(index)
			if not p.robot:
				if (os.path.exists('.'+p.GoodsPerCapita.url) and p.GoodsPerCapita.name != 'default_graph.png'):
					os.remove('.'+p.GoodsPerCapita.url)
					os.remove('.'+p.Inflation.url)
					os.remove('.'+p.RealGDP.url)
					os.remove('.'+p.Employment.url)
					os.remove('.'+p.GovBudget.url)
					os.remove('.'+p.tradeBalance.url)
					os.remove('.'+p.GDPPerCapita.url)
					os.remove('.'+p.InterestRate.url)
					os.remove('.'+p.Capital.url)
					os.remove('.'+p.GoodsProduction.url)
					os.remove('.'+p.GDP.url)
					os.remove('.'+p.GDPGrowth.url)
				#Graphs:
				#country.save_GoodsPerCapita('.'+p.GoodsPerCapita.url)
				a = country.save_graphs('',p.name)
				#print(a[1])
				
				with open(a[0]+'.png', 'rb') as f:
					p.GoodsPerCapita = File(f)
					p.save()
				os.remove(a[0]+'.png')

				
				with open(a[1]+'.png', 'rb') as f:
					p.Inflation = File(f)
					p.save()
				os.remove(a[1]+'.png')
				
				with open(a[2]+'.png', 'rb') as f:
					p.RealGDP = File(f)
					p.save()
				os.remove(a[2]+'.png')
				
				with open(a[3]+'.png', 'rb') as f:
					p.Employment = File(f)
					p.save()
				os.remove(a[3]+'.png')

				with open(a[4]+'.png', 'rb') as f:
					p.GovBudget = File(f)
					p.save()
				os.remove(a[4]+'.png')

				with open(a[5]+'.png', 'rb') as f:
					p.tradeBalance = File(f)
					p.save()
				os.remove(a[5]+'.png')

				with open(a[6]+'.png', 'rb') as f:
					p.GDPPerCapita = File(f)
					p.save()
				os.remove(a[6]+'.png')

				with open(a[7]+'.png', 'rb') as f:
					p.InterestRate = File(f)
					p.save()
				os.remove(a[7]+'.png')

				with open(a[8]+'.png', 'rb') as f:
					p.Capital = File(f)
					p.save()
				os.remove(a[8]+'.png')

				with open(a[9]+'.png', 'rb') as f:
					p.GoodsProduction = File(f)
					p.save()
				os.remove(a[9]+'.png')

				with open(a[10]+'.png', 'rb') as f:
					p.GDP = File(f)
					p.save()
				os.remove(a[10]+'.png')

				with open(a[11]+'.png', 'rb') as f:
					p.GDPGrowth = File(f)
					p.save()
				os.remove(a[11]+'.png')
		
			
	def calculate_differences(self, g, p, e):
	    #g = Game.objects.filter(name=g)[0]
	    #p = Player.objects.filter(name=p)[0]
		policy_list = PolicyGroup.objects.filter(game=g, player=p)
		BalanceList = [0.0 for i in range(11)]
		for pg in policy_list:
			p2 = Policy.objects.filter(policy_group=pg, applied=True)
			if len(p2) <= 0:
				continue
			p2 = p2[0]
			all_fields = p2._meta.get_fields() #_meta.fields
			count = 0
			for a in all_fields:
				if isinstance(a, FloatField):
					n = a.name
					BalanceList[count] += getattr(p2, n)
					count += 1
		#print(BalanceList[0])
		e.SavingsRate = 0.3 + BalanceList[0]
		#print(BalanceList[1])
		e.ConsumptionRate = 0.5 + BalanceList[1]
		#print(BalanceList[2])
		#p.Welfare = BalanceList[2]
		e.Wages = 0.4 + BalanceList[9]
		e.population_growth = 0.02 + BalanceList[10]
		p.save()

	def get_hex_numbers(self, g, p, e):
		hex_list = Hexes.objects.filter(game=g, controller=p, water=False)
		total_population = 0
		total_capital = 0
		total_iron = 0.01
		total_wheat = 0.01
		total_coal = 0.01
		total_oil = 0.01
		for h in hex_list:
			total_population += h.population
			total_capital += h.capital
			total_iron += h.iron
			total_wheat += h.wheat
			total_coal += h.coal
			total_oil += h.oil
		#e.Population = total_population
		#e.capital = total_capital
		e.RawResources[0] = total_iron
		e.RawResources[1] = total_wheat
		e.RawResources[2] = total_coal
		e.RawResources[3] = total_oil
		p.save()


	def apply_hex_number(self, g, p, e):
		hex_list = Hexes.objects.filter(game=g, controller=p, water=False)
		centers = []
		for h in range(0, len(hex_list)):
			if hex_list[h].center:
				centers.append(h)
		#print(centers)
		capital_list = e.create_distribution([0 for j in range(0, len(centers))], centers, e.capital - e.lastcapital, len(hex_list))
		population_list = e.create_distribution([0 for j in range(0, len(centers))], centers, e.Population - e.lastPopulation, len(hex_list))

		#e.lastPopulation = e.Population
		for h in range(0, len(hex_list)):
			print(capital_list[h])
			if not math.isnan(capital_list[h]):
				hex_list[h].capital += int(capital_list[h])
			if not math.isnan(population_list[h]):
				hex_list[h].population += int(population_list[h])
			hex_list[h].save()
			print(hex_list[h].capital)

	def start_hex_number(self, g, p, e):
		hex_list = Hexes.objects.filter(game=g, controller=p, water=False)
		centers = []
		for h in range(0, len(hex_list)):
			if hex_list[h].center:
				centers.append(h)
		#print(centers)
		capital_list = e.create_distribution([0 for j in range(0, len(centers))], centers, e.capital, len(hex_list))
		population_list = e.create_distribution([0 for j in range(0, len(centers))], centers, e.Population, len(hex_list))

		#e.lastPopulation = e.Population
		for h in range(0, len(hex_list)):
			print(capital_list[h])
			hex_list[h].capital += int(capital_list[h])
			hex_list[h].population += int(population_list[h])
			hex_list[h].save()
			print(hex_list[h].capital)

	def printTradeAms(self):
		countryNames = self.nameList
		currencyChangeReserves = self.TradeEngine.currencyChangeReserves 
		string = ""
		for i in range(0,len(currencyChangeReserves)):
			string += "Trade Portfolio of "+countryNames[i]+"\n"
		for j in range(0,len(currencyChangeReserves[0])):
			if i == j:
				continue
		string += "Exports to "+countryNames[j]+": "+str(currencyChangeReserves[i][j])+"\n"
		return string

	def printCurrencyReserves(self):
		countryNames = self.nameList
		currencyReserves = self.TradeEngine.currencyReserves 
		string = ""
		for i in range(0,len(currencyReserves)):
			string += "Currency Reserves of "+countryNames[i]+"\n"
		for j in range(0,len(currencyReserves[0])):
			if i == j:
				continue
		string += "Exports to "+countryNames[j]+": "+str(currencyReserves[i][j])+"\n"
		return string

	def printCurrencyExchange(self):
		countryNames = self.nameList
		currencyRates = self.TradeEngine.exchangeRates 
		string = ""
		for i in range(0,len(currencyRates)):
			string += " "+countryNames[i]
			string += ": "+str(currencyRates[i])+"\n"
		return string
	#Causes a province to rebel.
	def rebel(self, g, hex2, res):
		p = hex2.controller
		if p.name != "Neutral":
			neutral_player = Player.objects.filter(game=g,name="Neutral")[0]
			self.switch_hex(hex2, neutral_player, g)
			Army.objects.create(game=g, size=int(hex2.population*res),controller=neutral_player, naval=False, location=hex2, name=hex2.name+" Rebel Army")
			message2 = "In "+p.name+"'s territory a rebel army of size "+str(round(hex2.population*res*100,0))+" rose up in "+hex2.name
			turn = g.GameEngine.get_country_by_name("UK").time - 6
			Notification.objects.create(game=g, message=message2,year=turn)

	#Switches control of a hex between two players (doesn't work yet)
	def switch_hex(self, h, player_to, g):
		loser = h.controller
		#import pdb; pdb.set_trace()
		to_country = player_to.country.name
		self.TradeEngine.hex_switches.append(h.name)
		self.TradeEngine.hex_switches.append(to_country)
		self.TradeEngine.switch_hex(h.name, to_country)

		g.save()
		h.controller = player_to
		h.color = player_to.country.color

		h.save()
		player_to.save()
		loser.save()

	def create_industry_dict(self, good_names, goods_type, industry_types, industry_value_dict):
	  industry_dict = {}
	  researcher_indexes = {}
	  #labour_types = goods_type.count('Labour')
	  for i in range(0, len(industry_types) -1):
	    if (i >= len(goods_type)) or (goods_type[i] != 'Labour' and goods_type[i] != 'ForeignCurrency'):
	      industry_dict[industry_types[i]] = [0 for i in range(0,len(good_names))]
	      for j in range(len(industry_value_dict[industry_types[i]])):
	        index = good_names.index(industry_value_dict[industry_types[i]][j][0])
	        industry_dict[industry_types[i]][index] = industry_value_dict[industry_types[i]][j][1]
	      researcher_indexes[industry_types[i]] = good_names.index(industry_value_dict[industry_types[i]][-1][0])

	  return researcher_indexes, industry_dict

class CustomObject2:
	def __init__(self, name, attributes):
	    self.name = name
	    self.__dict__.update(attributes)

	def get_country(self, name):
	    return self.CountryList[self.CountryNameList.index(name)]

	def switch_hex(self, hex, to, g=None):
	    market = self.market_list[self.location_names.index(hex)]
	    prev_gov = market.government
	    prev_gov.markets.remove(market)
	    country_to = self.get_country(to)
	    country_to.markets.append(market)
	    for trader in range(0,len(market.traders)):
	        if market.traders[trader].other_market.government == country_to:
	            market.traders[trader].type2 = "Trader"
	        elif market.traders[trader].other_market.government == prev_gov:
	            market.traders[trader].type2 = "ForeignTrader"
	    market.government = country_to
	    market.households[-2] = country_to
	    market.households[-1] = country_to.TaxCollector
	    if g != None:
	        g.save()

	def budget_graph(self, country, start, file_path=None):
	    def add_trace(fig, y, net, color, title, green_num=0, red_num=0,blue_num=0, negative=1, fill2='tonexty'):
	      fig.add_trace(go.Scatter(x=[i for i in range(0,len(net))], y=[negative*y[i] + net[i] for i in range(0,len(net))],
	        fill=fill2,
	        mode='lines',
	        line_color='black',
	        fillcolor = 'rgba('+str(red_num)+', '+str(green_num)+', 0, 0.5)',
	        name=title
	        ))
	    #print('rgba('+str(red_num)+', '+str(green_num)+', '+str(blue_num)+', 0.5)')
	    def collection2(fig, collection, total, labels, net,color):
	      sum = [i for i in total]
	      add_trace(fig, total, net,'green', labels[0],155,0,0,1,None)
	      for i in range(1,len(collection)):
	        sum = [sum[j] - collection[i-1][j] for j in range(0,len(total))]
	        add_trace(fig, sum, net,'green',labels[i], (100*i)% 255)

	    def collection3(fig, collection, total, labels, net,color):
	      sum = [0 for i in total]
	      #add_trace(fig, total, net,'green', labels[0],color,0,1,None)
	      for i in range(0,len(collection)):
	        sum = [sum[j] + collection[i][j] for j in range(0,len(total))]
	        add_trace(fig, sum, net,'green',labels[i], (80*(i)) % 255, 255, (80*(i)) % 255,-1)
	    country = self.get_country(country)
	    Corporate_Tax = country.CorporateTaxArray[start:-1]
	    #print(Corporate_Tax)
	    Income_Tax = country.IncomeTaxArray[start:-1]
	    Tarriffs = country.TarriffCollectionArray[start:-1]
	    revenues = [Corporate_Tax[i] + Income_Tax[i] + Tarriffs[i] for i in range(0,len(Corporate_Tax))]
	    
	    net = [0 for i in range(0,len(country.Government_SavingsArray[start:-1]))]#country.Government_SavingsArray[start:-1] #[1000, 1200, 1100, 800]
	    collection = [Corporate_Tax, Income_Tax, Tarriffs]
	    expense = [country.GovWelfareArray[start:-1],country.InfrastructureArr[start:-1],country.ScienceBudgetArr[start:-1],country.MilitaryArr[start:-1],country.EducationArray[start:-1], country.SubsidyArr[start:-1]]
	    expenses = [sum([expense[j][i] for j in range(0,len(expense))]) for i in range(0,len(expense[0]))]
	    #print(expenses)
	    #debt = [1000, -800, -900, -1100]
	    fig = go.Figure()
	    fig.update_layout(title_text='Debt and Budget', title_x=0.5)
	    #pdb.set_trace()
	    collection2(fig, collection, revenues, ['Corporate Tax', 'Income Tax', 'Tarriffs'], net, 255)
	    fig.add_trace(go.Scatter(
	        x=[i for i in range(0,len(Corporate_Tax))],
	        y=net,
	        fill='tonexty', # fill area between trace0 and trace1
	        name='Net Savings',
	        mode='lines', line_color='black',
	        fillcolor = 'green',
	        line=dict(width=10)
	        ))
	    #pdb.set_trace()
	    collection3(fig, expense, expenses, ['Welfare', 'Infrastructure', 'Science', 'Military', 'Education','Subsidies'], net, 255)
	    if file_path == None:
	      fig.show()
	    else:
	      fig.write_html(file_path)

def to_json(self):
    # Convert list attributes to JSON while ignoring non-list attributes.
    json_data = {}
    variable_list = ['IncomeTax', 'CorporateTax', 'interest_rate', 'deposit_rate', 'GovWelfare', 'InfrastructureInvest', 'ResearchSpend']
    self_dict = self.__dict__
    for attr_name in variable_list:
    	if not isinstance(self_dict[attr_name], list):
    		json_data[attr_name] = self_dict[attr_name]
    json_data['subsidies'] = self_dict["subsidies"]
    """for attr_name, attr_value in self.__dict__.items():
        if isinstance(attr_value, list):
            if len(attr_value) > 0:
                    #elif type(attr_value[0]) == int or type(attr_value[0]) == float:
                if attr_name == "subsidies":
                	json_data[attr_name] = attr_value
                #elif not hasattr(attr_value[0], '__dict__'):
                #json_data[attr_name] = attr_value
                #else:
                #json_data[attr_name] = str(attr_value)
        elif (attr_name in variable_list):
            json_data[attr_name] = attr_value"""
    return json_data

def market_to_json(self):
    # Convert list attributes to JSON while ignoring non-list attributes.
    json_data = {}
    variable_list = ['specialty', 'universityLevel']
    self_dict = self.__dict__
    for attr_name in variable_list:
    	json_data[attr_name] = self_dict[attr_name]
    return json_data

def manager_to_json(self):
    # Convert list attributes to JSON while ignoring non-list attributes.
    json_data = {}
    #variable_list = ['hex_switches', 'investment_restrictions', 'Tariffs', 'Sanctions', 'restrictions']
    for attr_name, attr_value in self.__dict__.items():
        if attr_name == "market_dict":
                continue
        elif isinstance(attr_value, list):
            if len(attr_value) > 0:
                if attr_name == 'CountryList':
                    json_data[attr_name] = [to_json(item) for item in attr_value]
                    #json_data[attr_name] = [to_json(item) for item in attr_value]
                    #elif type(attr_value[0]) == int or type(attr_value[0]) == float:
                elif attr_name == 'market_list':
                	json_data[attr_name] = [market_to_json(item) for item in attr_value]
                elif not hasattr(attr_value[0], '__dict__') and (attr_name == 'hex_switches' or attr_name == 'investment_restrictions' or attr_name == 'Tariffs' or attr_name == 'Sanctions' or attr_name == 'restrictions'):
                    json_data[attr_name] = attr_value
            else:
                json_data[attr_name] = attr_value

    return json_data