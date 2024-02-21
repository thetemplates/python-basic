"""Module main.py"""
import logging
import os
import sys


def main():
    """
    Entry point
    """

    # Logging
    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('Templates')

    # The square root of a random number
    example: float = random.exc()
    logger.info('The square root of %s: %s', example, roots.exc(value=example))

    # Deleting __pycache__
    src.functions.cache.Cache().delete()


if __name__ == '__main__':

    # Setting-up
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Classes
    import src.functions.cache
    import src.algorithms.random
    import src.algorithms.roots

    # Instances
    random = src.algorithms.random.Random()
    roots = src.algorithms.roots.Roots()

    main()
