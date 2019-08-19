import googlemaps, csv
from secret import API_KEY, LOC1, LOC2

gmaps = googlemaps.Client(key= API_KEY)

with open(r"C:\\Users\speedykai\Documents\Programming\csv_to_googlemaps\addresses.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader: # row is the addresses individually from the csv csv_file
        my_dist = gmaps.distance_matrix(row,LOC1, units ='imperial', avoid = 'tolls')['rows'][1]['elements'][0]
        print(my_dist, row)
        print(" \n")
