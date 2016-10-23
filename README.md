# Project Overview

PySize is a simple lightweight tool for converting quantities between defined units.

# Installation

Installing the easy way, using pip:

    $ pip install pysize

# Basic Usage

With PySize it's easy to calculate a conversion from one unit to another.

    >>> from pysize import convert
    
    >>> a = convert(1.0).frm('m').to('mm')
    >>> print(a)
    1000.0

The conversion functionality even works with NumPy arrays.

    >>> a = numpy.array([[1.0, 2.0], [3.0, 4.0]])
    >>> print(a)
    [[ 1.  2.]
     [ 3.  4.]]
    >>> b = convert(a).frm('m').to('mm')
    >>> print(b)
    [[ 1000.  2000.]
     [ 3000.  4000.]]

One can also convert units combined with multiplication and/or division.

    >>> a = 60.0  # In miles per hour
    >>> b = convert(a).frm('mi/h').to('ft/s')  # Coverts to feet per second
    >>> print(b)
    88.0

Exponents are parsed and applied correctly.

    >>> a = 10.0  # cubic yards
    >>> b = convert(a).frm('yd^3').to('ft^3')  # Coverts to cubic feet
    >>> print(b)
    270.0

To view a list valid conversions from a unit, use the `options` function.

    >>> opts = options('mm')
    >>> print(opts)
    ['km', 'm', 'dm', 'cm', 'mm']

Options can also be shown after defining the 'from' unit.

    >>> opts = convert(1.0).frm('mm').options()
    >>> print(opts)
    ['km', 'm', 'dm', 'cm', 'mm']

# Contributing

For developers, it's important to use common best practices when contributing to the project.
[PEP 8](https://www.python.org/dev/peps/pep-0008/) should always be adhered. Code should be
documented with [Google style docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
Pull requests and filing issues are encouraged.

To start contributing with the PySize repository:

1. Fork it!

2. Create a local clone of your fork.
    
        $ git clone https://github.com/YOUR-USERNAME/pysize
        Cloning into `pysize`...
        remote: Counting objects: 10, done.
        remote: Compressing objects: 100% (8/8), done.
        remove: Total 10 (delta 1), reused 10 (delta 1)
        Unpacking objects: 100% (10/10), done.

3. Set up a clean working environment, using virtualenv.

        $ virtualenv -p python3 venv
        $ source venv/bin/activate
        $ pip install -r requirements.txt

4. Add the original as a remote repository named `upstream`.

        $ git remote add upstream https://github.com/benjiyamin/pysize.git
        $ git remote -v
        origin    https://github.com/YOUR-USERNAME/pysize.git (fetch)
        origin    https://github.com/YOUR-USERNAME/pysize.git (push)
        upstream  https://github.com/benjiyamin/pysize.git (fetch)
        upstream  https://github.com/benjiyamin/pysize.git (push)

5. Fetch the current upstream repository branches and commits.

        $ git fetch upstream
        remote: Counting objects: 75, done.
        remote: Compressing objects: 100% (53/53), done.
        remote: Total 62 (delta 27), reused 44 (delta 9)
        Unpacking objects: 100% (62/62), done.
        From https://github.com/benjiyamin/pysize
         * [new branch]      master     -> upstream/master

6. Checkout your local `master` branch and sync `upstream/master` to it, without losing local changes.

        $ git checkout master
        Switched to branch 'master'
        
        $ git merge upstream/master

7. Commit your local changes and push to `upstream/master`.

        $ git commit -m 'Add some feature'
        $ git push upstream master

8. Submit a pull request. =)

For a list of contributors who have participated in this project, check out [AUTHORS](AUTHORS.md).

# Testing

Unit Testing is currently done using the built-in unittest module:

    $ python tests.py

# License

This project is licensed under GPL 3.0 - see [LICENSE](LICENSE.md) for details.
