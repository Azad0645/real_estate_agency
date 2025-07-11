# Generated by Django 2.2.24 on 2025-07-01 19:39

from django.db import migrations
import phonenumbers


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.iterator():
        raw_phone = flat.owners_phonenumber

        if raw_phone:
            try:
                parsed = phonenumbers.parse(raw_phone, 'RU')
            except phonenumbers.NumberParseException:
                parsed = None

            if parsed and phonenumbers.is_valid_number(parsed):
                flat.owner_pure_phone = phonenumbers.format_number(
                    parsed,
                    phonenumbers.PhoneNumberFormat.E164
                )
                flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20250701_2237'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone),
    ]
