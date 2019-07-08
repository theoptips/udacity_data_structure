import Group
import Queue

parent = Group.Group("parent")
child = Group.Group("child")
sub_child = Group.Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print("parent name is {}, child group name is {}, sub child group name is {} ".format(parent.get_name(), child.get_name(), sub_child.get_name()))
print("print parent group length {}".format(len(parent.get_groups())))
print("print group user of parent is {}".format(len(parent.get_users())))

print("print child group length {}".format(len(child.get_groups())))
print("print group user of child is {}".format(len(child.get_users())))

'''
pseudo code
each group gets put into a queue
each of the user gets checked before hand, never need to enter a queue
walk through all its members see if it is there

TODO test

TODO O(n)

'''

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group is None or user is None:
    	return False

    Q = Queue.Queue()
    Q.enqueue(group)

    while Q.size() != 0:
    	current = Q.dequeue()
    	group_group = current.get_groups()
    	group_user = current.get_users()
    	#group_name = current.get_name() # for checking only
    	for usr in group_user:
    		if usr == user:
    			return True
    	for grp in group_group:
    		Q.enqueue(grp)
    
    return False

print(is_user_in_group("sub_child_user",parent))

assert(is_user_in_group("sub_child_user",parent)==True)
assert(is_user_in_group("crazy_user",parent)==False)
assert(is_user_in_group("curve",child)==False)
curve = "curve"
child.add_user(curve)
assert(is_user_in_group("curve",child)==True)


'''
Big O
in this case is very similar to to the File Recursion
if we start with one group it has max of m groups, and each group can have max of n member
(m*m) + n for the first pass, then each of the m can have more (m*m)**depth) = m*(2*dpeth) power with is exponentation 
the n is neglegible

O(m** depth)
'''
