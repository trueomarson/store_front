# Generated by Django 3.2.6 on 2021-08-23 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_product'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection (title)
            VALUES ('collection1')
    """, """
        DELETE FROM store_collection
        WHERE title='collection1'
    """)
    ]
