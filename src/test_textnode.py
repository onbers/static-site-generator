import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq1(self):
        node = TextNode()
        node2 = TextNode()
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("This is a text node", None, "bold")
        node2 = TextNode("This is a text node", None, "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is the first next node", "bold")
        node2 = TextNode("This is the second next node", "bold")
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()