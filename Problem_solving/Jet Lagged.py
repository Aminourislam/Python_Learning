'''
Jet Lagged

Daily Coding Challenge
June 8, 2026

Given a departure city, an arrival city, a flight duration in hours, and a direction of travel, return the number of jet lag hours the traveller is experiencing.

The given cities will be from the following list that includes their UTC offset:
City 	Offset
"Los Angeles" 	-8
"New York" 	-5
"London" 	0
"Istanbul" 	+3
"Dubai" 	+4
"Hong Kong" 	+8
"Tokyo" 	+9

To calculate jet lag hours:

    Find the timezone difference in hours between the two cities.
    Determine the direction multiplier. If travelling "east", it's 1.5, otherwise, it's 1.0.
    Get the jet lag hours with the formula: timezone difference + (flight duration * 0.1) * direction multiplier

Return the jet lag hours rounded to one decimal place.
Tests:

Waiting: 1. get_jet_lag_hours("Istanbul", "Hong Kong", 10, "east") should return 6.5.
Waiting: 2. get_jet_lag_hours("London", "New York", 8, "west") should return 5.8.
Waiting: 3. get_jet_lag_hours("Hong Kong", "Tokyo", 4, "east") should return 1.6.
Waiting: 4. get_jet_lag_hours("Dubai", "London", 7, "west") should return 4.7.
Waiting: 5. get_jet_lag_hours("Los Angeles", "Hong Kong", 15, "west") should return 17.5.
Waiting: 6. get_jet_lag_hours("Tokyo", "Dubai", 9, "west") should return 5.9.
Waiting: 7. get_jet_lag_hours("New York", "Istanbul", 10, "east") should return 9.5.
'''