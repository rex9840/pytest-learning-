################
""" Test the Task data Type """
################

from collections import namedtuple


Task = namedtuple('Task', ['summary','owner','done','id'])

Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults(): 
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None,None,False , None)
    
    assert t1 == t2 

def test_member_access(): 
    """Check field functionality of nametuple """
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)
    


##############################
"""__new__.__defaults__ to create Task objects without having to specify all the
fields. 

The test_defaults() test is there to demonstrate and validate how the defaults work.

The test_member_access() test is to demonstrate how to access members by name and not by
index, which is one of the main reasons to use namedtuples."""
##############################


