from math import radians, cos, sin, asin, sqrt


class ShoppersCoverage:
    def __init__(self, shopper, coverage):
        self.shopper_id = shopper
        self.coverage = coverage

    def __repr__(self):
        return "shopper ID = " + str(self.shopper_id) + ", Coverage = " + str(self.coverage)+";"


locations = [
    {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84},
    {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99},
    {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00},
    {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02},
]

shoppers = [
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': "true"},
    {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': "true"},
    {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': "true"},
    {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': "true"},
    {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': "true"},
    {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': "true"},
    {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': "true"}
]

distances = []


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    return R * c


for index, i in enumerate(shoppers):
    distances.append([])
    for elem in locations:
        distances[index].append(
            haversine(i["lat"], i["lng"], elem["lat"], elem["lng"]))

percentageCover = []
# Get percentage cover for each shopper.
for elem in distances:
    counter = 0
    for i in elem:
        if i <= 10:
            counter += 1
    percentageCover.append(counter/len(elem)*100)

result = []
testPerson = ShoppersCoverage("S1", 15)
for index, i in enumerate(percentageCover):
    n = ShoppersCoverage(shoppers[index]["id"], i)
    result.append(ShoppersCoverage(shoppers[index]["id"], i))


result.sort(key=lambda x: x.coverage, reverse=True)
print(result)
