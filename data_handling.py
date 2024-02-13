import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling

def reproject_raster(src, output_file, dst_crs):
    with rasterio.open(output_file, "w", **src.meta) as dst:
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

    dst.write(src.read(), indexes=1)
    print("Reprojected raster saved to:", output_file)