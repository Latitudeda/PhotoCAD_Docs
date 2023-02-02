QuickStart to PhotoCAD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Important note: The script layout of the user manual cannot be identical to the format of the Python script, the code paragraphs in the manual are for illustrative purposes only. Please refer to the Python source code in the package for the actual code format.**

This section is for users who have installed PyCharm (Python 3.8) and are familiar with how to use PyCharm. For detailed documentation on **PhotoCAD**, please start from the Tutorial section.

1. After obtaining the **PhotoCAD** installation package, unzip it and find the "Installation Instructions.pdf" file; follow the detailed instructions in "Installation Instructions.pdf".

2. Once you have successfully installed **PhotoCAD** according to the installation instructions, you can continue with the following actions to quickly experience **PhotoCAD**. 

3. First look of the component unit script:

   In the current project of PyCharm, find ``External Libraries`` > ``site-packages`` > ``gpdk`` > ``components`` > ``bend`` > ``bend_bezier.py`` file and double-click it, it will open the python source code of Bessel type bend (as shown below):
   
   .. image:: ../images/quickstart1.png
   
   
4. Run the script and view the layout:

   After running ``bend_bezier.py``, a local folder will be generated under ``gpdk`` > ``components`` > ``bend``, and the ``bend_bezier.gds`` file will be generated in the local folder (currently there is already a local folder under the bend folder, no new local folder will be created after running the script, and the generated file will replace the file of the same name in the local folder by default). Note that there are two common ways to run this script file.
  
   4.1. Click the right button in the code editing area, and then click ``Run bend_bezier`` as indicated by the red arrow in the figure.


