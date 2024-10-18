from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, related_name='districts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    ads_count = models.IntegerField(null=True, blank=True)
    # icon = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ImageField(upload_to='category_icons/', null=True, blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Seller(models.Model):
    full_name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='seller_photo/', null=True, blank=True)

    def __str__(self):
        return self.full_name


class AdExtraInfo(models.Model):
    STATUS_CHOICES = [
        ('in_moderation', 'In Moderation'),
        ('rejected', 'Rejected'),
        ('active', 'Active'),
        ('expired', 'Expired'),
    ]

    is_mine = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    expires_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.status


class Ad(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, related_name='ads', on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='ad_photos/', null=True, blank=True)
    price = models.IntegerField()
    currency = models.CharField(max_length=10)
    published_at = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    district = models.ForeignKey(District, related_name='ads', on_delete=models.CASCADE)
    address_name = models.CharField(max_length=255, null=True, blank=True)
    address_lat = models.FloatField(null=True, blank=True)
    address_long = models.FloatField(null=True, blank=True)
    seller = models.ForeignKey(Seller, related_name='ads', on_delete=models.CASCADE)
    extra_info = models.OneToOneField(AdExtraInfo, related_name='ad', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
