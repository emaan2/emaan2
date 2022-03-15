# recommendation engine for tourists
 
 # setting up
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# travelling to faraway lands
def get_destination_index(destination) -> str:
    destination_index = destinations.index(destination)
    return destination_index


def get_traveler_location(traveler) -> str:
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)