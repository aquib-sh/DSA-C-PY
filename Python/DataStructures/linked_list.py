class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    def isempty(self):
        return(self.val==None and self.next==None)

    def append(self, val):
        p = self
        while p.next != None:
            p = self.next
        p.next = Node(val)

    def __str__(self):
        string = "("
        p = self
        while p.next != None:
            string += (str(p.val)+", ")
            p = p.next

        string += (str(p.val))
        string += ")"
        return string

            
