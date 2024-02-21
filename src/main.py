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


    random = src.algorithms.random.Random()

    roots = src.algorithms.roots.Roots()

    logger.info(roots.exc(value=random.exc()))
    logger.info(roots.exc(value=random.exc()))

    
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

    main()
