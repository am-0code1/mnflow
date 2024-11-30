.. _block:

Block
------

Various DLD systems can be produced based on the themes available from 
``mnflow.mfda.cad.dld.theme``. 
The ``mnflow.mfda.cad.dld.theme.block.DLD`` class is the most basic one; a DLD
system with uniform gap throughout the channel. Yet, it is an important 
building block for making more complex systems.

The method :py:func:`mnflow.mfda.cad.dld.theme.block.DLD.process()` is the 
`class method` to configure the layout of a DLD block. This method is 
automatically invoked from the constructor.

.. hint::
   Some of the use cases of the class ``DLD``:
	- Instantiating a ``DLD`` object to be configured to produce a DLD-based system with a uniform gap throughout the system, `e.g.`, a condenser.
	- Instantiating multiple ``DLD`` objects with different gaps to be configured to produce a DLD-based system with a non-uniform gap throughout the system, multi-stage DLD systems, etc.

.. autoclass:: mnflow.mfda.cad.dld.theme.block.DLD
   :members:
   :no-index: