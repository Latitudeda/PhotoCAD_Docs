Exporting GDS/Json file
==========================

#. Export GDS file:

   ::

       fp.export_gds(
            content, # cell library and cell reference can be used as a content.
            file, # gds file path, both absolute and relative paths are applicable.
            layer_mapper, # users are allowed to hide some layers when exporting GDS file.
            auto_flatten=True, # default setting of auro_flatten is True.
            )

#. Export Json file from existing cell:

   This will export both gds file and json file at the same time.

   ::

       fp.export_json(
            content, # cell library and cell reference can be used as a content.
            json_file, # path to store json file, both absolute and relative paths are applicable.
            library_file, # path to store gds file, both absolute and relative paths are applicable.
            layer_mapper, # users are allowed to hide some layers when exporting GDS file.
            auto_flatten=True, # default setting of auto_flatten is True.
            explicit_parameters=False, # default setting of explicit_parameters is False and is used to show the values of the waveguide types.
            )