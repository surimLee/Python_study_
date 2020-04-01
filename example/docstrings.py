# docstrings.py

def square(n):
    """Return the squatr of a number n."""
    return n ** 2

def get_username(userid):
    """Return the name of a user given their id. """
    return db.get(user_id=userid).username
