# # DELETE THE FOLLOWING: # #
# Here is an overview of how the microservice works.
# This is a microservice to take an input team name and year and search through
# a JSON data file until the team names match. When you find the correct team
# name you simply return the team stats for that team and year. You must
# jsonify the data

# Import JSON and flask modules
import json
from flask import Flask, request, jsonify


# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)


# Use the app route decorator tell the app which URL should call the
# associated function
@app.route("/get_team_data", methods=["POST"])
def get_team_data():
    """
    This is the function to get team data from the json data. Works as a
    server that takes in a team name and year. Returns the stats for that
    team for that given year in the form of a post.
    """

    # Get the team name and year from the request that was sent
    received_year = request.json.get("year")
    team_name = request.json.get("team")

    # Generate the JSON filename for the stats for a given year.
    json_filename = "Stats_" + received_year + ".json"

    # Try opening the json file and cycling through the data until you find
    # the correct team.
    try:

        # Load the JSON Data and cycle through until you find the right team
        # Return the information for that team as JSON data.
        with open(json_filename, 'r') as file:

            # Load the json data in as the variable "data""
            data = json.load(file)

            # Loop through all teams in the data and check for the match
            for team in data['teams']:

                # If the team name matches, return the JSON data for that team
                if team['name'] == team_name:
                    return jsonify({'team': team})

            # If the team is not found in the data, print and return the
            # message that the data was not found.
            print("Team not found.")
            return "Team not found.", 200

    # Check for the exception where the file cannot be found. If that is the
    # case return a file not found error and print the message.
    except FileNotFoundError:
        print("File not found.")
        return "File not found.", 200


# Main function to run the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)
