################
""" Test the Task data Type """
################


from collections import namedtuple 


Task = namedtuple("Task", ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None , None , False , None )


def test_asdict(): 
    ################
    """_asdict() returns dictionary  """
    ################
    
    t_task = Task("do something","Ram",True ,21 )
    t_dict = t_task._asdict()
    expected = {
        "summary" : "do something",
        "owner"  : "Ram",        
        "done" : True ,
        "id" : 21}
    assert t_dict == expected
    
    
def test_replace():
    ################
    """replace() changes passed in fields."""
################
    t_before  = Task("finish book","Syam" ,False)
    t_after = t_before._replace(id = 10 , done = True )
    t_expected = Task("finish book", "Syam", True , 10)
    assert t_after == t_expected 


