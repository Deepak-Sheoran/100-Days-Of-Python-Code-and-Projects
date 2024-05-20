# Instructions
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List
# that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.
#
# Write a function that will work with the following line of code to add the entry for Brazil to the
# travel_log.
#
# add_new_country("Brazil", 5, ["São Paulo", "Rio de Janeiro"])

country = "Brazil"  # Add country name
visits = 5  # Number of visits
List = ["São Paulo", "Rio de Janeiro"]  # list of cities in the country

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Writing the function that will allow new countries to be added to the travel_log.
def add_new_country(country_name, number_of_visits, list_of_cities):
    new_entry = {"country": country_name, "visits": number_of_visits, "cities": list_of_cities}
    travel_log.append(new_entry)


add_new_country(country, visits, List)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
