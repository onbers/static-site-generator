from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    
    leaf_node = LeafNode("value")
    leaf_node2 = LeafNode("value2", tag="b")
    leaf_node3 = LeafNode("value3", tag="i")

    parent_node = ParentNode([leaf_node, leaf_node2, leaf_node3], tag="p")

    leaf_node4 = LeafNode("value4", tag="b")
    leaf_node5 = LeafNode("value5")    

    parent_node2 = ParentNode([leaf_node4, leaf_node5, parent_node], tag="h1")

    print("parent node:")
    print(parent_node)
    print(parent_node.to_html())

    print("parent node 2:")
    print(parent_node2)
    print(parent_node2.to_html())


main()