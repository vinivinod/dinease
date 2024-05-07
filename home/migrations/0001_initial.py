# Generated by Django 4.2.4 on 2023-10-13 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('password', models.CharField(max_length=128)),
                ('role', models.IntegerField(blank=True, choices=[(1, 'CUSTOMER'), (2, 'EMPLOYEE')], default='1', null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillingInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('town', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('payment_status', models.BooleanField(default=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='hmenus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='menus/')),
            ],
        ),
        migrations.CreateModel(
            name='menus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Kerala', 'Kerala'), ('Chineese', 'Chineese'), ('North Indian', 'North Indian'), ('Arabian', 'Arabian'), ('Beverages', 'Beverages')], default='', max_length=50)),
                ('submenu', models.CharField(blank=True, choices=[('Breads', 'Breads'), ('Curries', 'Curries'), ('Rice Dishes', 'Rice Dishes'), ('Appetizers', 'Appetizers'), ('Main Course', 'Main Course'), ('Breads & Accompaniments', 'Breads & Accompaniments'), ('Rolls & Grills', 'Rolls & Grills'), ('Hot Beverage', 'Hot Beverage'), ('Cold Beverage', 'Cold Beverage')], default='', max_length=50)),
                ('sub_submenu', models.CharField(blank=True, choices=[('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian'), ('Water-based', 'Water-based'), ('Milk-based', 'Milk-based')], default='', max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='menus/')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='tables',
            fields=[
                ('tab_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('slot_time', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Time Slot',
                'verbose_name_plural': 'Time Slots',
            },
        ),
        migrations.CreateModel(
            name='TableBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(blank=True, choices=[('Two-Top (1)', 'Two-Top (1)'), ('Two-Top (2)', 'Two-Top (2)'), ('Two-Top (3)', 'Two-Top (3)'), ('Four-Top (1)', 'Four-Top (1)'), ('Four-Top (2)', 'Four-Top (2)'), ('Four-Top (3)', 'Four-Top (3)'), ('Six-Top (1)', 'Six-Top (1)'), ('Six-Top (2)', 'Six-Top (2)'), ('Six-Top (3)', 'Six-Top (3)'), ('Eight-Top (1)', 'Eight-Top (1)'), ('Eight-Top (2)', 'Eight-Top (2)'), ('Eight-Top (3)', 'Eight-Top (3)'), ('Large Party (1)', 'Large Party (1)'), ('Large Party (2)', 'Large Party (2)'), ('Large Party (3)', 'Large Party (3)')], max_length=30, null=True)),
                ('date', models.DateField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('del_status', models.BooleanField(default=False)),
                ('email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings_by_email', to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings_by_name', to=settings.AUTH_USER_MODEL)),
                ('phone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings_by_phone', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.CharField(default=None, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('num_of_persons', models.PositiveIntegerField()),
                ('time_slot', models.CharField(blank=True, max_length=20, null=True)),
                ('reservation_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[(None, 'None'), ('approved', 'Approved'), ('declined', 'Declined')], default=None, max_length=10, null=True)),
                ('menu_name', models.CharField(blank=True, max_length=100, null=True)),
                ('menu_price', models.FloatField(blank=True, null=True)),
                ('table_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.tables')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_order_id', models.CharField(max_length=255)),
                ('payment_id', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('currency', models.CharField(max_length=3)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('successful', 'Successful'), ('failed', 'Failed')], default='pending', max_length=20)),
                ('billing_info', models.ManyToManyField(to='home.billinginformation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.CharField(choices=[('full-day', 'Full Day'), ('half-day-morning', 'Half Day (Morning)'), ('half-day-afternoon', 'Half Day (Afternoon)')], max_length=20)),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(default='default', editable=False, max_length=100, null=True)),
                ('years_of_experience', models.PositiveIntegerField(default='default', null=True)),
                ('address', models.TextField(default='', null=True)),
                ('id_proof_number', models.CharField(default='', max_length=100, null=True)),
                ('education', models.CharField(default='', max_length=100, null=True)),
                ('qualification', models.CharField(default='', max_length=100, null=True)),
                ('emergency_name', models.CharField(default='', max_length=100, null=True)),
                ('emergency_contact_number', models.CharField(blank=True, default='', max_length=12, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='employee_profile/')),
                ('active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='billinginformation',
            name='menu',
            field=models.ManyToManyField(blank=True, to='home.menus'),
        ),
        migrations.AddField(
            model_name='billinginformation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AddToCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.PositiveSmallIntegerField(default=1)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.menus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
