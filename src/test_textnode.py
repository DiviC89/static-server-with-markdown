import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("I am your father", "bold", "allyourbaseisbelongto.us")
        node2 = TextNode("I am your child", "bold", "allyourbaseisbelongto.us")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("I am your father", "bold", "allyourbaseisbelongto.us")
        node2 = TextNode("I am your father", "bold", "allyourbaseisbelongto.you")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("I am your father", "bold", "allyourbaseisbelongto.us")
        node2 = TextNode("I am your father", "bold", "allyourbaseisbelongto.us")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "text", "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
