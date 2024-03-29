

"""
from eodag import EODataAccessGateway
from eodag.plugins.search.qssearch import QueryStringSearch

# Set the STAC catalog URL
catalog_url = "https://nz-imagery.s3-ap-southeast-2.amazonaws.com/catalog.json"

# Create an EODataAccessGateway instance
dag = EODataAccessGateway()

# Define the area of interest (bounding box coordinates in [min_lon, min_lat, max_lon, max_lat] format)
min_lon, min_lat, max_lon, max_lat = 175.2, -36, 175.6, -36.4

# Set the search parameters
LINZ_search_parameters = {
    "geom": {"lonmin": 175.2, "latmin": -36, "lonmax": 175.6, "latmax": -36.4}
}

# Search for available products using the STAC catalog
search_results = dag.search(QueryStringSearch(**LINZ_search_parameters), catalog_url)

# Display information about the search results
if search_results:
    print("Found matching products:")
    for product in search_results:
        print(f"- Product ID: {product.properties['id']}")
        print(f"  Date: {product.properties['datetime']}")
        print(f"  Cloud Cover: {product.properties['eo:cloud_cover']}%")
        print(f"  Platform: {product.properties['platform']}")
        print(f"  Instrument: {product.properties['instrument']}")
        print(f"  Thumbnail URL: {product.properties['thumbnail']}")
        print("")

else:
    print("No products found matching the search criteria.")

"""





from pystac_client import Client

LINZclient = Client.open("https://nz-imagery.s3-ap-southeast-2.amazonaws.com/catalog.json")

search = LINZclient.search(
    bbox=[175.2,-36,175.6,-36.4]
)
print(f"{search.matched()} items found")


for item in search.items():
    print(item.id)



