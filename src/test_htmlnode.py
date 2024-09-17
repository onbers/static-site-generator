import unittest

from htmlnode import HTMLNode

#HTMLNode(tag, value, children, props)
class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag", "value","children", {"key": "value", "key2": "value2"})
        test_against = ' key="value" key2="value2"'
        self.assertEqual(node.props_to_html(), test_against)

    def test_eq2(self):
        node = HTMLNode("tag", "value", "children", None)
        test_against = ""
        self.assertEqual(node.props_to_html(), test_against)

    def test_eq3(self):
        node = HTMLNode()
        test_against = ""
        self.assertEqual(node.props_to_html(), test_against)

    def test_eq4(self):
        node = HTMLNode(props={"key": "value"})
        test_against = ' key="value"'
        self.assertEqual(node.props_to_html(), test_against)


if __name__ == "__main__":
    unittest.main()
