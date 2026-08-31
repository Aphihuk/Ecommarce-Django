from django.core.management.base import BaseCommand
from shop.models import Category, Product

class Command(BaseCommand):
    help = 'Seed the FNS Maker Club demo catalog'
    def handle(self, *args, **options):
        data = [('Desk & Setup','desk-setup','⌘'),('Build & Tinker','build-tinker','◒'),('Wearable Tech','wearable-tech','◌'),('Gifts for Makers','gifts-for-makers','✧')]
        cats = {slug: Category.objects.update_or_create(slug=slug, defaults={'name': name,'icon': icon})[0] for name,slug,icon in data}
        products = [('Pocket Pixel Camera','pocket-pixel-camera','capture',2490,'blue','NEW','desk-setup','https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&fit=crop&w=700&q=85'),('The Everyday Dock','the-everyday-dock','desk',1290,'pink','POPULAR','desk-setup','https://images.unsplash.com/photo-1625842268584-8f3296236761?auto=format&fit=crop&w=700&q=85'),('Mini Field Recorder','mini-field-recorder','audio',3850,'green','NEW','build-tinker','https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&w=700&q=85'),('Focus Timer','focus-timer','desk',890,'gray','FNS PICK','gifts-for-makers','https://images.unsplash.com/photo-1495360010541-f48722b34f7d?auto=format&fit=crop&w=700&q=85')]
        for name,slug,kind,price,tone,tag,category,image in products:
            Product.objects.update_or_create(slug=slug, defaults={'name':name,'category':cats[category],'price':price,'tone':tone,'tag':tag,'image_url':image,'stock':10,'is_featured':True})
        self.stdout.write(self.style.SUCCESS('FNS catalog seeded.'))
