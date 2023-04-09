class TNode:

    def __init__(self, data=None, balance=0, P=None, L=None, R=None):
        self.data = data
        self.left = L
        self.right = R
        self.parent = P
        self.balance = balance
    
    # Getters
    def getData(self):
        return self.data
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getParent(self):
        return self.parent
    
    def getBalance(self):
        return self.balance
    
    # Setters
    def setData(self, data):
        self.data = data
        
    def setLeft(self, node):
        self.left = node
        
    def setRight(self, node):
        self.right = node
        
    def setParent(self, node):
        self.parent = node
        
    def setBalance(self, balance):
        self.balance = balance
    
    # Print
    def printNode(self):
        print(f"Data: {self.data}, Balance: {self.balance}")
    
    # toString
    def __str__(self):
        return str(self.data)
