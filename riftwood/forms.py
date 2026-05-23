from django import forms

class GuitarOrderForm(forms.Form):
    ORIENTATION_CHOICES = [('Right-handed', 'Right-handed'), ('Left-handed', 'Left-handed')]
    BODY_SHAPE_CHOICES = [
        ('S-Shape', 'S-Shape'), ('SS-Shape', 'SS-Shape'), ('T-Shape', 'T-Shape'),
        ('LP-Shape', 'LP-Shape'), ('DC-Shape', 'DC-Shape'), ('J-Shape', 'J-Shape'), ('FB-Shape', 'FB-Shape')
    ]
    BODY_WOOD_CHOICES = [
        ('Maple', 'Maple'), ('Alder', 'Alder'), ('Ash', 'Ash'),
        ('Mahogany', 'Mahogany'), ('Basswood', 'Basswood'), ('Korina', 'Korina')
    ]
    FINISH_CHOICES = [
        ('Black', 'Black'), ('White', 'White'), ('Aged White', 'Aged White'), ('Surf Green', 'Surf Green'),
        ('Daphne Blue', 'Daphne Blue'), ('Cherry Red', 'Cherry Red'), ('Coral Red', 'Coral Red'),
        ('Pink', 'Pink'), ('Gold', 'Gold'), ('Cherry Sunburst', 'Cherry Sunburst'),
        ('Tobacco Burst', 'Tobacco Burst'), ('Blue Burst', 'Blue Burst'), ('Natural', 'Natural')
    ]
    NECK_SHAPE_CHOICES = [
        ('C-Shape', 'C-Shape'), ('D-Shape', 'D-Shape'), ('U-Shape', 'U-Shape'), ('V-Shape', 'V-Shape')
    ]
    NECK_WOOD_CHOICES = [
        ('Maple', 'Maple'), ('Alder', 'Alder'), ('Ash', 'Ash'), ('Mahogany', 'Mahogany'), ('Spruce', 'Spruce')
    ]
    FINGERBOARD_WOOD_CHOICES = [
        ('Maple', 'Maple'), ('Rosewood', 'Rosewood'), ('Ebony', 'Ebony')
    ]
    SCALE_LENGTH_CHOICES = [('25.5”', '25.5”'), ('24.75”', '24.75”')]
    FRET_NUMBER_CHOICES = [('22', '22'), ('23', '23'), ('24', '24')]
    PICKUP_CHOICES = [
        ('S-Style Single Coil', 'S-Style Single Coil'), ('T-Style Single Coil', 'T-Style Single Coil'),
        ('J-Style Single Coil', 'J-Style Single Coil'), ('Lipstick Tube Single Coil', 'Lipstick Tube Single Coil'),
        ('P-90 Soap Bar', 'P-90 Soap Bar'), ('Filtertron Humbucker', 'Filtertron Humbucker'),
        ('Vintage PAF Humbucker', 'Vintage PAF Humbucker'), ('Mini-Humbucker', 'Mini-Humbucker'),
        ('Wide Range Humbucker', 'Wide Range Humbucker'), ('High Output Humbucker', 'High Output Humbucker')
    ]
    PICKUP_CHOICES_OPTIONAL = [('None', 'None')] + PICKUP_CHOICES
    PICKGUARD_CHOICES = [
        ('None', 'None'), ('White', 'White'), ('Aged White', 'Aged White'),
        ('Black', 'Black'), ('Gold', 'Gold'), ('Tortoiseshell', 'Tortoiseshell')
    ]
    BRIDGE_CHOICES = [
        ('Hard-Tail', 'Hard-Tail'), ('T-Style Bridge', 'T-Style Bridge'), ('Direct String-Through', 'Direct String-Through'),
        ('Stop-Tail', 'Stop-Tail'), ('Vibrola', 'Vibrola'), ('Bigsby', 'Bigsby'),
        ('Synchronized Tremolo', 'Synchronized Tremolo'), ('Double Locking Tremolo', 'Double Locking Tremolo')
    ]
    HARDWARE_COLOR_CHOICES = [('Chrome', 'Chrome'), ('Gold', 'Gold'), ('Black', 'Black')]
    ADDONS_CHOICES = [
        ('F-Hole', 'F-Hole'), ('Scalloped Fretboard', 'Scalloped Fretboard'), ('Neck Heel Contour', 'Neck Heel Contour'),
        ('Locking Tuners', 'Locking Tuners'), ('Killswitch', 'Killswitch'), ('Treble Bleed', 'Treble Bleed'),
        ('Volume/Tone Bypass', 'Volume/Tone Bypass'), ('Piezo Pickup', 'Piezo Pickup'),
        ('Coil Splitting', 'Coil Splitting'), ('Series/Parallel Switching', 'Series/Parallel Switching'),
        ('Phase Switching', 'Phase Switching')
    ]

    orientation = forms.ChoiceField(choices=ORIENTATION_CHOICES, widget=forms.RadioSelect)
    body_shape = forms.ChoiceField(choices=BODY_SHAPE_CHOICES)
    body_wood = forms.ChoiceField(choices=BODY_WOOD_CHOICES)
    finish = forms.ChoiceField(choices=FINISH_CHOICES)
    neck_shape = forms.ChoiceField(choices=NECK_SHAPE_CHOICES)
    neck_wood = forms.ChoiceField(choices=NECK_WOOD_CHOICES)
    fingerboard_wood = forms.ChoiceField(choices=FINGERBOARD_WOOD_CHOICES)
    scale_length = forms.ChoiceField(choices=SCALE_LENGTH_CHOICES)
    fret_number = forms.ChoiceField(choices=FRET_NUMBER_CHOICES)
    bridge_pickup = forms.ChoiceField(choices=PICKUP_CHOICES)
    middle_pickup = forms.ChoiceField(choices=PICKUP_CHOICES_OPTIONAL, required=False)
    neck_pickup = forms.ChoiceField(choices=PICKUP_CHOICES_OPTIONAL, required=False)
    pickguard = forms.ChoiceField(choices=PICKGUARD_CHOICES, required=False)
    bridge = forms.ChoiceField(choices=BRIDGE_CHOICES)
    hardware_color = forms.ChoiceField(choices=HARDWARE_COLOR_CHOICES)
    addons = forms.MultipleChoiceField(choices=ADDONS_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)
    additional_requests = forms.CharField(widget=forms.Textarea, required=False)

class DrumOrderForm(forms.Form):
    SHELL_MATERIAL_CHOICES = [
        ('Maple', 'Maple'), ('Birch', 'Birch'), ('Bubinga', 'Bubinga'), ('Gum', 'Gum'),
        ('Mahogany', 'Mahogany'), ('Walnut', 'Walnut'), ('Maple / Mahogany', 'Maple / Mahogany'),
        ('Walnut / Birch', 'Walnut / Birch'), ('Maple / Gum', 'Maple / Gum')
    ]
    SHELL_THICKNESS_CHOICES = [('Thin', 'Thin'), ('Medium', 'Medium'), ('Thick', 'Thick')]
    FINISH_CHOICES = [
        ('Natural', 'Natural'), ('Black Satin', 'Black Satin'), ('White Satin', 'White Satin'),
        ('Black Oyster', 'Black Oyster'), ('Blue Oyster', 'Blue Oyster'), ('Green Sparkle', 'Green Sparkle'),
        ('Orange Sparkle', 'Orange Sparkle'), ('Blue Fade', 'Blue Fade'), ('Aqua Gloss', 'Aqua Gloss'),
        ('Pink Wrap', 'Pink Wrap'), ('Red Wrap', 'Red Wrap')
    ]
    HARDWARE_COLOR_CHOICES = [('Chrome', 'Chrome'), ('Gold', 'Gold'), ('Black', 'Black')]
    HOOP_TYPE_CHOICES = [
        ('Wooden', 'Wooden'), ('Single-Flanged', 'Single-Flanged'),
        ('Die-Cast', 'Die-Cast'), ('Triple-Flanged', 'Triple-Flanged')
    ]

    shell_material = forms.ChoiceField(choices=SHELL_MATERIAL_CHOICES)
    shell_thickness = forms.ChoiceField(choices=SHELL_THICKNESS_CHOICES)
    finish = forms.ChoiceField(choices=FINISH_CHOICES)
    kick_diameter = forms.IntegerField(label="Kick Diameter (16-28\")", min_value=16, max_value=28)
    kick_depth = forms.IntegerField(label="Kick Depth (14-22\")", min_value=14, max_value=22)
    rack_tom_diameter = forms.IntegerField(label="Rack Tom Diameter (8-16\")", min_value=8, max_value=16)
    rack_tom_depth = forms.IntegerField(label="Rack Tom Depth (7-11\")", min_value=7, max_value=11)
    floor_tom_diameter = forms.IntegerField(label="Floor Tom Diameter (14-18\")", min_value=14, max_value=18)
    floor_tom_depth = forms.IntegerField(label="Floor Tom Depth (12-18\")", min_value=12, max_value=18)
    add_snare = forms.BooleanField(label="Add Matching Snare", required=False)
    snare_diameter = forms.IntegerField(label="Snare Diameter (11-14\")", min_value=11, max_value=14, required=False)
    snare_depth = forms.IntegerField(label="Snare Depth (3-10\")", min_value=3, max_value=10, required=False)
    add_gong = forms.BooleanField(label="Add Gong Drum", required=False)
    gong_diameter = forms.IntegerField(label="Gong Diameter (18-22\")", min_value=18, max_value=22, required=False)
    gong_depth = forms.IntegerField(label="Gong Depth (14-18\")", min_value=14, max_value=18, required=False)
    add_concert_tom = forms.BooleanField(label="Add Concert Tom", required=False)
    concert_tom_diameter = forms.IntegerField(label="Concert Tom Diameter (8-16\")", min_value=8, max_value=16, required=False)
    concert_tom_depth = forms.IntegerField(label="Concert Tom Depth (7-11\")", min_value=7, max_value=11, required=False)
    add_pancake = forms.BooleanField(label="Add Pancake Drum", required=False)
    pancake_depth = forms.DecimalField(label="Pancake Depth (2.5-5\")", min_value=2.5, max_value=5, required=False)
    add_rocket_tom = forms.BooleanField(label="Add Rocket Tom Set (6x10,6x12,6x15,6x18)", required=False)
    add_woofer = forms.BooleanField(label="Add Woofer", required=False)
    hoop_type = forms.ChoiceField(choices=HOOP_TYPE_CHOICES)
    hardware_color = forms.ChoiceField(choices=HARDWARE_COLOR_CHOICES)
    additional_requests = forms.CharField(widget=forms.Textarea, required=False)