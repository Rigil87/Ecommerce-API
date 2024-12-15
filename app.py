from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import ForeignKey, Table, String, Column, DateTime, Float
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional

# Initialize Flask app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Wins5323@localhost/ecommerce_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Creating our Base Model

class Base(DeclarativeBase):
    pass
# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)

#The association table between Users and Orders
user_orders = Table(
	"user_orders",
	Base.metadata,
	Column("user_id", ForeignKey("users.user_id")),
	Column("order_id", ForeignKey("orders.order_id")),
)
#The association table between Orders and Products
order_products = Table(
    "order_products",
    Base.metadata,
    Column("order_id", ForeignKey("orders.order_id")),
    Column("product_id", ForeignKey("products.product_id")),   
)
# User model
class User(Base):
    __tablename__ = "users"
    
    user_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    street_address: Mapped[str] = mapped_column(String(200))
    apt: Mapped[Optional[str]] = mapped_column(String(10))
    city: Mapped[str] = mapped_column(String(50))
    state: Mapped[str] = mapped_column(String(2))
    zip_code: Mapped[str] = mapped_column(String(5))
    email: Mapped[str] = mapped_column(String(200), unique=True)
    home_phone: Mapped[str] = mapped_column(String(10))
    cell_phone: Mapped[str] = mapped_column(String(10))
    
# Defines the many to many relationship with the Order class	
    orders: Mapped[List["Order"]] = relationship(secondary=user_orders, back_populates="users")

#Order model    
class Order(Base):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    
# Defines the many to many relationship with the User and Product classes    
    users: Mapped[List["User"]] = relationship(secondary=user_orders, back_populates="orders")
    products: Mapped[List["Product"]] = relationship(secondary=order_products, back_populates="orders")

#Product model
class Product(Base):
    __tablename__ = "products"
    
    product_id: Mapped[int] = mapped_column(primary_key=True)
    product_category: Mapped[str] = mapped_column(String(50))
    product_name: Mapped[str] = mapped_column(String(200))
    product_mfg: Mapped[str] = mapped_column(String(200))
    product_model: Mapped[str] = mapped_column(String(200))
    product_price: Mapped[float] = mapped_column(Float)
    product_color: Mapped[str] = mapped_column(String(20))
    product_weight: Mapped[float] = mapped_column(Float)
    product_length: Mapped[float] = mapped_column(Float)
    product_width: Mapped[float] = mapped_column(Float)
    product_height: Mapped[float] = mapped_column(Float)
#Defines the many to many relationship with the Order class   
    orders: Mapped[List["Order"]] = relationship(secondary=order_products, back_populates="products")

#Defines the schema for serializing User object    
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
#Defines the schema for serializing Order object          
class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
#Defines the schema for serializing Product object          
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        
#Intiliizes schema for multiple and single objects
user_schema = UserSchema()
users_schema = UserSchema(many=True) 
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
product_schema = ProductSchema()
products_schemas = ProductSchema(many=True)

