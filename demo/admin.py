from django.contrib import admin
from .models import Region, District, Category, SubCategory, Seller, Ad, AdExtraInfo


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region')
    search_fields = ('name',)
    list_filter = ('region',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ads_count', 'icon')
    search_fields = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'profile_photo')
    search_fields = ('full_name',)


@admin.register(AdExtraInfo)
class AdExtraInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_mine', 'status', 'expires_at')
    list_filter = ('status',)
    search_fields = ('status',)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'price', 'currency', 'published_at', 'phone_number', 'seller', 'district')
    search_fields = ('name', 'slug', 'phone_number')
    list_filter = ('published_at', 'district', 'sub_category', 'currency')
    autocomplete_fields = ('sub_category', 'district', 'seller', 'extra_info')
    prepopulated_fields = {'slug': ('name',)}
