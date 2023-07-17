from stac_cat_utils.stac_generator import StacCatalogGenerator

if __name__ == '__main__':
    stac_gen = StacCatalogGenerator()

    src_path = './../test_files'
    catalog = stac_gen.create(src_path,
                                     collection_paths=[f'{src_path}/logs'],
                                     item_paths=[f'{src_path}/logs/extra_logs'],
                                     ignore_paths=[f'{src_path}/cube'])

    # Catalog collection can be set to be datacube compliant if possible, please be aware that this is a custom
    # method provided by STACCatalog which inherits from pystac.Catalog
    catalog.make_datacube_compliant()

    # For simple usage, one can just use the provided save method of the generator class
    stac_gen.save(dest_path='stac_catalog')
