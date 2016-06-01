# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from gt.theme.testing import GT_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that gt.theme is properly installed."""

    layer = GT_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if gt.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'gt.theme'))

    def test_browserlayer(self):
        """Test that IGtThemeLayer is registered."""
        from gt.theme.interfaces import (
            IGtThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IGtThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = GT_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['gt.theme'])

    def test_product_uninstalled(self):
        """Test if gt.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'gt.theme'))

    def test_browserlayer_removed(self):
        """Test that IGtThemeLayer is removed."""
        from gt.theme.interfaces import IGtThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IGtThemeLayer, utils.registered_layers())
