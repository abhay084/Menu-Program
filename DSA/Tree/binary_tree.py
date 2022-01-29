class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def preorderTraverse(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorderTraverse(rootNode.leftchild)
    preorderTraverse(rootNode.rightchild)


def inordertraverse(rootNode):
    if not rootNode:
        return
    inordertraverse(rootNode.leftchild)
    print(rootNode.data)
    inordertraverse(rootNode.rightchild)


def postordertraverse(rootNode):
    if not rootNode:
        return
    postordertraverse(rootNode.leftchild)
    postordertraverse(rootNode.rightchild)
    print(rootNode.data)

rootNode = TreeNode("Menu")
food = TreeNode("Food")
snaks = TreeNode("Snacks")
drink = TreeNode("Drinks")
sandwiches = TreeNode("Sandwiches")
Cofee = TreeNode("Cofee")
coke = TreeNode("Coke")


rootNode.leftchild = food
rootNode.rightchild = drink
food.leftchild = snaks
food.rightchild = sandwiches
drink.leftchild = coke
drink.rightchild = Cofee

print(rootNode.__dict__)


preorderTraverse(rootNode)

print("\n")
inordertraverse(rootNode)
print("\n")
postordertraverse(rootNode)


