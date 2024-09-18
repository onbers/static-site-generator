import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("value text")
        test_against = "LeafNode(None, value text, None)"
        self.assertEqual(repr(node), test_against)

    def test_to_html(self):
        node = LeafNode("value text", "a", {"prop1": "prop1 values"})
        to_html = '<a prop1="prop1 values">value text</a>'
        self.assertEqual(node.to_html(), to_html)

    def test_no_tag(self):
        node = LeafNode("value text")
        self.assertEqual(node.to_html(), "value text")

    def test_no_value(self):
        node = LeafNode("")
        with self.assertRaises(ValueError):
            node.to_html()



if __name__ == "__main__":
    unittest.main()