Importing/Exporting GDS/Json file
===================================


#. Import GDS file:

   This often happens when we want to import PDK cell from a GDS file. You need to prepare the GDS file and write the corresponding json file indicating the layers and the port information of the cell.

   We recommend to follow the folder structure as follows:

   .. image:: ../images/importGDSsturcture.png

   * json file:

     * cell name: The cell name indicated in the GDS file.

     * layers: First point out all the layers in the GDS file, and assign them to the layers in your PDK. User are allowed to link the layers to PDK layers e.g., ``TECH.LAYER.FWG_COR``, ignore the layer in the GDS file e.g., "_IGNORE_", or directly use the layer ID in the PDK e.g., "80/30".

     * ports:

       * names: The name of the port

       * position: The coordinate of the ports in the GDS file. It should be the center of the port.

       * orientation: The orientation of the port is pointing out.

       * waveguide type: The port has to match one of the waveguide type in your PDK. However, the parameters e.g, core_width can be modified.



         ::

            {
                "cell_name": "edge_coupler_1550",
                "layers": {
                    "*": "_ERROR_",
                    "1/0": "TECH.LAYER.FWG_COR",
                    "1/10": "TECH.LAYER.FWG_CLD",
                    "7/0": "TECH.LAYER.TIN_DRW",
                    "60/0": "TECH.LAYER.CONT_DRW",
                    "63/0": "TECH.LAYER.M1_DRW",
                    "66/0": "_IGNORE_",
                    "68/0": "80/30"
                },
                "ports": [
                    {
                        "name": "op_0",
                        "position": [
                            200,
                            0
                        ],
                        "orientation": {
                            "degrees": 0
                        },
                        "waveguide_type": {
                            "override": "TECH.WG.FWG.C.WIRE",
                            "values": {
                                "core_width": 0.5,
                                "cladding_width": 4.45
                            }
                        }
                    }
                ]
            }

       * For metal pins, instead of a line, a rectangle could be the case which a pin is. In this situation, use ``shape`` to form a rectangular or a polygon.

         ::

                  {
                    "name": "ELEC_1_PAD",
                    "position": [
                      211.5,
                      100
                    ],
                    "shape": [
                      [173, 140.5],
                      [250, 140.5],
                      [250, 59.5],
                      [173, 59.5]
                    ],
                    "metal_line_type": {
                      "override": "TECH.METAL.PAD.W81",
                      "values": {
                        "line_width": 81
                      }
                    }
                  },




   * gds file: Put the GDS file of the cell in this folder

   * cell.py

     ::

            from fnpcell import all as fp
            from gpdk.technology import get_technology
            from gpdk.util.json_cell import JsonCell


            class Edge_Coupler_1550(JsonCell, locked=True):

                json_path: fp.StrPath = "./json_file/edge_coupler_1550.json"
                gds_path: fp.StrPath = "./gds_file/edge_coupler_1550.gds"





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