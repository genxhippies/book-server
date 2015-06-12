# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfred', '0003_auto_20150605_0549'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mybook',
            unique_together=set([('user', 'book')]),
        ),
        migrations.AlterUniqueTogether(
            name='wishlist',
            unique_together=set([('user', 'book')]),
        ),
    ]
