from basket_ball import (
    num_points_per_game, player_age,
    team_colors, team_names,
    player_numbers, player_stats,
    average_rebounds_by_shoe_brand
)

import io
import sys

class TestBasketBall:
    '''Module basket_ball.py'''

    def test_num_points_per_game(self):
        '''knows the number of points scored by each player'''
        assert(num_points_per_game("Jarrett Allen") == 16.1)
        assert(num_points_per_game("Darius Garland") == 21.7)
        assert(num_points_per_game("Evan Mobley") == 15.0)
        assert(num_points_per_game("Kevin Love") == 13.6)
        assert(num_points_per_game("Isaac Okoro") == 8.8)
        assert(num_points_per_game("Ricky Rubio") == 13.1)
        assert(num_points_per_game("Bradley Beal") == 23.2)
        assert(num_points_per_game("Kyle Kuzma") == 17.1)
        assert(num_points_per_game("Kentavious Caldwell-Pope") == 13.2)
        assert(num_points_per_game("Davis Bertans") == 5.6)
        assert(num_points_per_game("Kristaps Porzingis") == 22.1)
        assert(num_points_per_game("Rui Hachimura") == 11.3)

    def test_player_age(self):
        '''knows the age of each player'''
        assert(player_age("Jarrett Allen") == 24)
        assert(player_age("Darius Garland") == 22)
        assert(player_age("Evan Mobley") == 21)
        assert(player_age("Kevin Love") == 34)
        assert(player_age("Isaac Okoro") == 21)
        assert(player_age("Ricky Rubio") == 31)
        assert(player_age("Bradley Beal") == 29)
        assert(player_age("Kyle Kuzma") == 27)
        assert(player_age("Kentavious Caldwell-Pope") == 29)
        assert(player_age("Davis Bertans") == 29)
        assert(player_age("Kristaps Porzingis") == 27)
        assert(player_age("Rui Hachimura") == 24)

    def test_team_colors(self):
      '''knows the team colors of each team'''
      assert(team_colors("Cleveland Cavaliers") == ["Wine", "Gold"])
      assert(team_colors("Washington Wizards") == ["Red", "White", "Navy Blue"])

    def test_team_names(self):
      '''returns the team names'''
      assert(team_names() == ["Cleveland Cavaliers", "Washington Wizards"])

    def test_player_numbers(self):
      '''returns the player numbers for a given team'''
      assert(player_numbers("Cleveland Cavaliers") == [31, 10, 4, 0, 35, 99])
      assert(player_numbers("Washington Wizards") == [3, 33, 1, 42, 6, 8])

    def test_player_stats(self):
      '''returns all stats for a given player'''

      jarrett_allen = { "name": "Jarrett Allen", "number": 31, "position": "Center", "points_per_game": 16.1, "rebounds_per_game": 10.8, "assists_per_game": 1.6, "steals_per_game": 0.8, "blocks_per_game": 1.3, "career_points": 3945, "age": 24, "height_inches": 82, "shoe_brand": "Nike", }
      darius_garland = { "name": "Darius Garland", "number": 10, "position": "Point Guard", "points_per_game": 21.7, "rebounds_per_game": 3.3, "assists_per_game": 8.6, "steals_per_game": 1.3, "blocks_per_game": 0.1, "career_points": 3142, "age": 22, "height_inches": 73, "shoe_brand": "Nike", }
      evan_mobley = { "name": "Evan Mobley", "number": 4, "position": "Center", "points_per_game": 15.0, "rebounds_per_game": 8.3, "assists_per_game": 2.5, "steals_per_game": 0.8, "blocks_per_game": 1.7, "career_points": 1034, "age": 21, "height_inches": 83, "shoe_brand": "Adidas", }
      kevin_love = { "name": "Kevin Love", "number": 0, "position": "Power Forward", "points_per_game": 13.6, "rebounds_per_game": 7.2, "assists_per_game": 2.2, "steals_per_game": 0.4, "blocks_per_game": 0.2, "career_points": 14305, "age": 34, "height_inches": 80, "shoe_brand": "Nike", }
      isaac_okoro = { "name": "Isaac Okoro", "number": 35, "position": "Small Forward", "points_per_game": 8.8, "rebounds_per_game": 3.0, "assists_per_game": 1.8, "steals_per_game": 0.8, "blocks_per_game": 0.3, "career_points": 1234, "age": 21, "height_inches": 77, "shoe_brand": "Nike", }
      ricky_rubio = { "name": "Ricky Rubio", "number": 99, "position": "Point Guard", "points_per_game": 13.1, "rebounds_per_game": 4.1, "assists_per_game": 6.6, "steals_per_game": 1.4, "blocks_per_game": 0.2, "career_points": 7399, "age": 31, "height_inches": 74, "shoe_brand": "Adidas", }
      bradley_beal = { "name": "Bradley Beal", "number": 3, "position": "Shooting Guard", "points_per_game": 23.2, "rebounds_per_game": 4.7, "assists_per_game": 6.6, "steals_per_game": 0.9, "blocks_per_game": 0.4, "career_points": 14231, "age": 29, "height_inches": 76, "shoe_brand": "Nike", }
      kyle_kuzma = { "name": "Kyle Kuzma", "number": 33, "position": "Power Forward", "points_per_game": 17.1, "rebounds_per_game": 8.5, "assists_per_game": 3.5, "steals_per_game": 0.6, "blocks_per_game": 0.9, "career_points": 5336, "age": 27, "height_inches": 81, "shoe_brand": "Puma", }
      kentavious_caldwell_pope = { "name": "Kentavious Caldwell-Pope", "number": 1, "position": "Shooting Guard", "points_per_game": 13.2, "rebounds_per_game": 3.4, "assists_per_game": 1.9, "steals_per_game": 1.1, "blocks_per_game": 0.3, "career_points": 7911, "age": 29, "height_inches": 77, "shoe_brand": "Nike", }
      davis_bertans = { "name": "Davis Bertans", "number": 42, "position": "Power Forward", "points_per_game": 5.6, "rebounds_per_game": 2.1, "assists_per_game": 0.6, "steals_per_game": 0.3, "blocks_per_game": 0.3, "career_points": 3165, "age": 29, "height_inches": 82, "shoe_brand": "Nike", }
      kristaps_porzingis = { "name": "Kristaps Porzingis", "number": 6, "position": "Power Forward", "points_per_game": 22.1, "rebounds_per_game": 8.8, "assists_per_game": 2.9, "steals_per_game": 0.7, "blocks_per_game": 1.5, "career_points": 6371, "age": 27, "height_inches": 87, "shoe_brand": "Adidas", }
      rui_hachimura = { "name": "Rui Hachimura", "number": 8, "position": "Power Forward", "points_per_game": 11.3, "rebounds_per_game": 3.8, "assists_per_game": 1.1, "steals_per_game": 0.5, "blocks_per_game": 0.2, "career_points": 1913, "age": 24, "height_inches": 80, "shoe_brand": "Jordan", }

      assert(player_stats("Jarrett Allen") == jarrett_allen)
      assert(player_stats("Darius Garland") == darius_garland)
      assert(player_stats("Evan Mobley") == evan_mobley)
      assert(player_stats("Kevin Love") == kevin_love)
      assert(player_stats("Isaac Okoro") == isaac_okoro)
      assert(player_stats("Ricky Rubio") == ricky_rubio)
      assert(player_stats("Bradley Beal") == bradley_beal)
      assert(player_stats("Kyle Kuzma") == kyle_kuzma)
      assert(player_stats("Kentavious Caldwell-Pope") == kentavious_caldwell_pope)
      assert(player_stats("Davis Bertans") == davis_bertans)
      assert(player_stats("Kristaps Porzingis") == kristaps_porzingis)
      assert(player_stats("Rui Hachimura") == rui_hachimura)

    def test_average_rebounds_by_shoe_brand(self):
      '''returns the average rebounds for players by the brand of shoe they wear'''
      captured_out = io.StringIO()
      sys.stdout = captured_out
      average_rebounds_by_shoe_brand()
      sys.stdout = sys.__stdout__
      assert(captured_out.getvalue() == "Nike:  4.93\nAdidas:  7.07\nPuma:  8.50\nJordan:  3.80\n")
