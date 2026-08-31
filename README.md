# FNS Maker Club — Django Demo

## Run locally

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_shop
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. Add products from the storefront, review the session-backed cart at `/cart/`, and complete the mock checkout at `/checkout/`.

Create an admin account with `python manage.py createsuperuser`, then open `/admin/` to manage categories, products, and orders.
