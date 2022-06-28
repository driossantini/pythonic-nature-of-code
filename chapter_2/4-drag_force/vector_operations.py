import numpy as np


def check_2D_vector(vector):
    """check if input is a 2D vector in the shape np.array([a,b])

    Args:
        vector (np.ndarray): _ A numpy vector
    """
    assert type(
        vector) == np.ndarray, f"The following value has to be a numpy array: {vector}"
    assert len(vector.shape) == 1 and sum(
        vector.shape) == 2, "The force has to be a 2D numpy array in the shape np.array([a,b])"


def normalise_vector(vector):
    """Normalises a vector

    Args:
        vector (numpy.ndarray): A numpy vector
    """
    return vector/np.linalg.norm(vector)


def set_magnitude(vector, mag):
    """Sets the magnitude of a vector to mag

    Args:
        vector (numpy.ndarray): The numpy vector
        mag (float): Desired magnitude
    """

    return mag * normalise_vector(vector)
