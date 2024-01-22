from eodag import setup_logging
setup_logging(3)

from eodag import EODataAccessGateway
dag = EODataAccessGateway()
dag.available_providers("S2_MSI_L1C")

[product_type["ID"] for product_type in dag.list_product_types("onda")]


search_criteria = {
    "productType": "S2_MSI_L1C",
    "start": "2023-11-01",
    "end": "2023-12-31",
    "geom": {"lonmin": 175.2, "latmin": -36, "lonmax": 175.6, "latmax": -36.4}
}
products_first_page, estimated_total_number = dag.search(**search_criteria)
print(f"Got {len(products_first_page)} products and an estimated total number of {estimated_total_number} products.")


# Use  eodag code with peps to download S2 data
# ONDA does not have S2 data for aotea
# try using sentinelsat


dag = EODataAccessGateway()
#dag.set_preferred_provider("peps")

# Carry out the search and download
search_criteria = {
    "productType": "S2_MSI_L1C",
    "start": "2021-11-01",
    "end": "2021-12-31",
    "geom": {"lonmin": 175.2, "latmin": -36, "lonmax": 175.6, "latmax": -36.4}
}

products = dag.search_all(**search_criteria)