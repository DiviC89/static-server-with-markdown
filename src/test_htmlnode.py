import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        prop1 = {"href": "google.com", "target": "_blank"}
        node = HTMLNode(None, prop1, "p", "this is a value")
        print(node.props_to_html_method())
        self.assertEqual(node.props_to_html_method(), node.props_to_html_method())

    def test_eq_false(self):
        prop1 = {"href": "www.google.com", "target": "_blank"}
        node = HTMLNode(None, prop1, "p", "this is a value")
        node2 = HTMLNode(None, prop1, "a", "this is a value")
        self.assertNotEqual(node, node2)
