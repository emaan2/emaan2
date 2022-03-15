# recommendation engine for tourists
 
 # setting up
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# travelling to faraway lands
def get_destination_index(destination) -> str:
    destination_index = destinations.index(destination)
    return destination_index

get_destination_index("Los Angeles, USA")