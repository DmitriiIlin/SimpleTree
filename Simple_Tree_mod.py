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
            if NodeToDelete in Nodes_in_Tree:
                Parent_Node=NodeToDelete.Parent
                Children=NodeToDelete.Children
                for everynode in Children:
                    everynode.Parent=Parent_Node
        elif NodeToDelete==self.Root:
            self.Root=None 


    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом -- 
        # в качестве дочернего для узла NewParent
        all_Nodes=self.GetAllNodes()
        if NewParent and OriginalNode in all_Nodes:
            if NewParent==OriginalNode.Parent:
                pass
            elif NewParent!=OriginalNode.Parent:
                old_Parent=OriginalNode.Parent
                old_Parent.Children.remove(OriginalNode)
                OriginalNode.Parent=NewParent
                NewParent.Children.append(OriginalNode)
        elif OriginalNode in all_Nodes and NewParent==None:
            old_Parent=OriginalNode.Parent
            print(old_Parent.Children)
            old_Parent.Children.remove(OriginalNode)
            print(old_Parent.Children)
            OriginalNode.Parent=None
            self.Root=OriginalNode
            print(self.GetAllNodes())
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
        return all_leaf

      

A=SimpleTreeNode(1,None)
B=SimpleTreeNode(2,None)
D=SimpleTreeNode(3,None)
C=SimpleTreeNode(4,None)
F=SimpleTreeNode(5,None)
Tree=SimpleTree(A)
Tree.AddChild(A,B)
Tree.AddChild(B,D)
Tree.AddChild(B,C)
Tree.AddChild(C,F)
E=SimpleTreeNode(10,None)
R=SimpleTreeNode(20,None)
Tree.AddChild(F,E)
Tree.AddChild(F,R)
AA=A.Children
BB=B.Children
DD=D.Children
CC=C.Children
FF=F.Children
EE=E.Children
RR=R.Children
Root=Tree.Root
Tree.MoveNode(F,None)
print("*********")
print(A.Children==AA)
print(B.Children==BB)
print(D.Children==DD)
print(C.Children==CC)
print(F.Children==FF)
print(E.Children==EE)
print(R.Children==RR)
print("*********")
print(Root==Tree.Root)

            




