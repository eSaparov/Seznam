# Generated by Django 4.2.4 on 2023-08-10 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='appMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(blank=True, max_length=256, null=True)),
                ('downloaded', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='storedContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offlineUri', models.URLField(blank=True, null=True)),
                ('originalManifestUri', models.URLField(blank=True, null=True)),
                ('duration', models.FloatField(blank=True, null=True)),
                ('size', models.PositiveIntegerField(blank=True, null=True)),
                ('expiration', models.CharField(blank=True, max_length=50, null=True)),
                ('isIncomplete', models.BooleanField(blank=True, null=True)),
                ('appMetadata', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.appmetadata')),
            ],
        ),
        migrations.CreateModel(
            name='tracks',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('bandwidth', models.PositiveIntegerField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=2, null=True)),
                ('label', models.CharField(blank=True, max_length=50, null=True)),
                ('kind', models.CharField(blank=True, max_length=50, null=True)),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('frameRate', models.PositiveIntegerField(blank=True, null=True)),
                ('pixelAspectRatio', models.FloatField(blank=True, null=True)),
                ('hdr', models.FloatField(blank=True, null=True)),
                ('mimeType', models.CharField(blank=True, max_length=50, null=True)),
                ('audioMimeType', models.CharField(blank=True, max_length=50, null=True)),
                ('videoMimeType', models.CharField(blank=True, max_length=50, null=True)),
                ('codecs', models.CharField(blank=True, max_length=50, null=True)),
                ('audioCodec', models.CharField(blank=True, max_length=50, null=True)),
                ('videoCodec', models.CharField(blank=True, max_length=50, null=True)),
                ('primary', models.BooleanField(blank=True, null=True)),
                ('roles', models.JSONField(blank=True, null=True)),
                ('audioRoles', models.JSONField(blank=True, null=True)),
                ('forced', models.BooleanField(blank=True, null=True)),
                ('videoId', models.PositiveIntegerField(blank=True, null=True)),
                ('audioId', models.PositiveIntegerField(blank=True, null=True)),
                ('channelsCount', models.PositiveIntegerField(blank=True, null=True)),
                ('audioSamplingRate', models.PositiveIntegerField(blank=True, null=True)),
                ('spatialAudio', models.BooleanField(blank=True, null=True)),
                ('tilesLayout', models.CharField(blank=True, max_length=50, null=True)),
                ('audioBandwidth', models.CharField(blank=True, max_length=50, null=True)),
                ('videoBandwidth', models.CharField(blank=True, max_length=50, null=True)),
                ('originalVideoId', models.CharField(blank=True, max_length=50, null=True)),
                ('originalAudioId', models.CharField(blank=True, max_length=50, null=True)),
                ('originalTextId', models.CharField(blank=True, max_length=50, null=True)),
                ('originalImageId', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'track',
                'verbose_name_plural': 'tracks',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('shortName', models.CharField(blank=True, max_length=50, null=True)),
                ('iconUri', models.URLField(blank=True, null=True)),
                ('manifestUri', models.URLField(blank=True, null=True)),
                ('iconFile', models.ImageField(upload_to='../static/images')),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('focus', models.BooleanField(blank=True, null=True)),
                ('disabled', models.BooleanField(blank=True, null=True)),
                ('extraText', models.JSONField(blank=True, null=True)),
                ('certificateUri', models.URLField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('isFeatured', models.BooleanField(blank=True, null=True)),
                ('drm', models.JSONField(blank=True, null=True)),
                ('features', models.JSONField(blank=True, null=True)),
                ('licenseServers', models.JSONField(blank=True, null=True)),
                ('licenseRequestHeaders', models.JSONField(blank=True, null=True)),
                ('requestFilter', models.CharField(blank=True, max_length=100, null=True)),
                ('responseFilter', models.CharField(blank=True, max_length=100, null=True)),
                ('clearKeys', models.JSONField(blank=True, null=True)),
                ('extraConfig', models.CharField(blank=True, max_length=100, null=True)),
                ('adTagUri', models.URLField(blank=True, null=True)),
                ('imaVideoId', models.CharField(blank=True, max_length=100, null=True)),
                ('imaAssetKey', models.CharField(blank=True, max_length=100, null=True)),
                ('imaContentSrcId', models.CharField(blank=True, max_length=100, null=True)),
                ('mimeType', models.CharField(blank=True, max_length=100, null=True)),
                ('mediaPlaylistFullMimeType', models.CharField(blank=True, max_length=100, null=True)),
                ('storedProgress', models.PositiveIntegerField(blank=True, null=True)),
                ('storedContent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.storedcontent')),
            ],
        ),
        migrations.AddField(
            model_name='storedcontent',
            name='tracks',
            field=models.ManyToManyField(to='movies.tracks'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('telnumber', models.CharField(max_length=13, unique=True, verbose_name='Telefonni cislo')),
                ('name', models.CharField(max_length=25, verbose_name='Jmeno')),
                ('surname', models.CharField(max_length=25, verbose_name='Primeni')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktivni uzivatel')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Operator')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Uzivatel',
                'verbose_name_plural': 'Uzivatele',
                'ordering': ['-id'],
            },
        ),
    ]
