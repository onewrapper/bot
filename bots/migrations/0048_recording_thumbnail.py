from django.db import migrations, models
import bots.models


class Migration(migrations.Migration):

    dependencies = [
        ("bots", "0047_remove_botevent_valid_event_type_event_sub_type_combinations_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="recording",
            name="thumbnail",
            field=models.FileField(blank=True, null=True, storage=bots.models.RecordingStorage(), upload_to=""),
        ),
    ] 