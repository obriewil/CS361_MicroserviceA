# CS361_MicroserviceA
Microservice A Repository to share with my teammates. 

# PART A: how to programmatically REQUEST data from the microservice you implemented
My microservice works off of HTTP requests and flask servers. The user must have pip installed FLASK to use 
The microservice. My Microservice A is a simualte_game function for a march madness simlation tool. This 
microservice simulates the results of a single baseketball game based on stat values and weight values for the 
statistics. To request data from the microservice, you have to use a "POST" request. This involves importing the request module, defining the post request URL, creating a dictionary with the data to send to the microservice, and requesting the data. The following is an example of how this works in python code (Note, the 
microservice must be started in a separate terminal before requesting data form the microservice). 

  import requests
  import json
  
  simulate_game_url = "http://localhost:5004/simulate_game"

  weights = {'Seed': 25, 'KenPom': 25, 'TS_Perc': 25,
             'ORtg': 25}

  team1_data_to_send = {'name': "Uconn", 'Seed': 1, 'KenPom': 25, 'TS_Perc': 0.55,
                        'ORtg': 100}
  
  team2_data_to_send = {'name': "Pitt", 'Seed': 16, 'KenPom': 2, 'TS_Perc': 0.52,
                        'ORtg': 20}
  
  matchup_data_to_send = {"weights": weights,
                          "team1": team1_data_to_send,
                          "team2": team2_data_to_send}

  simulated_game = requests.post(simulate_game_url, json=matchup_data_to_send)

# PART B: how to programmatically RECEIVE data from the microservice you implemented
When the user requests data from the microservice, the user must define a variable for the post request. 
This variable will store the response data, which is sent back as JSON data. The microservice will return
The winner of the simulated game as a json file that looks like this (for example): {"winner": "Connecticut"}.
To actually receive the data, the user just has to load the response in using the json.loads module. 
In code it looks like this:

  game_winner = json.loads(simulated_game.text)
  
  print(game_winner)

# PART C: UML sequence diagram
![UML Diagram](https://github.com/obriewil/CS361-Course-Project/assets/137870954/8cc40a70-91b3-41b4-86a5-ab036a5062b5)
