# # DELETE THE FOLLOWING: # #
# Here is an overview of how requesting data works.
# This is the code to request data from the microservice. It works by
# creating a request URL. Then you define the team and the year you want
# data for. You then create a dictionary with the year and team to include
# in the request. You send the request using "requests.post".
# The microservice receives that request and returns the team data, which
# this code then parses through and prints.

# Import the requests module and the JSON module
import requests
import json

# First, define the URL for getting team data for a matchup
team_data_request_url = "http://localhost:5000/get_team_data"

# Next, define the team and the year you want data for
team = "Connecticut"
year = "2024"

# Define the json data to send with the requests to the get_team_data file
year_and_team_to_send = {"year": year, "team": team}

# Define the json data to send with the requests to the get_team_data file

# Fetch the team data from the get_team_data microservice using the requests
team_data = requests.post(team_data_request_url, json=year_and_team_to_send)

# Parse through the data to actually get the team data from the response
parsed_team_data = json.loads(team_data.text)

# Print the team data to send to prove the request worked as planned
print(parsed_team_data["team"])
