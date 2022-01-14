from django.db import models

# provides drop down of skate brands for which a review may be submitted
BRANDS = (
    ('Bont', 'Bont'),
    ('Flyke', 'Flyke'),
    ('Luigino Verducci', 'Luigino Verducci'),
    ('Powerslide', 'Powerslide'),
    ('Riedell', 'Riedell'),
    ('Rollerblade', 'Rollerblade'),
    ('Vanilla', 'Vanilla'),
)

# provides drop down of skate boot material combinations
BOOT_MATERIALS = (
    ('Leather/Fiberglass', 'Leather/Fiberglass'),
    ('Leather/Carbon Fiber', 'Leather/Carbon Fiber'),
    ('Leather/Resin', 'Leather/Resin'),
)

# provides drop down of skate boot style (high/low)
BOOT_STYLE = (
    ('Low Ankle', 'Low Ankle'),
    ('High Ankle', 'High Ankle'),
)

# provides drop down of skate chasis types
FRAME = (
    ('Aluminum', 'Aluminum'),
    ('Carbon Fiber', 'Carbon Fiber'),
    ('Composite', 'Composite'),
    ('Steel', 'Steel'),
)

# provides drop down of a mix of industry bearing numerical ratings vs. other rating systems
# due to the complexity of this rating metric, provided selections are not all-inclusive
BEARINGS_RATING = (
    ('ABEC (Below 7)', 'ABEC (Below 7)'),
    ('ABEC-7', 'ABEC-7'),
    ('ABEC-8', 'ABEC-8'),
    ('ABEC-9', 'ABEC-9'),
    ('Bones', 'Bones'),
    ('Swiss', 'Swiss'),
)

# provides drop down of bearing material types
BEARINGS_MATERIAL = (
    ('Ceramic', 'Ceramic'),
    ('Steel', 'Steel'),
    ('Other', 'Other'),
)

# provides drop down of general comfort ratings
# also providing pros and cons fields for more feedback detail
COMFORT = (
    ('Poor', 'Poor'),
    ('Average', 'Average'),
    ('Good', 'Good'),
    ('Above Average', 'Above Average'),
)

# provides numerical overall rating
OVERALL_RATING = (
    ('Poor', 'Poor'),
    ('Average', 'Average'),
    ('Good', 'Good'),
    ('Above Average', 'Above Average'),
)

# this is a model for submission of an individual skate model reviews
class Review(models.Model):
    email = models.EmailField(('email address'), default="", blank=False, max_length=255)
    skate_brand = models.CharField(max_length=20, default="", blank=True, choices=BRANDS)
    boot_materials = models.CharField(max_length=20, default="", blank=True, choices=BOOT_MATERIALS)
    boot_style = models.CharField(max_length=20, default="", blank=True, choices=BOOT_STYLE)
    frame = models.CharField(max_length=15, default="", blank=True, choices=FRAME)
    bearings_rating = models.CharField(max_length=10, default="", blank=True, choices=BEARINGS_RATING)
    bearings_material = models.CharField(max_length=7, default="", blank=True, choices=BEARINGS_MATERIAL)
    comfort = models.CharField(max_length=13, default="", blank=True, choices=COMFORT)
    overall_rating = models.CharField(max_length=13, default="", blank=True, choices=OVERALL_RATING)
    pros = models.TextField(max_length=300, default="", blank=True)
    cons = models.TextField(max_length=300, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.emails


