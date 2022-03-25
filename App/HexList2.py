from .models import Hexes, Country

class HexList2():
	def __init__(self):
		self.hexList = []
		first_row = [['Atlantic Ocean',True,0,'#3262a8','Neutral',False,0,0,0,0],['Agadir',False,40,'#d2d6d5','Neutral', False,0,1,0,0],['South Algeria',False,20,'#013220','Algeria', False,0,0,0,1],['Sahara',False,0,'#013220','Algeria', False,0,0,0,1],['Awbari',False,10,'#d2d6d5','Neutral',False,0,0,0,0], ['Kabir',False,0,'#d2d6d5','Neutral',False,0,0,0,0], ['Tazirbu', False, 10,'#d2d6d5','Neutral', True,0,0,0,1],['Mut',False,10,'#FFD700','Egypt',False,1,0,0,0],['Aswan', False, 40,'#FFD700','Egypt', False,0,1,0,0],['Red Sea',True,0,'#3262a8','Egypt',False,0,0,0,0],['Mecca', False, 100,'#006400','Saudi Arabia', True,1,0,0,0],['Riyadh', False, 70,'#006400','Saudi Arabia', True,0,0,0,1],['Saudi Arabia', False, 20,'#006400','Saudi Arabia', False,0,0,0,1],['Oman', False, 50,'#006400','Saudi Arabia', True,0,0,0,0]]
		second_row = [['Atlantic Ocean',True,0,'#3262a8','Neutral',False,0,0,0,0],['Morocco',False,100,'#d2d6d5','Neutral', False,1,0,0,0],['Bechar',False,100,'#013220','Algeria', True,0,0,0,1],['Jebil',True,70,'#013220','Algeria', False,0,0,0,0],['Tripoli',False,0,'#d2d6d5','Neutral',False,0,1,0,0], ['Ghani',False,0,'#d2d6d5','Neutral',False,0,0,0,0], ['Benghazi', False, 100,'#d2d6d5','Neutral', True,0,0,0,1],['Alexandria',False,100,'#FFD700','Egypt',True,0,1,0,0],['Cairo', False, 20,'#FFD700','Neutral', True,1,0,0,0],['Sinai', False, 40,'#FFD700','Egypt', False,0,0,0,0],['Israel', False, 70,'#d2d6d5','Neutral', True,0,1,0,0],['Jordan', False, 70,'#d2d6d5','Neutral', True,0,1,0,0],['Iraq',False,40,'#d2d6d5','Neutral', False,0,0,0,1],['Persian Gulf',True,0,'#3262a8','Neutral',False,0,0,0,0]]
		third_row = [['Atlantic Ocean',True,0,'#3262a8','Neutral',False,0,0,0,0],['Tangier',False,100,'#d2d6d5','Neutral', False,0,0,0,0],['Algeria',False,100,'#013220','Algeria', True,1,0,0,0],['Tunisia',True,70,'#013220','Algeria', False,1,0,0,0],['Mediterranean Sea',True,0,'#3262a8','Neutral',False,0,0,0,0],['Mediterranean Sea',True,0,'#3262a8','Neutral',False,0,0,0,0], ['South Ionian Sea',True,0,'#3262a8','Italy',False,0,0,0,0],['Mediterranean Sea',True,0,'#3262a8','Neutral',False,0,0,0,0],['Aegean Sea',True,0,'#3262a8','Turkey',False,0,0,0,0],['Mediterranean Sea',True,0,'#3262a8','Turkey',False,0,0,0,0],['Mediterranean Sea',True,0,'#3262a8','Neutral',False,0,0,0,0],['Syria', False, 20,'#d2d6d5','Neutral', False,0,0,0,0],['Kurdistan', False, 30,'#d2d6d5','Neutral', False,0,0,0,0],['Qom', False, 30,'#00FF00','Iran', False,0,0,0,0]]
		ocean_row = [['Atlantic Ocean',True,0,'#3262a8','Neutral',False,0,0,0,0],['Atlantic Ocean',True,0,'#3262a8','Neutral',False,0,0,0,0],['Gibraltar',True,0,'#3262a8','Neutral',False,0,0,0,0],['Alboran Sea',True,0,'#3262a8','Neutral',False,0,0,0,0],['Naples',False,70,'#15ad31','Italy',False,1,0,0,0], ['Ionian Sea',True,0,'#3262a8','Italy',False,0,0,0,0], ['Ionian Sea',True,0,'#3262a8','Neutral',False,0,0,0,0],['Greece',False,70,'#d2d6d5','Neutral',False,0,1,0,0],['Aegean Sea',True,0,'#3262a8','Turkey',False,0,0,0,0],['Izmir', False, 50,'#FF0000','Turkey', False,1,0,0,0],['Antalya', False, 50,'#FF0000','Neutral', False,1,0,0,0],['Adana', False, 40,'#FF0000','Turkey', False,1,0,0,0],['Isfahan', False, 30,'#00FF00','Iran', False,0,0,0,1],['Shiraz', False, 30,'#00FF00','Iran', False,1,0,0,0]]
		fourth_row = [['Atlantic Ocean',True,0,'#3262a8','Spain',False,0,0,0,0],['Portugal',True,0,'#d2d6d5','Neutral',False,0,1,0,0],['Andalusia',False,50,'#e8cf10','Spain', False,0,0,1,0],['Baleric Sea',True,0,'#3262a8','Spain',False,0,0,0,0],['Rome',False,100,'#15ad31','Italy', True,0,1,0,0],['North Ionian Sea',True,0,'#3262a8','Italy',False,0,0,0,0], ['Bosnia', False, 50,'#d2d6d5','Neutral', False,0,0,1,0],['Serbia',False,100,'#d2d6d5','Neutral',True,1,0,0,0],['Mamara',True,0,'#3262a8','Turkey',False,0,0,0,0],['Bosphorus',True,0,'#3262a8','Turkey',False,0,0,0,0],['Ankara', False, 90,'#FF0000','Turkey', True,0,1,0,0],['Erzurum', False, 40,'#FF0000','Turkey', False,0,0,0,0],['Tabriz', False, 30,'#00FF00','Iran', False,1,0,0,0],['Tehran', False, 100,'#00FF00','Iran', True,0,0,0,1]]
		fifth_row = [['Atlantic Ocean',True,0,'#3262a8','Spain', False, 0,0,0,0],['Castille',False,50,'#e8cf10','Spain', False,0,0,1,0],['Madrid',False,100,'#e8cf10','Spain', True,0,1,0,0],['North Baleric Sea',True,0,'#3262a8','France', False,0,0,0,0],['Lombardy', False, 50,'#15ad31','Italy', False,0,1,0,0], ['Venice', False, 50,'#15ad31','Italy', False,1,0,0,0],['Slovenia', False, 50,'#d2d6d5','Neutral', False,0,0,0,0],['Transdanubia', False, 50,'#d2d6d5','Neutral', False,0,1,0,0],['Istanbul', False, 100,'#FF0000','Turkey', True,0,1,0,0],['Black Sea',True,0,'#3262a8','Turkey',False,0,0,0,0],['Black Sea',True,0,'#3262a8','Ukraine',False,0,0,0,0],['Black Sea',True,0,'#3262a8','Ukraine',False,0,0,0,0], ['Georgia', False, 70,'#d2d6d5','Neutral', False,0,0,1,0], ['Caspian Sea',True,0,'#3262a8','Iran',False,0,0,0,0]]
		sixth_row = [['Atlantic Ocean',True,0,'#3262a8','UK', False,0,0,0,0],['Bay of Biscay',True,0,'#3262a8','France', False,0,0,0,0],['Bordeaux',False,50,'#ad3315','France', False,0,1,0,0],['Lyon',False,50,'#ad3315','France', False,0,1,0,0],['Switzerland', False, 50,'#d2d6d5','Neutral', False,0,0,0,0], ['Austria', False, 50,'#d2d6d5','Neutral', False,0,0,0,0], ['Hungary', False, 50,'#d2d6d5','Neutral', False,0,1,0,0], ['Slovakia', False, 50,'#d2d6d5','Neutral', False,0,1,0,0],['Romania', False, 50,'#d2d6d5','Neutral', False,0,1,0,0], ['Black Sea',True,0,'#3262a8','Ukraine',False,0,0,0,0], ['Crimea', False, 70,'#03c2fc','Ukraine', False,0,0,0,0], ['Black Sea',True,0,'#3262a8','Ukraine',False,0,0,0,0], ['Caucauses', False, 70,'#d2d6d5','Neutral', False,0,0,0,1], ['Caspian Sea',True,0,'#3262a8','Iran',False,0,0,0,0]]
		seventh_row = [['Atlantic Ocean',True,0,'#3262a8','UK', False,0,0,0,0],['Brest',False,30,'#ad3315','France', False,0,1,0,0],['Paris',False,100,'#ad3315','France', True,1,0,0,0],['Alsace Lorraine',False,70,'#ad3315','France', False,1,0,0,0],['Baden', False, 70,'#808080','Germany', False,0,1,0,0], ['Bavaria', False, 50,'#808080','Germany', False,0,0,1,0], ['Wroclaw', False, 50,'#FFFFFF','Poland', False,0,0,1,0],['Krakow', False, 70,'#FFFFFF','Poland', False,0,0,2,0],['Odessa', False, 30,'#03c2fc','Ukraine', False,0,1,0,0], ['Dnieper', False, 50,'#03c2fc','Ukraine', False,0,1,0,0],['Donbas', False, 50,'#03c2fc','Ukraine', False,0,1,0,0],['Kuban', False, 50,'#702963','Russia', False,0,1,0,0],['Astrakhan', False, 50,'#702963','Russia', False,0,0,0,1],['Kahazakstan', False, 30,'#d2d6d5','Neutral', False,0,0,0,0]]
		eighth_row = [['Atlantic Ocean',True,0,'#3262a8','UK', False,0,0,0,0],['Atlantic Ocean',True,0,'#3262a8','UK', False,0,0,0,0],['English Channel',True,0,'#3262a8','UK', False,0,0,0,0],['Belgium',False,50,'#d2d6d5','Neutral', False,1,0,0,0],['Ruhr',False,100,'#808080','Germany', True,0,0,2,0], ['Berlin', False, 80,'#808080','Germany', True,0,0,1,0], ['Poznan', False, 50,'#FFFFFF','Poland', False,0,1,0,0], ['Warsaw', False, 100,'#FFFFFF','Poland', True,0,1,0,0],['Podoloia', False, 100,'#03c2fc','Ukraine', False,0,0,0,0],['Kiev', False, 100,'#03c2fc','Ukraine', True,0,1,0,0],['Kharkov', False, 70,'#03c2fc','Ukraine', False,0,0,1,0],['Voronezh', False, 30,'#702963','Russia', False,0,1,0,0],['Volga', False, 40,'#702963','Russia', False,0,1,0,0],['Kahazakstan', False, 30,'#d2d6d5','Neutral', False,0,0,0,0]]
		ninth_row = [['Cornwall',False,100,'#fc2403','UK', True,0,0,1,0],['London',False,100,'#fc2403','UK', True,0,0,0,0],['North Sea',True,0,'#3262a8','Neutral', False,0,0,0,0],['Netherlands',False,100,'#d2d6d5','Neutral', True,0,1,0,0],['Hamburg', False, 50,'#808080','Germany', False,0,1,0,0], ['Pomerania', False, 50,'#808080','Germany', False,0,1,0,0], ['Danzig', False, 50,'#FFFFFF','Poland', False,0,0,0,0], ['Gdansk', False, 50,'#FFFFFF','Poland', False,0,0,0,0],['Lithuania', False, 30,'#d2d6d5','Neutral', False,0,0,0,0],['Belarus', False, 30,'#d2d6d5','Neutral', False,0,0,0,0],['Moscow', False, 100,'#702963','Russia', False,0,0,0,0],['Gorky', False, 40,'#702963','Russia', False,0,0,0,0],['Kazan', False, 40,'#702963','Russia', False,0,0,0,0],['Samara', False, 40,'#702963','Russia', False,1,0,0,0]]
		tenth_row = [['Atlantic Ocean',True,0,'#3262a8','UK', True,0,0,0,0],['Wales',False,100,'#fc2403','UK', True,0,0,1,0],['Midlands',False,100,'#fc2403','UK', True,0,0,1,0],['North Sea',True,0,'#3262a8','UK', False,0,0,0,0],['North Sea',True,50,'#3262a8','Neutral', False,0,0,0,0],['Denmark', False, 50,'#d2d6d5','Neutral', False,0,0,0,1],['Baltic Sea',True,0,'#3262a8','Germany', False,0,0,0,0], ['Baltic Sea',True,0,'#3262a8','Poland', False,0,0,0,0],['Baltic Sea',True,0,'#3262a8','Germany', False,0,0,0,0],['Estonia',False,20,'#d2d6d5','Neutral', False,0,0,0,0],['Novgorod', False, 30,'#702963','Russia', False,0,0,0,0],['Yaroslavl', False, 40,'#702963','Russia', False,0,0,0,0],['Koml', False, 30,'#702963','Russia', False,0,0,0,0],['Yamalia', False, 30,'#702963','Russia', False,1,0,0,0],['Urals', False, 10,'#702963','Russia', False,0,0,0,0],['Perm', False, 40,'#702963','Russia', False,0,1,0,0]]
		eleventh_row = [['Atlantic Ocean',True,0,'#3262a8','UK', True,0,0,0,0],['Edinburgh',False,100,'#fc2403','UK', True,0,0,0,1],['North Sea',True,50,'#3262a8','Neutral', False,0,0,0,0],['North Sea',True,50,'#3262a8','Neutral', False,0,0,0,0],['North Sea',True,0,'#3262a8','Germany', False,0,0,0,0], ['Oresund',True,0,'#3262a8','Sweden', False,0,0,0,0],['Malmo',False,0,'#FFFF00','Sweden', False,0,1,0,0],['Baltic Sea',True,0,'#3262a8','Sweden', False,0,0,0,0],['Baltic Sea',True,0,'#3262a8','Neutral', False,0,0,0,0],['Baltic Sea',True,0,'#3262a8','Russia', False,0,0,0,0],['St. Petersburg',False,20,'#702963','Russia', True,0,0,0,0],['Archangel', False, 20,'#702963','Russia', False,0,0,0,0],['Yugyd', False, 10,'#702963','Russia', False,0,0,0,0],['Even', False, 5,'#702963','Russia', False,0,0,0,0]]
		twelth_row = [['Atlantic Ocean',True,0,'#3262a8','UK', True,0,0,0,0],['Scotland',False,100,'#fc2403','UK', True,0,0,0,1],['North Sea',True,50,'#3262a8','Neutral', False,0,0,0,0],['North Sea',True,0,'#3262a8','Neutral', False,0,0,0,0],['North Sea',True,0,'#3262a8','Germany', False,0,0,0,0], ['Skagerak',True,0,'#3262a8','Neutral', False,0,0,0,0],['Gothenburg',False,0,'#FFFF00','Sweden', False,0,0,0,0],['Stockholom',False,0,'#FFFF00','Sweden', True,0,1,0,0],['Baltic Sea',True,0,'#3262a8','Russia', False,0,0,0,0],['Helsinki', False, 30,'#d2d6d5','Neutral', False,0,0,0,0],['Karelia', False, 20,'#702963','Russia', False,0,0,0,0],['White Sea',True,0,'#3262a8','Russia', False,0,0,0,0],['White Sea',True,0,'#3262a8','Russia', False,0,0,0,0],['White Sea',True,0,'#3262a8','Russia', False,0,0,0,0]]
		thirteenth_row = [['Atlantic Ocean',True,0,'#3262a8','UK', True,0,0,0,0],['Atlantic Ocean',True,0,'#3262a8','UK', True,0,0,0,0],['North Sea',True,0,'#3262a8','UK', False,0,0,0,0],['North Sea',True,0,'#3262a8','Neutral', False,0,0,0,0],['North Sea',True,0,'#3262a8','Germany', False,0,0,0,0], ['Oslo',False,0,'#d2d6d5','Neutral', False,0,0,0,1], ['Svealand',False,0,'#FFFF00','Sweden', False,1,0,0,0],['Lappland',False,0,'#FFFF00','Sweden', False,1,0,0,0],['Finland', False, 30,'#FFFF00','Sweden', False,0,0,0,0],['Finland', False, 30,'#d2d6d5','Neutral', False,1,0,0,0],['Murmansk', False, 40,'#702963','Russia', False,0,0,0,0],['White Sea',True,0,'#3262a8','Russia', False,0,0,0,0],['Arctic Sea',True,0,'#3262a8','Russia', False,0,0,0,0],['Arctic Sea',True,0,'#3262a8','Russia', False,0,0,0,0]]
		#fourteenth_row = [['Atlantic Ocean',True,0,'#3262a8','UK', True,0,0,0,0],['Atlantic Ocean',True,0,'#3262a8','UK', True,0,0,0,0],['North Sea',True,0,'#3262a8','UK', False,0,0,0,0],['North Sea',True,0,'#3262a8','Neutral', False,0,0,0,0],['North Sea',True,0,'#3262a8','Germany', False,0,0,0,0],['North Sea',True,0,'#3262a8','Germany', False,0,0,0,0],['Lappland',False,0,'#FFFF00','Sweden', False,1,0,0,0],['Lulea',False,0,'#FFFF00','Sweden', False,0,0,0,0],['Finland', False, 30,'#FFFF00','Sweden', False,1,0,0,0],['Murmansk', False, 40,'#702963','Russia', False,0,0,0,0],['Kola', False, 20,'#702963','Russia', False,0,0,0,0],['White Sea',True,0,'#3262a8','Russia', False,0,0,0,0],['Arctic Sea',True,0,'#3262a8','Russia', False,0,0,0,0],['Arctic Sea',True,0,'#3262a8','Russia', False,0,0,0,0]]
		self.hexList.append(first_row)
		self.hexList.append(second_row)
		self.hexList.append(third_row)
		self.hexList.append(ocean_row)
		self.hexList.append(fourth_row)
		self.hexList.append(fifth_row)
		self.hexList.append(sixth_row)
		self.hexList.append(seventh_row)
		self.hexList.append(eighth_row)
		self.hexList.append(ninth_row)
		self.hexList.append(tenth_row)
		self.hexList.append(eleventh_row)
		self.hexList.append(twelth_row)
		self.hexList.append(thirteenth_row)
		#self.hexList.append(fourteenth_row)

	def apply(self, g, p):
		y = 0
		total = len(self.hexList)
		for i in self.hexList:
			x = 0
			for j in i:
				start = Country.objects.filter(name=j[4])[0]
				temp = Hexes(hexNum=total*y+x ,game=g, controller=p, color=j[3], name=j[0], water=j[1], xLocation=x, yLocation=y, population=j[2], start_country=start, center=j[5], iron=j[6], wheat=j[7], coal=j[8], oil=j[9])
				temp.save()
				x += 1
			y += 1