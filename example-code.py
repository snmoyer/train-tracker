from google.transit import gtfs_realtime_pb2
import requests

trips = []
stops = []

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace')
feed.ParseFromString(response.content)
for entity in feed.entity:
  if entity.HasField('trip_update'):
    trips.append(entity.trip_update)
  if entity.HasField('vehicle'):
    stops.append(entity.vehicle)

print(trips[0])
print(stops[0])