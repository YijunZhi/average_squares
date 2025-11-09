Average Squares Documentation
===============================================================================

Overview
-------------------------------------------------------------------------------

This project provides a small module ``squares`` with a few utility functions,
e.g. computing the (weighted) average of squares and converting mixed strings
to numbers. The documentation below is generated from the code's docstrings.

Examples
-------------------------------------------------------------------------------

Here are a few quick examples you can try in Python:

.. code-block:: pycon

    >>> from squares import average_of_squares, convert_numbers
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> convert_numbers(["4", " 8 ", "15 16", " 23   42 "])
    [4, 8, 15, 16, 23, 42]

API Reference
-------------------------------------------------------------------------------

.. automodule:: squares
   :members:
   :undoc-members:
   :show-inheritance:
