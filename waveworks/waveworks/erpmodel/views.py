# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Brand(models.Model):
    name = models.CharField(primary_key=True, max_length=45)
    description = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'brand'


class MarketSegment(models.Model):
    name = models.CharField(primary_key=True, max_length=45)
    description = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'market_segment'


class Model(models.Model):
    name = models.CharField(primary_key=True, max_length=45)
    description = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'model'


class Product(models.Model):
    market_segment_name = models.ForeignKey(MarketSegment, db_column='market_segment_name')
    product_family_name = models.ForeignKey('ProductFamily', db_column='product_family_name')
    brand_name = models.ForeignKey(Brand, db_column='brand_name')
    model_name = models.ForeignKey(Model, db_column='model_name')
    name = models.CharField(primary_key=True, max_length=45)
    sku = models.CharField(unique=True, max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductFamily(models.Model):
    name = models.CharField(primary_key=True, max_length=45)
    description = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'product_family'


class ProductFamilyAttributes(models.Model):
    attribute = models.CharField(primary_key=True, max_length=45)
    product_family_name = models.ForeignKey(ProductFamily, db_column='product_family_name')

    class Meta:
        managed = False
        db_table = 'product_family_attributes'


class ProductInfo(models.Model):
    product_model_name = models.CharField(max_length=45)
    product_family_attributes_attribute = models.ForeignKey(ProductFamilyAttributes, db_column='product_family_attributes_attribute')
    product_family_attribute_value = models.CharField(max_length=45, blank=True)
    product_name = models.ForeignKey(Product, db_column='product_name')

    class Meta:
        managed = False
        db_table = 'product_info'
