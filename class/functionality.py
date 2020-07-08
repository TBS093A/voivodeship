from backend.player import *
from backend.country import *
from backend.army import *
from backend.settlement import *

class Functionality():

    def __init__(self):
        self.clans = []
        self.players = []
        self.countries = []
        self.provinces = []
        self.cities = []
        self.villages = []

    def create_clan(self, name):
        new_clan = Clan(name)
        self.clans.append( new_clan )

    def create_player(self, clan, player_name):
        new_player = Player(player_name, clan)
        clan.players.append( new_player )
        self.players.append( new_player )

    def create_country(self, player, country_name):
        new_country = Country(country_name, player)
        player.countries.append( new_country )
        self.countries.append( new_country )

    def create_province(self, country, province_name):
        new_province = Province(province_name, country)
        country.provinces.append( new_province )
        self.provinces.append( new_province )

    def create_city(self, province, city_name):
        new_city = City(city_name, province)
        province.cities.append( new_city )
        self.cities.append( new_city )

    def create_village(self, city, village_name):
        new_village = Village(village_name, city)
        city.villages.append( new_village )
        self.villages.append( new_village )
