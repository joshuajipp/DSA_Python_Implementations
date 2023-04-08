class TNode:

    def __init__(self, data=None, balance=0, P=None, L=None, R=None):
        self.data = data
        self.left = L
        self.right = R
        self.parent = P
        self.balance = balance
    
    # Getters
    def get_data(self):
        return self.data
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_parent(self):
        return self.parent
    
    def get_balance(self):
        return self.balance
    
    # Setters
    def set_data(self, data):
        self.data = data
        
    def set_left(self, node):
        self.left = node
        
    def set_right(self, node):
        self.right = node
        
    def set_parent(self, node):
        self.parent = node
        
    def set_balance(self, balance):
        self.balance = balance
    
    # Print
    def print_node(self):
        print(f"Data: {self.data}, Balance: {self.balance}")
    
    # toString
    def __str__(self):
        return str(self.data)
