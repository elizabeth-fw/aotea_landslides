
# Peps has half data for some years (ex. 2023) and shows errors for others (ex. 2021)
# ONDA does not have S2 data for aotea
# sentinelsat is not recognized anymore as the previous copernicus website was shut down in Oct 2023

# FOR S2_MSI_L1C
# 2015 search results - 12 on creodias
# 2016 search results - 18 on creodias
# 2017 search results - 44 on creodias
# 2018 search results - 46 on creodias
# 2019 search results - 92 on creodias
# 2020 search results - 92 on creodias
# 2021 search results - 96 on creodias
# 2022 search results - 50 on creodias
# 2023 search results - 44 on creodias

# FOR S2_MSI_L2A
# 2017 search results - 0 on creodias
# 2018 search results - 20 on creodias
# 2019 search results - 105 on creodias
# 2020 search results - 110 on creodias
# 2021 search results - 110 on creodias
# 2022 search results - 48 on creodias
# 2023 search results - 44 on creodias


################ SEARCH #######################
from eodag import EODataAccessGateway
dag = EODataAccessGateway()
dag.set_preferred_provider("creodias")

# Carry out the search and download
search_criteria = {
    "productType": "S2_MSI_L1C",
    "start": "2015-11-01",
    "end": "2015-12-31",
    "geom": {"lonmin": 175.2, "latmin": -36, "lonmax": 175.6, "latmax": -36.4}
}

products = dag.search_all(**search_criteria)



############### DOWNLOAD #######################
import os
from eodag import EODataAccessGateway
from eodag import setup_logging
setup_logging(3)

#Setup user credentials and directory
dag = EODataAccessGateway()
dag.set_preferred_provider("creodias")
dag.providers_config["creodias"].auth.credentials["totp"] = "141565"  #update token and run immediately

save_dir = "C:/Users/ewil195/Documents/S2"
if not os.path.isdir(save_dir):
    os.mkdir(save_dir)

# Carry out the search and download
search_criteria = {
    "productType": "S2_MSI_L1C",
    "start": "2016-11-01",
    "end": "2016-12-31",
    "geom": {"lonmin": 175.2, "latmin": -36, "lonmax": 175.6, "latmax": -36.4}
}

products = dag.search_all(**search_criteria)

if not products:
    print("No products found matching the search criteria.")
else:
    for product in products:
        print('Trying to download:', product.properties['title'])
        try:
            dag.download(product, progress_callback=None, wait=2, timeout=20, destination_uri=save_dir)
            print(f"Downloaded {product.properties['title']} to {save_dir}")
        except Exception as e:
            print(f"Error downloading {product.properties['title']}: {str(e)}")