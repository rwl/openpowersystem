# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

from cim14.iec61970.core import IdentifiedObject
from cim14.iec61968.common import Location
from cim14.iec61968.common import PositionPoint
from cim14 import Element

from cim14.iec61970.domain import AngleDegrees
from cim14.iec61970.domain import FloatQuantity

# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

QueryGrammarKind = db.StringProperty(choices=("xquery", "xpath", "other"))

ns_prefix = "cim.IEC61968.Informative.InfGMLSupport"
ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#IEC61968.Informative.InfGMLSupport"

class GmlSvgParameter(IdentifiedObject):
    """ Refers to an SVG/CSS graphical-formatting parameter. The parameter is identified using the 'name' attribute and the content of the element gives the SVG/CSS-coded value.
    """

    # The attribute of the GmlSvgParameter. E.g., for 'Stroke', the following SvgParameters may be used: 'stroke' (color), 'stroke-opacity', 'stroke-width', 'stroke-linejoin', 'stroke-linecap', 'stroke-dasharray', and 'stroke-dashoffset'. Others are not officially supported.
    attribute = db.StringProperty()
    # The SVG/CSS-coded value of the associated SvgAttribute.
    value = db.StringProperty()
#    gml_stokes = db.ListProperty(db.Key)

#    @property
#    def gml_svg_parameters(self):
#        return GmlStroke.gql("WHERE gml_stokes = :1", self.key())
#    gml_fonts = db.ListProperty(db.Key)

#    @property
#    def gml_svg_parameters(self):
#        return GmlFont.gql("WHERE gml_fonts = :1", self.key())
#    gml_fills = db.ListProperty(db.Key)

#    @property
#    def gml_svg_parameters(self):
#        return GmlFill.gql("WHERE gml_fills = :1", self.key())

class GmlColour(IdentifiedObject):
    """ The solid color that will be used. The color value is RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign. The hexadecimal digits between A and F may be in either uppercase or lowercase. For example, full red is encoded as '#ff0000' (with no quotation marks). If the Stroke cssParameter element is absent, the default color is defined to be black ('#000000').
    """

    # The color value for BLUE (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.).
    blue = db.StringProperty()
    # The color value for RED (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.)
    red = db.StringProperty()
    # The color value for GREEN (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.)
    green = db.StringProperty()
    # The 'gml_fills' property has been implicitly created by
    # the gml_colour' property of GmlFill.
    pass
    # The 'gml_fonts' property has been implicitly created by
    # the gml_colour' property of GmlFont.
    pass
    # The 'gml_strokes' property has been implicitly created by
    # the gml_colour' property of GmlStroke.
    pass

class GmlDiagramObject(Location):
    """ Any of the magnitudes that serve to define the position of a point by reference to a fixed figure, system of lines, etc.
    """

    # The 'gml_raster_symbols' property has been implicitly created by
    # the gml_diagram_object' property of GmlRasterSymbol.
    pass
    # The 'gml_point_symbols' property has been implicitly created by
    # the gml_diagram_object' property of GmlPointSymbol.
    pass
#    diagrams = db.ListProperty(db.Key)

#    @property
#    def gml_diagram_objects(self):
#        return Diagram.gql("WHERE diagrams = :1", self.key())
    # The 'gml_polygon_symbols' property has been implicitly created by
    # the gml_diagram_object' property of GmlPolygonSymbol.
    pass
    # The 'gml_line_symbols' property has been implicitly created by
    # the gml_diagram_object' property of GmlLineSymbol.
    pass
#    gml_coordinate_systems = db.ListProperty(db.Key)

#    @property
#    def gml_diagram_objects(self):
#        return GmlCoordinateSystem.gql("WHERE gml_coordinate_systems = :1", self.key())
    # The 'gml_text_symbols' property has been implicitly created by
    # the gml_diagram_object' property of GmlTextSymbol.
    pass

class GmlGraphic(IdentifiedObject):
    """ A 'graphic symbol' with an inherent shape, color(s), and possibly size. A 'graphic' can be very informally defined as 'a little picture' and can be of either a raster or vector-graphic source type.
    """

    # Vertical scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbars).
    y_scale = db.FloatProperty()
    # The identifier of the symbol, if not derived from the type of CIM object (PSR, Asset, Organisation, Document, etc.) gmlSymbolPlacement is associated with.
    symbol_id = db.StringProperty()
    # Gives the rotation of a graphic in the clockwise direction about its center point in decimal degrees, encoded as a floating-point number. Negative values mean counter-clockwise rotation. The default value is 0.0 (no rotation). Note that there is no connection between source geometry types and rotations; the point used for plotting has no inherent direction. Also, the point within the graphic about which it is rotated is format dependent. If a format does not include an inherent rotation point, then the point of rotation should be the centroid.
    rotation = AngleDegrees
    # The minimum symbol size allowed.
    min_size = db.IntegerProperty()
    # Gives the absolute size of the graphic in pixels encoded as a floatingpoint number. The default size for an object is context-dependent. Negative values are not allowed.
    size = db.IntegerProperty()
    # Horizontal scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbar).
    x_scale = db.FloatProperty()
    # Specifies the level of translucency to use when rendering the Graphic.The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
    opacity = db.FloatProperty()
    # The 'gml_point_symbols' property has been implicitly created by
    # the gml_graphic' property of GmlPointSymbol.
    pass
#    gml_marks = db.ListProperty(db.Key)

#    @property
#    def gml_graphics(self):
#        return GmlMark.gql("WHERE gml_marks = :1", self.key())

class GmlFill(IdentifiedObject):
    """ Specifies how the area of the geometry will be filled.
    """

    # Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
    opacity = db.FloatProperty()
#    gml_colour = db.ReferenceProperty()
    # The 'gml_polygon_symbols' property has been implicitly created by
    # the gml_fill' property of GmlPolygonSymbol.
    pass
#    gml_marks = db.ListProperty(db.Key)

#    @property
#    def gml_fills(self):
#        return GmlMark.gql("WHERE gml_marks = :1", self.key())
    # The 'gml_text_symbols' property has been implicitly created by
    # the gml_fill' property of GmlTextSymbol.
    pass
#    gml_svg_parameters = db.ListProperty(db.Key)

#    @property
#    def gml_fills(self):
#        return GmlSvgParameter.gql("WHERE gml_svg_parameters = :1", self.key())

class GmlSelector(IdentifiedObject):
    """ A diagram element that allows selection by a user, i.e. as 'hyperNode' for navigating between diagrams, or as composite object representing multiple grouped objects.
    """

#    locations = db.ListProperty(db.Key)

#    @property
#    def gml_selectors(self):
#        return Location.gql("WHERE locations = :1", self.key())
    # The 'change_items' property has been implicitly created by
    # the gml_selector' property of ChangeItem.
    pass

class GmlLabelPlacement(IdentifiedObject):
    """ Used to position a label relative to a point or a line.
    """

    # Type of 'LabelPlacement' which in turn specifies where and how a text label should be rendered relative to a geometry.
    type = db.StringProperty()
    # Perpendicular distance away from a line to draw a label. The distance is in pixels and is positive to the left-hand side of the line string. Negative numbers mean right. The default offset is 0.
    offset = db.StringProperty()
    # Y displacement from the main-geometry point to render a text label.
    displacement_y = db.StringProperty()
    # Clockwise rotation of the label in degrees from the normal direction for a font.
    rotation = db.StringProperty()
    # Y-coordinate location inside of a label to use for anchoring the label to the main-geometry point.
    anchor_y = db.StringProperty()
    # X displacement from the main-geometry point to render a text label.
    displacement_x = db.StringProperty()
    # X-coordinate location inside of a label to use for anchoring the label to the main-geometry point.
    anchor_x = db.StringProperty()
    # The 'gml_text_symbols' property has been implicitly created by
    # the gml_label_placement' property of GmlTextSymbol.
    pass

class GmlSymbol(IdentifiedObject):
    """ Describes how a feature is to appear on a map or display. The symbol describes not just the shape that should appear but also such graphical properties as color and opacity.
    """

    # The level (of the map) where the symbol exists or the zoom levels at which this diagram object is displayed. As a way of de-cluttering displays, for example, some symbols and annotations are only shown when zoomed in.
    level = db.StringProperty()
    # The version of the Symbol.
    version = db.StringProperty()
    # The Symbol type.
    type = db.StringProperty()
#    gml_feature_styles = db.ListProperty(db.Key)

#    @property
#    def gml_symbols(self):
#        return GmlFeatureStyle.gql("WHERE gml_feature_styles = :1", self.key())
#    gml_base_symbol = db.ReferenceProperty()

class GmlValue(IdentifiedObject):
    """ Used for direct representation of values.
    """

    value = FloatQuantity
    date_time = db.DateProperty()
    time_period = db.StringProperty()
#    measurement_value = db.ReferenceProperty()
#    gml_observation = db.ReferenceProperty()

class GmlBaseSymbol(IdentifiedObject):
    """ Allows referencing and extension of external symbols, which may be stored in a symbol repository. The graphical properties from a referenced external symbol override the ones read in from the base symbol.
    """

    # The 'gml_symbols' property has been implicitly created by
    # the gml_base_symbol' property of GmlSymbol.
    pass

class GmlCoordinateSystem(IdentifiedObject):
    """ A coordinate reference system consists of a set of coordinate system axes that is related to the earth through a datum that defines the size and shape of the earth or some abstract reference system such as those used for rendering schemantic diagrams, internal views of items such as cabinets, vaults, etc. Geometries in GML indicate the coordinate reference system in which their measurements have been made.
    """

    # If applicable, the minimum position allowed along the Z axis of the coordinate reference system.
    z_min = db.StringProperty()
    position_unit_name = db.StringProperty()
    # The maximum position allowed along the Y axis of the coordinate reference system.
    y_max = db.StringProperty()
    scale = db.StringProperty()
    # The minimum position allowed along the Y axis of the coordinate reference system.
    y_min = db.StringProperty()
    # If applicable, the maximum position allowed along the Z axis of the coordinate reference system.
    z_max = db.StringProperty()
    # The minimum position allowed along the X axis of the coordinate reference system.
    x_min = db.StringProperty()
    # The maximum position allowed along the X axis of the coordinate reference system.
    x_max = db.StringProperty()
#    gml_diagram_objects = db.ListProperty(db.Key)

#    @property
#    def gml_coordinate_systems(self):
#        return GmlDiagramObject.gql("WHERE gml_diagram_objects = :1", self.key())
    # The 'diagrams' property has been implicitly created by
    # the gml_coordinate_system' property of Diagram.
    pass
    # The 'gml_positions' property has been implicitly created by
    # the gml_coordinate_system' property of GmlPosition.
    pass

class GmlLabelStyle(IdentifiedObject):
    """ The style for the text that is to be displayed along with the graphical representation of a feature. The content of the label is not necessarily defined in the GML data set. More precisely, the content can be static text specified in the style itself and the text from the GML data set. Label style has two elements: gml:style that specifies the style and gml:label that is used to compose the label content.
    """

    # Used to specify the style of the rendered text. The CSS2 styling expressions grammar should be used to express graphic properties.
    style = db.StringProperty()
    # Allows both text content and unbounded number of gml:LabelExpression elements. The value of gml:LabelExpression element is an XPath expression that selects the value of some property of the feature.
    label_expression = db.StringProperty()
    # Allows us to specify a transformation expression that will be applied to the symbol in the rendering phase. Its type is xsd:string and the value is specified in the SVG specification (transform attribute).
    transform = db.StringProperty()
    # The 'gml_topology_styles' property has been implicitly created by
    # the gml_lable_style' property of GmlTopologyStyle.
    pass
#    gml_feature_style = db.ReferenceProperty()
    # The 'gml_geometry_styles' property has been implicitly created by
    # the gml_label_style' property of GmlGeometryStyle.
    pass

class GmlMark(IdentifiedObject):
    """ Defines a 'shape' which has coloring applied to it (i.e. square, circle, triangle, star, ...).
    """

    # Gives the well-known name of the shape of the mark. Allowed values include at least square, circle, triangle, star, cross, and x.
    well_known_name = db.StringProperty()
#    gml_graphics = db.ListProperty(db.Key)

#    @property
#    def gml_marks(self):
#        return GmlGraphic.gql("WHERE gml_graphics = :1", self.key())
#    gml_strokes = db.ListProperty(db.Key)

#    @property
#    def gml_marks(self):
#        return GmlStroke.gql("WHERE gml_strokes = :1", self.key())
#    gml_fills = db.ListProperty(db.Key)

#    @property
#    def gml_marks(self):
#        return GmlFill.gql("WHERE gml_fills = :1", self.key())

class GmlPosition(PositionPoint):
    """ Position point with a GML coordinate reference system.
    """

#    gml_coordinate_system = db.ReferenceProperty()

class GmlHalo(IdentifiedObject):
    """ A type of Fill that is applied to the backgrounds of font glyphs. The use of halos greatly improves the readability of text labels.
    """

    # The Radius element gives the absolute size of a halo radius in pixels encoded as a floating-point number. The radius is taken from the outside edge of a font glyph to extend the area of coverage of the glyph (and the inside edge of ?holes? in the glyphs). The default radius is one pixel. Negative values are not allowed.
    radius = db.StringProperty()
    # Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
    opacity = db.FloatProperty()
    # The 'gml_text_symbols' property has been implicitly created by
    # the gml_halo' property of GmlTextSymbol.
    pass

class GmlFont(IdentifiedObject):
    """ Identifies a font of a certain family, style, and size.
    """

    # True if 'size' is expressed in absolute values. Default is false.
    absolute_size = db.BooleanProperty()
    # Family name of a font to use. Allowed values are system-dependent. Any number of font-family attributes may be given and they are assumed to be in preferred order.
    family = db.StringProperty()
    # The style to use for a font. The allowed values are 'normal', 'italic', and 'oblique'.
    style = db.StringProperty()
    # The amount of weight or boldness to use for a font. Allowed values are 'normal' and 'bold'.
    weight = db.StringProperty()
    # The size to use for the font in pixels. The default is defined to be 10 pixels, though various systems may have restrictions on what sizes are available.
    size = db.StringProperty()
#    gml_colour = db.ReferenceProperty()
#    gml_svg_parameters = db.ListProperty(db.Key)

#    @property
#    def gml_fonts(self):
#        return GmlSvgParameter.gql("WHERE gml_svg_parameters = :1", self.key())
    # The 'gml_text_symbols' property has been implicitly created by
    # the gml_font' property of GmlTextSymbol.
    pass

class GmlTopologyStyle(IdentifiedObject):
    """ The style for one topology property. Similarly to the Geometry style, a feature can have multiple topology properties, thus multiple topology style descriptors can be specified within one feature style.
    """

#    gml_lable_style = db.ReferenceProperty()
#    gml_feature_style = db.ReferenceProperty()

class GmlGeometryStyle(IdentifiedObject):
    """ The style for one geometry of a feature. Any number of geometry style descriptors can be assigned to one feature style. This is usually required for features with multiple geometry properties.
    """

    # Graphical symbol used to render a geometry or a topology. A symbol is a description of graphical attributes of a graphical object without a particular, implicit meaning. It can be a description of a line, circle, polygon or more complex drawing.
    symbol = db.StringProperty()
    # It is necessary to specify the geometry type using this attribute as well since the application schema of the geometry property may allow different geometries as its value.
    geometry_type = db.StringProperty()
    # The name of the geometry property of a feature to which this GeometryStyle applies.
    geometry_property = db.StringProperty()
#    gml_label_style = db.ReferenceProperty()
#    gml_feature_style = db.ReferenceProperty()

class GmlFeatureType(IdentifiedObject):
    """ Type classification of feature.
    """

#    gml_feature_styles = db.ListProperty(db.Key)

#    @property
#    def gml_feature_types(self):
#        return GmlFeatureStyle.gql("WHERE gml_feature_styles = :1", self.key())

class GmlObservation(Element):
    """ A GML observation models the act of observing, often with a camera, a person or some form of instrument. An observation feature describes the 'metadata' associated with an information capture event, together with a value for the result of the observation. The basic structures introduced in this class are intended to serve as the foundation for more comprehensive schemas for scientific, technical and engineering measurement schemas.
    """

    # Indicates the result of the observation.
    result_of = db.StringProperty()
    date_time = db.DateProperty()
    # Contains or points to a description of a sensor, instrument or procedure used for the observation.
    using = db.StringProperty()
    # Contains or points to the specimen, region or station which is the object of the observation
    target = db.StringProperty()
    # The 'gml_values' property has been implicitly created by
    # the gml_observation' property of GmlValue.
    pass
#    locations = db.ListProperty(db.Key)

#    @property
#    def gml_observatins(self):
#        return Location.gql("WHERE locations = :1", self.key())
    # The 'change_items' property has been implicitly created by
    # the gml_observation' property of ChangeItem.
    pass

class GmlStroke(IdentifiedObject):
    """ The element encapsulating the graphical symbolization parameters for linear geometries.
    """

    # Enumerated values telling how line strings should be joined (between line segments). The values are represented as content strings.  The allowed values for line join are 'mitre', 'round', and 'bevel'. The default values are system-dependent.
    linejoin = db.StringProperty()
    # Specifies the level of translucency to use when rendering the stroke. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
    opacity = db.FloatProperty()
    # The name of a defined line style. Usually will be an enumerated value and will be system-specific.
    line_style = db.StringProperty()
    # Specifies the distance as a float into the 'stroke-dasharray' pattern at which to start drawing.
    dash_offset = db.StringProperty()
    # Encodes a dash pattern as a series of space separated floats. The first number gives the length in pixels of dash to draw, the second gives the amount of space to leave, and this pattern repeats. If an odd number of values is given, then the pattern is expanded by repeating it twice to give an even number of values. Decimal values have a system-dependent interpretation (usually depending on whether antialiasing is being used). The default is to draw an unbroken line.
    dash_array = db.StringProperty()
    # The absolute width (thickness) of a stroke in pixels encoded as a float. The default is 1.0. Fractional numbers are allowed (with a system-dependent interpretation) but negative numbers are not.
    width = db.FloatProperty()
    # Enumerated values telling how line strings should be capped (at the two ends of the line string). The values are represented as content strings.  The allowed values for line cap are 'butt', 'round', and 'square'. The default values are system-dependent.
    line_cap = db.StringProperty()
    # The 'gml_line_symbols' property has been implicitly created by
    # the gml_stroke' property of GmlLineSymbol.
    pass
#    gml_svg_parameters = db.ListProperty(db.Key)

#    @property
#    def gml_stokes(self):
#        return GmlSvgParameter.gql("WHERE gml_svg_parameters = :1", self.key())
#    gml_colour = db.ReferenceProperty()
    # The 'gml_polygon_symbols' property has been implicitly created by
    # the gml_stroke' property of GmlPolygonSymbol.
    pass
#    gml_marks = db.ListProperty(db.Key)

#    @property
#    def gml_strokes(self):
#        return GmlMark.gql("WHERE gml_marks = :1", self.key())

class GmlFeatureStyle(IdentifiedObject):
    """ Used for styling a particular aspect or aspects of a feature, such as geometry, topology or arbitrary text string.
    """

    # This property is used to further constrain the feature instance set to which the style applies. It is optional and its value is an XPath expression. If the property does not exist, the style applies to all feature instances selected by 'featureType' or 'baseType'.
    feature_constraint = db.StringProperty()
    # Identifies the specific feature type that the feature-type style is for.
    feature_type_name = db.StringProperty()
    # The SemanticTypeIdentifier is experimental in GML and is intended to be used to identify what the feature style is suitable to be used for using community-controlled name(s). For example, a single style may be suitable to use with many different feature types.
    semantic_type_identifier = db.StringProperty()
    # The simplest and most common way of relating features and styles is by using this attribute. Its value will be the declared name of a feature, instances of which we want to style. For example, if the featureType = Switch, this FeatureStyle object will simply apply to all Switch features.
    feature_type = db.StringProperty()
    # Grammar used in the content of the gml:featureConstraint element.
    query_grammar = QueryGrammarKind
    # Another way of selecting the feature instances to which the style applies is to specify, as the value of this attribute, the name of the base type from which feature or features derive.
    base_type = db.StringProperty()
    # Allows version numbers to be identified when the SLD pieces are used independently.
    version = db.StringProperty()
#    gml_symbols = db.ListProperty(db.Key)

#    @property
#    def gml_feature_styles(self):
#        return GmlSymbol.gql("WHERE gml_symbols = :1", self.key())
    # The 'gml_label_styles' property has been implicitly created by
    # the gml_feature_style' property of GmlLabelStyle.
    pass
#    gml_feature_types = db.ListProperty(db.Key)

#    @property
#    def gml_feature_styles(self):
#        return GmlFeatureType.gql("WHERE gml_feature_types = :1", self.key())
    # The 'gml_tobology_styles' property has been implicitly created by
    # the gml_feature_style' property of GmlTopologyStyle.
    pass
    # The 'gml_geometry_styles' property has been implicitly created by
    # the gml_feature_style' property of GmlGeometryStyle.
    pass

class GmlTextSymbol(GmlSymbol):
    """ Used for styling text labels, i.e., for rendering them according to various graphical parameters.
    """

    # The minimum font size allowed.
    min_font_size = db.IntegerProperty()
    # The name of the field of the class being annotated. Most objects will include name, description, and aliasName. Many objects may contain other fields such as comment, status, etc.
    field_id = db.StringProperty()
    # Text-label content. If the value is not provided, then no text will be rendered.
    label = db.StringProperty()
    # The type-classification of a label.
    label_type = db.StringProperty()
    # Generic method for capturing all unspecified information pertaining to the TextSymbol.
    property = db.StringProperty()
#    gml_label_placement = db.ReferenceProperty()
#    gml_diagram_object = db.ReferenceProperty()
#    gml_font = db.ReferenceProperty()
#    gml_halo = db.ReferenceProperty()
#    gml_fill = db.ReferenceProperty()

class GmlLineGeometry(GmlDiagramObject):
    """ Typically used for rendering linear assets and/or power system resources.
    """

    # For dynamic network update (i.e. colouring) purposes
    source_side = db.StringProperty()

class GmlLineSymbol(GmlSymbol):
    """ Used to style a 'stroke' along a linear geometry type, such as a string of line segments.
    """

    # For dynamic network update (i.e. colouring) purposes
    source_side = db.StringProperty()
#    gml_stroke = db.ReferenceProperty()
#    gml_diagram_object = db.ReferenceProperty()

class GmlPointGeometry(GmlDiagramObject):
    """ Typically used for rendering power system resources and/or point assets.
    """

    pass

class GmlPointSymbol(GmlSymbol):
    """ Used to draw a 'graphic' at a point.
    """

#    gml_diagram_object = db.ReferenceProperty()
#    gml_graphic = db.ReferenceProperty()

class GmlPolygonGeometry(GmlDiagramObject):
    """ Used to show the footprint of substations, sites, service territories, tax districts, school districts, etc.
    """

    pass

class GmlRasterSymbol(GmlSymbol):
    """ Describes how to render raster/matrix-coverage data (e.g., satellite photos, DEMs).
    """

    # Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
    red_sourcename = db.StringProperty()
    # Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
    blue_sourcename = db.StringProperty()
    # Specifies the level of translucency to use when rendering the Graphic. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0.
    opacity = db.FloatProperty()
    # Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
    green_source_name = db.StringProperty()
    # A single colour channel may be selected to display in grayscale. Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
    gray_sourcename = db.StringProperty()
    # The ReliefFactor gives the amount of exaggeration to use for the height of the 'hills'. A value of around 55 (times) gives reasonable results for Earth-based DEMs. The default value is system-dependent.
    relief_factor = db.StringProperty()
    # Tells a system how to behave when multiple raster images in a layer overlap each other, for example with satellite-image scenes.
    overlapbehaviour = db.StringProperty()
    # If the BrightnessOnly flag is 0 (false, default), the shading is applied to the layer being rendered as the current RasterSymbol. If BrightnessOnly is 1 (true), the shading is applied to the brightness of the colors in the rendering canvas generated so far by other layers, with the effect of relief-shading these other layers.
    brighness_only = db.BooleanProperty()
#    gml_diagram_object = db.ReferenceProperty()

class GmlPolygonSymbol(GmlSymbol):
    """ Used to draw a polygon (or other area-type geometries), including filling its interior and stroking its border (outline).
    """

#    gml_stroke = db.ReferenceProperty()
#    gml_diagram_object = db.ReferenceProperty()
#    gml_fill = db.ReferenceProperty()


