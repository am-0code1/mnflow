mnFlow Documentation
======================

Micro-nanoflow (`mnFlow`) library is aimed at providing the community with tools for design and modeling of micro-nanofluidic chips.
The current focus of the project is on :ref:`Deterministic Lateral Displacement (DLD) [1] <Refs>` structures.
In particular, the DLD design automation (DDA) tool aims at automating the entire process of design and production of computer-aided design (CAD) files for DLD-based micro-nanofluidic chips.
The produced CAD files can be used for computational modeling, optimization, and manufacturing of DLD devices.

Check out the :doc:`usage` section for further information, including how to install the package as well as a quick start.
The :doc:`tutorials` section also includes a set of examples to introduce various features of the package.
Finally, the :doc:`manual` section describes how the package works under the hood.
For information on how to cite the related works see :ref:`Citation <Citation>`.

.. note::

   This project is under development.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   usage
   tutorials
   manual
   api


Acknowledgments
----------------

This project utilizes the packages mentioned in the following.
We gratefully acknowledge their contributions to this project.

- `klayout <https://github.com/KLayout/klayout>`_: For creating CAD layouts.
- `numpy <https://github.com/numpy/numpy>`_: For numerical computations.
- `pillow <https://github.com/python-pillow/Pillow>`_: For creating image of layouts.
- `scipy <https://github.com/scipy/scipy>`_: For solving equations.
- `matplotlib <https://github.com/matplotlib/matplotlib>`_: For data visualization
- `black <https://github.com/psf/black>`_, `flake8 <https://github.com/PyCQA/flake8>`_, and `isort <https://github.com/PyCQA/isort>`_: For linting and formatting codes.
- `git <https://github.com/git/git>`_ and `pre-commit <https://github.com/pre-commit/pre-commit>`_: For revision control and pre-commit hooks, respectively.
- `sphinx <https://github.com/sphinx-doc/sphinx>`_, and `sphinx-rtd-theme <https://github.com/readthedocs/sphinx_rtd_theme>`_: For creating docs.
- `pytest <https://github.com/pytest-dev/pytest>`_, and `pytest-cov <https://github.com/pytest-dev/pytest-cov>`_: For creating test cases.


.. _Citation:

Citation
--------
If you use this work in your research, please cite the relevant works associated with it as listed in the following.

Original paper
^^^^^^^^^^^^^^
**A. Mehboudi**, **S. Singhal**, and **S.V. Sreenivasan**, **A universal framework for design and manufacture of deterministic lateral displacement chips**, *Lab on a Chip*, 2024.
DOI: `10.1039/D4LC00838C <https://pubs.rsc.org/en/content/articlelanding/2025/lc/d4lc00838c>`_

Zenodo Archive
^^^^^^^^^^^^^^
**A. Mehboudi**, **mnFlow: A package for micro/nanoflow**, *Zenodo*, 2024.
DOI: `10.5281/zenodo.14357811 <https://zenodo.org/doi/10.5281/zenodo.14357811>`_


.. _Refs:

Refs
----
[1] `L. R. Huang, E. C. Cox, R. H. Austin and J. C. Sturm, Science, 2004, 304, 987-990. <https://www.science.org/doi/10.1126/science.1094567>`_
