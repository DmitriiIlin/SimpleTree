"""
Реализация класса Simple Tree
"""

class SimpleTreeNode:
# Реализация узла дерева

    def __init__(self, val, parent):
        # Инициализация узла дерева 
        self.NodeValue=val
        self.Parent=parent
        self.Children=[]

class SimpleTree:
    #Реализация дерева

    def __init__(self, root):
        #Инициализация класса SimpleTree
        self.Root=root

    def AddChild(self, ParentNode, NewChild):
        #Добавление дочернего узла к предыдущему
        if self.Root is None and ParentNode==None and NewChild!=None:
            self.Root=NewChild
        elif self.Root!=None and ParentNode!=None and NewChild!=None:
            NewChild.Parent=ParentNode
            ParentNode.Children.append(NewChild)
        else:
            pass
  
    def GetAllNodes(self,allNodes=[]):
        # ваш код выдачи всех узлов дерева в определённом порядке
        if self.Root is None:
            return allNodes
        else:
            if not (self.Root in allNodes): 
                allNodes.append(self.Root)
            if self.Root.Children!=None:
                children_massive=self.Root.Children
                for children in children_massive:
                    self.Root=children
                    self.GetAllNodes()           
        self.Root=allNodes[0]
        return allNodes
            
    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        if val!=None and self.GetAllNodes()!=None:
            output=[]
            Nodes_in_Tree=self.GetAllNodes()
            for everynode in range(self.Count()):
                if Nodes_in_Tree[everynode].NodeValue==val:
                    output.append(Nodes_in_Tree[everynode])
            return output
        else: 
            return None 

    def Count(self):
        # количество всех узлов в дереве
        nodes_qty=self.GetAllNodes()
        return len(nodes_qty)

    def Print_all_Nodes(self):
        # печать значений элементов
        all_Nodes=self.GetAllNodes()
        all_Nodes_for_print=[]
        for i in range(self.Count()):
            all_Nodes_for_print.append(all_Nodes[i].NodeValue)
        print(all_Nodes_for_print)
        
    def DeleteNode(self, NodeToDelete):
        # ваш код удаления существующего узла NodeToDelete
        if NodeToDelete!=None:
            Nodes_in_Tree=self.GetAllNodes()
            print(self.GetAllNodes())
            if NodeToDelete in Nodes_in_Tree:
                Parent_Node=NodeToDelete.Parent
                Parent_Node_Children=Parent_Node.Children
                for i in range(0,len(Parent_Node_Children)):
                    if Parent_Node_Children[i]==NodeToDelete:
                        number_to_delete=i
                Parent_Node_Children.pop(number_to_delete)
                Children=NodeToDelete.Children
                for everynode in Children:
                    everynode.Parent=Parent_Node
                NodeToDelete.NodeValue=None
        elif NodeToDelete==self.Root:
            pass


    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом -- 
        # в качестве дочернего для узла NewParent
        all_Nodes_for_move=self.GetAllNodes()
        if NewParent and OriginalNode in all_Nodes_for_move:
            if NewParent==OriginalNode.Parent:
                pass
            elif NewParent!=OriginalNode.Parent:
                old_Parent=OriginalNode.Parent
                old_Parent.Children.remove(OriginalNode)
                OriginalNode.Parent=NewParent
                NewParent.Children.append(OriginalNode)
        elif OriginalNode in all_Nodes_for_move and NewParent==None:
            pass
        else:
            pass

    def LeafCount(self):
        # количество листьев в дереве
        all_Nodes=self.GetAllNodes()
        all_leaf=[]
        for everynode in all_Nodes:
            if everynode.Children==[]:
                all_leaf.append(everynode)
            else:
                pass
        
        return len(all_leaf)

"""    
A=SimpleTreeNode(1,None)
B=SimpleTreeNode(2,None)
D=SimpleTreeNode(3,None)
C=SimpleTreeNode(4,None)
F=SimpleTreeNode(5,None)
Tree=SimpleTree(A)
Tree.AddChild(A,B)
Tree.AddChild(A,D)
Tree.AddChild(B,C)
Tree.AddChild(C,F)
for node in Tree.GetAllNodes():
    print(node.NodeValue," ",node.Children)
print("количество листьев",Tree.LeafCount())
Tree.MoveNode(F,A)
for node in Tree.GetAllNodes():
    print(node.NodeValue," ",node.Children)
Tree.DeleteNode(B)
print("*********")
print(Tree.GetAllNodes())
print("*********")
for node in Tree.GetAllNodes():
    print(node.NodeValue," ",node.Children)
       
Tree2=SimpleTree(B)
Z=[Tree,Tree2]
print(Z)
Z.remove(Tree)
print(Z)
"""


