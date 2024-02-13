import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling

def reproject_raster(input_file, output_file, dst_crs):
    with rasterio.open(input_file) as src:
        transform, width, height = calculate_default_transform(src.crs,
                                                               dst_crs,
                                                               src.width,
                                                               src.height,
                                                               *src.bounds)
        kwargs = src.meta.copy()
        kwargs.update({
            "crs": dst_crs,
            "transform": transform,
            "width": width,
            "height": height})
    with rasterio.open(output_file, 'w', **kwargs) as dst:
        reproject(
            source=rasterio.band(src, 1),
            destination=rasterio.band(dst, 1),
            src_transform=src.transform,
            src_crs=src.crs,
            dst_transform=transform,
            dst_crs=dst_crs,
            resampling=Resampling.nearest)
    print("Reprojected raster saved to:", output_file)