class TreeNode():
    def __init__(self,data):
        self.data = data
        self.firstnode = None
        self.secondnode = None
        self.thirdnode = None
        self.fourthnode = None
        self.fifthnode = None
        self.sixthnode = None
        self.seventhnode = None



menu = TreeNode("Menu")
snaks = TreeNode("Snaks")
special = TreeNode("Taj Special")
sandwiches = TreeNode("Sandwiches")
chaats = TreeNode("Chaats")
salads = TreeNode("Salads")
soup = TreeNode("Soups")
starter = TreeNode("Starters")

menu.firstnode = snaks
menu.secondnode = special
menu.thirdnode = sandwiches
menu.fourthnode = chaats
menu.fifthnode = salads
menu.sixthnode = soup
menu.seventhnode = starter

print(menu.__dict__)

