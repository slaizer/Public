import requests
import json

# Set up the request parameters
url = "http://api.aviationstack.com/v1/flights"

Airportcode= input("please,put the airport code:")
Airlinecode= input("please,put the Airline code:")
ArrivalAirport=input("Arrival Airport:")
params = {
    "access_key": "xxxx",
    "flight_status": "",
    #"flight_date": "2023-4-28", #used for Preimum Sub
    "limit": 100,
    "arr_iata":(ArrivalAirport),
    "airline_iata" :(Airlinecode),
    "dep_iata":(Airportcode),   # Replace with the IATA code of the airport you want to filter by
}

response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = json.loads(response.text)

    # Save the flight data to a text file
    with open("flight_data.txt", "w") as f:
        for flight in data["data"]:
            f.write(f"Flight {flight['flight']['iata']}:\n")
            f.write(f"  Airline: {flight['airline']['name']}\n")
            f.write(f"  Flight Status: {flight['flight_status']}\n")

            # Write departure information
            departure = flight['departure']
            f.write("  Departure:\n")
            f.write(f"    Airport: {departure['airport']}\n")
            f.write(f"    Scheduled Time: {departure['scheduled']}\n")
            f.write(f"    Estimated Time: {departure['estimated']}\n")

            # Write arrival information
            arrival = flight['arrival']
            f.write("  Arrival:\n")
            f.write(f"    Airport: {arrival['airport']}\n")
            f.write(f"    Scheduled Time: {arrival['scheduled']}\n")
            f.write(f"    Estimated Time: {arrival['estimated']}\n")
            f.write("\n")

    print("Flight data saved to flight_data.txt")
else:
    # Print the error message
    print(f"Error: {response.status_code} - {response.json()['error']['message']}")