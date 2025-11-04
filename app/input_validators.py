import warnings
warnings.filterwarnings("ignore")



def is_number(value):
    """Check if the input value can be interpreted as a number (int or float)."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


