
"""
DESCRIPTION:
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

"""
def remove_exclamation_marks(s):
    return ''.join( c for c in s if c not in '!')