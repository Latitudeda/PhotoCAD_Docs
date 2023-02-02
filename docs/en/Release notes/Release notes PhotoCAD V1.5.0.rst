PhotoCAD V1.5.0 Update Content
The long-awaited version update is here, and the software will support more concise design syntax and more efficient design methods, while normalizing some ambiguous content.
1.	When building pcell, you can define the class of the design device without using the decorator @fp.pcell_class(band= "C"). Instead, you can specify something like: class RingResonator(PCell, band="C") when defining the class. 
2.	When building the pcell, the decorator @dataclass and its corresponding simplified notation, please refer to example_pcell_dataclass_with_final.py and example_pcell_dataclass_with_final.py in examples of gpdk; Simplified writing can cause some ides to fail to provide automatic code completion when code is written. 
3.	When defining the pcell parameter, there is no need to use the as_field( ) method. 
4.	The newly added process layer switching function allows users to quickly define process information through CSV files and switch the currently used process information to custom process information through simple operation. Please refer to Chapter 4, Section 5 of the PhotoCAD User Manual. 
5.	Updated wg.py file; The function of wg.py in technology can generate a wg.csv file by running the file, so that users can quickly view the waveguide and bend information corresponding to each waveguide type. Please refer to Section 5 of Chapter 4 of the PhotoCAD User Manual. 
6.	Added a simplified way to write fp.g.path: fp.path, which currently has the same functionality for both writing methods. 
7.	Correct fp.el.Rect( ), The parameter name of the center point of the receiving rectangle in the method was changed from origin to center, and the origin parameter can still be used; Provide bottom_left parameters; Enhancing the coner_radius parameter to receive a value of 0, such as assigning it to [0,10,0,0] will result in a rectangle with rounded corners in the lower left corner. 
8.	The fp.el.Label method supports the anchor parameter to align labels from the start, center, or end point. 
9.	The disabled attribute is added to Pin and Port.
10.	Updated fp.until_x，fp.until_y，fp.START，fp.PREV，fp.END method in waylines. And simplify the writing of these complex expressions, no need to write '( )' later. 
11.	`import_from_json` supports layer mapped to `(layer, xtype)` instead of layer name(eg. `TECH.LAYER.FWG_CORE`).
12.	Enhanced the functionality of minor SDL. 

Dear users, you can now contact support@latitudea.com to get the PhotoCAD V1.5.0 software to experience the above update.
