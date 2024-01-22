Design rule check(DRC)
==============================

Design Rule Check (DRC) is a crucial step in the photonics/electronic design automation (EDA) process for photonics integrated circuits (PICs). It is a verification process that ensures the compliance of a photonics layout or design with a set of predefined rules and constraints. The primary goal of DRC is to identify and rectify potential issues or violations in the layout that could lead to manufacturing defects, reliability issues, or functional failures in the final product.

DRC is an integral part of the PICs design flow, typically performed after the completion of the physical layout but before the fabrication process begins. It helps ensure that the design adheres to the specifications provided by the foundry or fabrication facility.

Most common type of design rules are:

1. Exclusion_
2. Inclusion_
3. Minimum_width_
4. Other rules provided by specific foundries

Exclusion
^^^^^^^^^^^^^^^^^

Specifies the minimum allowable distance between adjacent features (such as waveguides, metal layers) to prevent optical crosstalk or electrical interference

.. image:: ../images/drc_exclusion.png

Inclusion
^^^^^^^^^^^^^^

Specifies the minimum distance between the edge of a feature and the nearest edge of an adjacent feature, ensuring proper isolation.

.. image:: ../images/drc_inclusion.png

Minimum_width
^^^^^^^^^^^^^^^^^^

Defines the minimum allowable width for waveguides or other features to ensure proper functionality and manufacturability.

.. image:: ../images/drc_width.png
