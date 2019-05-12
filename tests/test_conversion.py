"""
Test the color-format conversion utilities.

"""
import unittest

import webcolors


class HexConversionTests(unittest.TestCase):
    """
    Test the functions which convert from hex color codes to other
    formats.

    """
    def test_hex_to_name(self):
        """
        Test conversion from hex to color name.
        """
        test_pairs = (
            (u'#ffffff', u'white'),
            (u'#fff', u'white'),
            (u'#000080', u'navy'),
            (u'#daa520', u'goldenrod')
        )

        for hex_value, name in test_pairs:
            self.assertEqual(
                name,
                webcolors.hex_to_name(hex_value)
            )

    def test_hex_to_name_unnamed(self):
        """
        A hex code which does not correspond to a named color, or does
        not correspond to a named color in the given specification,
        raises ValueError.

        """
        # No name in any spec.
        self.assertRaises(
            ValueError,
            webcolors.hex_to_name,
            '#123456'
        )

        # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
        self.assertRaises(
            ValueError,
            webcolors.hex_to_name,
            '#daa520',
            spec=u'html4'
        )

    def test_hex_to_name_specs(self):
        """
        Using one of the supported specifications succeeds; using an
        unsupported specification raises ValueError.

        """
        for supported_spec in (u'html4', u'css2', u'css21', u'css3'):
            self.assertEqual(
                u'white',
                webcolors.hex_to_name(
                    u'#ffffff',
                    spec=supported_spec
                )
            )

        for unsupported_spec in (u'css1', u'css4', u'html5'):
            self.assertRaises(
                ValueError,
                webcolors.hex_to_name,
                '#ffffff',
                spec=unsupported_spec
            )

    def test_hex_to_rgb(self):
        """
        Test conversion from hex to integer RGB triplet.

        """
        test_pairs = (
            (u'#fff', (255, 255, 255)),
            (u'#ffffff', (255, 255, 255)),
            (u'#000080', (0, 0, 128))
        )

        for hex_value, triplet in test_pairs:
            result = webcolors.hex_to_rgb(hex_value)
            self.assertTrue(
                isinstance(result, webcolors.IntegerRGB)
            )
            self.assertEqual(result, triplet)

    def test_hex_to_rgb_percent(self):
        """
        Test conversion from hex to percent RGB triplet.

        """
        test_pairs = (
            (u'#fff', (u'100%', u'100%', u'100%')),
            (u'#ffffff', (u'100%', u'100%', u'100%')),
            (u'#000080', (u'0%', u'0%', u'50%'))
        )

        for hex_value, triplet in test_pairs:
            result = webcolors.hex_to_rgb_percent(hex_value)
            self.assertTrue(
                isinstance(result, webcolors.PercentRGB)
            )
            self.assertEqual(result, triplet)


class IntegerRGBConversionTests(unittest.TestCase):
    """
    Test the functions which convert from integer RGB triplets to
    other formats.

    """
    def test_rgb_to_name(self):
        """
        Test conversion from integer RGB triplet to color name.

        """
        test_pairs = (
            ((255, 255, 255), u'white'),
            ((0, 0, 128), u'navy'),
            ((218, 165, 32), u'goldenrod'),
            (webcolors.IntegerRGB(218, 165, 32), u'goldenrod')
        )

        for triplet, name in test_pairs:
            self.assertEqual(name,
                             webcolors.rgb_to_name(triplet))

    def test_rgb_to_name_unnamed(self):
        """
        An integer RGB triplet which does not correspond to a named
        color, or does not correspond to a named color in the given
        specification, raises ValueError.

        """
        # No name in any spec.
        self.assertRaises(
            ValueError,
            webcolors.rgb_to_name,
            (18, 52, 86)
        )

        # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
        self.assertRaises(
            ValueError,
            webcolors.rgb_to_name,
            (218, 165, 32),
            spec=u'html4'
        )

    def test_rgb_to_name_specs(self):
        """
        Using one of the supported specifications succeeds; an
        unsupported specification raises ValueError.

        """
        for supported_spec in (u'html4', u'css2', u'css21', u'css3'):
            self.assertEqual(
                u'white',
                webcolors.rgb_to_name(
                    (255, 255, 255),
                    spec=supported_spec
                )
            )

        for unsupported_spec in (u'css1', u'css4', u'html5'):
            self.assertRaises(
                ValueError,
                webcolors.rgb_to_name,
                (255, 255, 255),
                spec=unsupported_spec
            )

    def test_rgb_to_hex(self):
        """
        Test conversion from integer RGB triplet to hex.

        """
        test_pairs = (
            ((255, 255, 255), u'#ffffff'),
            ((0, 0, 128), u'#000080'),
            ((218, 165, 32), u'#daa520')
        )

        for triplet, hex_value in test_pairs:
            self.assertEqual(
                hex_value,
                webcolors.rgb_to_hex(triplet)
            )

    def test_rgb_to_rgb_percent(self):
        """
        Test conversion from integer RGB triplet to percent RGB
        triplet.

        """
        test_pairs = (
            ((255, 255, 255), (u'100%', u'100%', u'100%')),
            ((0, 0, 128), (u'0%', u'0%', u'50%')),
            ((218, 165, 32), (u'85.49%', u'64.71%', u'12.5%'))
        )

        for triplet, percent_triplet in test_pairs:
            result = webcolors.rgb_to_rgb_percent(triplet)
            self.assertTrue(
                isinstance(result, webcolors.PercentRGB)
            )
            self.assertEqual(percent_triplet, result)


class NameConversionTests(unittest.TestCase):
    """
    Test the functions which convert from color names to other
    formats.

    """
    def test_name_to_hex(self):
        """
        Test correct conversion of color names to hex.
        """
        test_pairs = (
            (u'white', u'#ffffff'),
            (u'navy', u'#000080'),
            (u'goldenrod', u'#daa520')
        )

        for name, hex_value in test_pairs:
            self.assertEqual(
                hex_value,
                webcolors.name_to_hex(name)
            )

    def test_name_to_hex_bad_name(self):
        """
        A name which does not correspond to a color, or does not
        correspond to a color in the given specification, raises
        ValueError.

        """
        test_values = (
            {u'name': u'goldenrod',
             u'spec': u'html4'},
            {u'name': u'glue',
             u'spec': u'css21'},
            {u'name': u'breen',
             u'spec': u'css3'},
        )

        for kwarg_dict in test_values:
            self.assertRaises(
                ValueError,
                webcolors.name_to_hex,
                **kwarg_dict
            )

    def test_name_to_hex_specs(self):
        """
        Using one of the supported specifications succeeds; using an
        unsupported specification raises ValueError.

        """
        for supported_spec in (u'html4', u'css2', u'css21', u'css3'):
            self.assertEqual(
                u'#ffffff',
                webcolors.name_to_hex(
                    u'white',
                    spec=supported_spec
                )
            )

        for unsupported_spec in (u'css1', u'css4', u'html5'):
            self.assertRaises(
                ValueError,
                webcolors.name_to_hex,
                'white', spec=unsupported_spec
            )

    def test_name_to_rgb(self):
        """
        Test conversion from color name to integer RGB triplet.

        """
        test_pairs = (
            (u'white', (255, 255, 255)),
            (u'navy', (0, 0, 128)),
            (u'goldenrod', (218, 165, 32))
        )

        for name, triplet in test_pairs:
            result = webcolors.name_to_rgb(name)
            self.assertTrue(
                isinstance(
                    result,
                    webcolors.IntegerRGB
                )
            )
            self.assertEqual(triplet, result)

    def test_name_to_rgb_percent(self):
        """
        Test conversion from color name to percent RGB triplet.

        """
        test_pairs = (
            (u'white', (u'100%', u'100%', u'100%')),
            (u'navy', (u'0%', u'0%', u'50%')),
            (u'goldenrod', (u'85.49%', u'64.71%', u'12.5%'))
        )

        for name, triplet in test_pairs:
            result = webcolors.name_to_rgb_percent(name)
            self.assertTrue(
                isinstance(result, webcolors.PercentRGB)
            )
            self.assertEqual(triplet, result)


class PercentRGBConversionTests(unittest.TestCase):
    """
    Test the functions which convert from percent RGB triplets to
    other formats.

    """
    def test_rgb_percent_to_name(self):
        """
        Test conversion from percent RGB triplet to color name.
        """
        test_pairs = (
            ((u'100%', u'100%', u'100%'), u'white'),
            ((u'0%', u'0%', u'50%'), u'navy'),
            ((u'85.49%', u'64.71%', u'12.5%'), u'goldenrod'),
            (webcolors.PercentRGB(u'85.49%', u'64.71%', u'12.5%'),
             u'goldenrod')
        )

        for triplet, name in test_pairs:
            self.assertEqual(
                name,
                webcolors.rgb_percent_to_name(triplet)
            )

    def test_rgb_percent_to_name_unnamed(self):
        """
        A percent RGB triplet which does not correspond to a named
        color, or does not correspond to a named color in the given
        specification, raises ValueError.

        """
        # No name in any spec.
        self.assertRaises(
            ValueError,
            webcolors.rgb_percent_to_name,
            (u'7.06%', u'20.39%', u'33.73%')
        )

        # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
        self.assertRaises(
            ValueError,
            webcolors.rgb_percent_to_name,
            (u'85.49%', u'64.71%', u'12.5%'),
            spec=u'html4'
        )

    def test_rgb_percent_to_name_specs(self):
        """
        Using one of the supported specifications succeeds; an
        unsupported specification raises ValueError.

        """
        for supported_spec in (u'html4', u'css2', u'css21', u'css3'):
            self.assertEqual(
                u'white',
                webcolors.rgb_percent_to_name(
                    (u'100%', u'100%', u'100%'),
                    spec=supported_spec
                )
            )

        for unsupported_spec in (u'css1', u'css4', u'html5'):
            self.assertRaises(
                ValueError,
                webcolors.rgb_percent_to_name,
                (u'100%', u'100%', u'100%'),
                spec=unsupported_spec
            )

    def test_rgb_percent_to_hex(self):
        """
        Test conversion from percent RGB triplet to hex.

        """
        test_pairs = (
            ((u'100%', u'100%', u'0%'), u'#ffff00'),
            ((u'0%', u'0%', u'50%'), u'#000080'),
            ((u'85.49%', u'64.71%', u'12.5%'), u'#daa520')
        )

        for triplet, hex_value in test_pairs:
            self.assertEqual(
                hex_value,
                webcolors.rgb_percent_to_hex(triplet)
            )

    def test_rgb_percent_to_rgb(self):
        """
        Test conversion from percent RGB triplet to integer RGB
        triplet.

        """
        test_pairs = (
            ((u'100%', u'100%', u'0%'), (255, 255, 0)),
            ((u'0%', u'0%', u'50%'), (0, 0, 128)),
            ((u'85.49%', u'64.71%', u'12.5%'), (218, 165, 32))
        )

        for triplet, int_triplet in test_pairs:
            result = webcolors.rgb_percent_to_rgb(triplet)
            self.assertTrue(
                isinstance(result, webcolors.IntegerRGB)
            )
            self.assertEqual(int_triplet, result)
