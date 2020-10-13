import os

PROJECT_NAME = "ecommerce"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

SHOP_API = "/"
AUTH_API = "/auth"
ADMIN_API = "/admin"
