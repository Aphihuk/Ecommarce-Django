from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name='Category', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('name', models.CharField(max_length=80)),('slug', models.SlugField(unique=True)),('icon', models.CharField(default='✦', max_length=10))]),
        migrations.CreateModel(name='Product', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('name', models.CharField(max_length=120)),('slug', models.SlugField(unique=True)),('description', models.TextField(blank=True)),('price', models.DecimalField(decimal_places=2, max_digits=10)),('image_url', models.URLField(blank=True)),('tone', models.CharField(default='blue', max_length=20)),('tag', models.CharField(default='FNS PICK', max_length=20)),('stock', models.PositiveIntegerField(default=10)),('is_featured', models.BooleanField(default=True)),('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category'))]),
        migrations.CreateModel(name='Order', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('order_number', models.CharField(max_length=20, unique=True)),('email', models.EmailField(max_length=254)),('shipping_address', models.TextField()),('total_price', models.DecimalField(decimal_places=2, max_digits=10)),('status', models.CharField(choices=[('pending','Pending'),('paid','Paid')], default='paid', max_length=20)),('created_at', models.DateTimeField(auto_now_add=True))]),
        migrations.CreateModel(name='OrderItem', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('quantity', models.PositiveIntegerField(default=1)),('price_at_order', models.DecimalField(decimal_places=2, max_digits=10)),('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.order')),('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product'))]),
    ]
