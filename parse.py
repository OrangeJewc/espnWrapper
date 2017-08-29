from espnff import League

id = 240470
year = 2017

   # league.power_rankings(week=#)
   # league.scoreboard() (grabs current week. Returns Matchup[])
      # Matchup example - Matchup(Team(Team 2), Team(Team 7))
         # matchup = scoreboard[1]
         # matchup.home_team
         # matchup.home_score
         # matchup.away_team
         # matchup.away_score         
   # league.scoreboard(week=#)
league = League(id, year)

'''
   Contains array of teams (Team)
      Team.team_id
      Team.team_name
      Team.team_abbrev
      Team.owner
      Team.division_id
      Team.division_name
      Team.wins
      Team.losses
      Team.points_for
      Team.points_against
      Team.schedule (Array of teams in order of play)
      Team.scores (Array of weekly scores)
      Team.mov (?)
'''
teams = league.teams

'''
   settings.reg_season_count
   settings.final_season_count
   settings.undroppable_list
   settings.veto_votes_required
   settings.team_count
   settings.playoff_team_count
   settings.team_count
   settings.id
   settings.keeper_count
   settings.tie_rule ('Most Bench Points')
   settings.playoff_seed_tie_rule ('Head to Head Record')
   settings.roster ({'RB/WR/TE': 1, 'BE': 7, 'QB': 1, 'D/ST': 1, 'RB': 2, 'TE': 1, 'K': 1, 'WR': 2})
   settings.trade_deadline
   settings.name
   settings.status
   settings.year
   settings.server_date
'''
settings = league.settings

def main():
   for property, value in vars(teams[0]).iteritems():
    print property, ": ", value

if __name__ == "__main__":
   main()
