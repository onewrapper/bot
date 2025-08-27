from django.db import migrations, models
import bots.models


class Migration(migrations.Migration):

    dependencies = [
        ("bots", "0048_recording_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recording",
            name="file",
            field=models.FileField(storage=bots.models.RecordingStorage(), max_length=1024, upload_to=""),
        ),
        migrations.AlterField(
            model_name="recording",
            name="thumbnail",
            field=models.FileField(blank=True, null=True, storage=bots.models.RecordingStorage(), max_length=1024, upload_to=""),
        ),
    ] 