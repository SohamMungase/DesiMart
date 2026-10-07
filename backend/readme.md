# 🛒 DesiMart — Online Grocery Ordering System

DesiMart is a **full-stack online grocery ordering system** that allows customers to browse grocery products, manage their cart, place orders, and track their orders.

The project is developed as an **MVP (Minimum Viable Product)** with a focus on simple, scalable, and user-friendly e-commerce functionality.

---

## 🚀 Features

### 👤 Customer

- Create an account using email and password
- Login using authentication
- View user profile
- Browse available grocery products
- View product details
- Add products to cart
- Increase/decrease cart quantity
- Remove products from cart
- View cart subtotal and total amount
- Place orders
- View order history
- View detailed order information
- Track order status

### 👨‍💼 Admin

- Manage grocery products
- Add new products
- Update product details
- Remove products
- Activate/deactivate products
- View all customer orders
- Update order status

### 📦 Order Status

```text
Pending → Confirmed → Delivered
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Backend framework |
| Django REST Framework | REST APIs |
| React.js | Frontend |
| PostgreSQL | Database |
| JWT | Authentication |
| Docker | Containerization |
| Docker Compose | Multi-container development |
| Git & GitHub | Version control |
| GitHub Actions | CI/CD |

The project requirements specifically define Django REST Framework for APIs, React.js for the frontend, PostgreSQL for the database, and Docker/Docker Compose for containerization.

---

## 🏗️ Project Architecture

```text
DesiMart
│
├── Backend
│   ├── accounts
│   ├── products
│   ├── carts
│   ├── orders
│   ├── api
│   ├── manage.py
│   └── requirements.txt
│
├── Frontend
│   └── React.js
│
├── Docker
│   ├── Dockerfile
│   └── docker-compose.yml
│
└── README.md
```

---

## 🔐 Authentication

DesiMart uses authentication to protect customer-specific resources.

### Authentication Flow

```text
Register
   ↓
Login
   ↓
JWT Access Token
   ↓
Authenticated API Requests
   ↓
Profile / Cart / Orders
```

Only authenticated users can access cart and order functionality, as specified in the project requirements.

---

## 📦 Main API Modules

### Authentication

```text
POST   /api/v1/register/
POST   /api/v1/token/
POST   /api/v1/token/refresh/
GET    /api/v1/profile/
```

### Products

```text
GET    /api/v1/products/
GET    /api/v1/products/<id>/
GET    /api/v1/categories/
```

### Cart

```text
GET    /api/v1/carts/
POST   /api/v1/carts/add/
PATCH  /api/v1/carts/items/<item_id>/
DELETE /api/v1/carts/items/<item_id>/
```

### Orders

```text
POST   /api/v1/orders/place/
GET    /api/v1/orders/
GET    /api/v1/orders/<id>/
```

> API endpoints may change as development continues.

---

## 🛍️ Product Management

Products contain information such as:

```text
Product
├── Name
├── Description
├── Category
├── Image
├── Price
├── Stock
├── Tax Percentage
├── Active Status
└── Created At
```

Customers can view available products, while admins can create, update, remove, and control product visibility.

---

## 🛒 Cart Management

Each customer has **one active cart**.

Cart functionality includes:

- Add product
- Increase quantity
- Decrease quantity
- Remove product
- Check product stock
- Calculate subtotal
- Calculate tax
- Calculate grand total

```text
Customer
   │
   ▼
Cart
   │
   ├── Cart Item
   │      ├── Product
   │      └── Quantity
   │
   └── Total Amount
```

The requirement specifies one active cart per customer and requires quantity management, removal, full-cart viewing, and total calculation.

---

## 📋 Order Management

When a customer places an order, the system creates an order based on the items in their cart.

### Order Flow

```text
Cart
 ↓
Checkout
 ↓
Place Order
 ↓
Order Created
 ↓
Pending
 ↓
Confirmed
 ↓
Delivered
```

Customers can view previous orders and order details, while admins can view all orders and update their status.

---

## 🗄️ Database

DesiBasket uses **PostgreSQL** as its relational database.

Main entities:

```text
User
 │
 ├── Cart
 │     └── CartItem ─── Product
 │
 └── Order
       └── Order Items
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/SohamMungase/cjcmart.git
```

```bash
cd DesiMart
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

Activate on Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=cjcmart
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Admin User

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Backend will be available at:

```text
http://127.0.0.1:8000/
```

---

## 🐳 Docker Setup

Build and start the application using Docker Compose:

```bash
docker compose up --build
```

Stop containers:

```bash
docker compose down
```

Run migrations inside the container:

```bash
docker compose exec web python manage.py migrate
```

---

## 🔄 Development Workflow

```text
Developer
   ↓
Git
   ↓
GitHub
   ↓
GitHub Actions
   ↓
Build / Test
   ↓
Deployment
```

The requirements call for a deployment setup that supports scalable deployment and continuous delivery of updates to the live environment.

---

## 📌 MVP Scope

DesiMart is intentionally designed as an MVP.

The primary goal is to provide:

```text
Browse Products
       ↓
Add to Cart
       ↓
Place Order
       ↓
Track Order
```

Advanced e-commerce functionality is outside the initial MVP scope.

---

## 🔒 Security

- JWT-based authentication
- Protected customer APIs
- Admin-only product management
- Admin-only order management
- Environment variables for sensitive configuration
- PostgreSQL database
- CORS configuration for frontend integration

---

## 📈 Future Improvements

Potential future enhancements include:

- Online payment gateway
- Product search and filtering
- Product reviews and ratings
- Wishlist
- Coupons and discount codes
- Email notifications
- SMS notifications
- Advanced order tracking
- Delivery partner management
- Product recommendations
- Redis caching
- Automated testing
- Production monitoring

---

## 📊 Project Requirements

| Requirement | Status |
|---|---|
| Customer Registration | ✅ |
| Customer Login | ✅ |
| User Profile | ✅ |
| Product Listing | ✅ |
| Product Details | ✅ |
| Product Management | ✅ |
| Cart Management | ✅ |
| Stock Validation | ✅ |
| Order Placement | 🚧 |
| Order History | 🚧 |
| Order Tracking | 🚧 |
| Admin Order Management | 🚧 |
| PostgreSQL | ✅ |
| Docker | 🚧 |
| GitHub Actions CI/CD | 🚧 |
| React Frontend | 🚧 |

---

## 👨‍💻 Developer

**Soham Mungase**

Backend Developer | Python | Django | Django REST Framework

- GitHub: https://github.com/SohamMungase
- LinkedIn: https://www.linkedin.com/in/sohammungase/

---

## ⭐ Project Goal

The goal of DesiMart is to build a **clean, scalable and production-ready grocery ordering platform** using modern backend technologies and RESTful API architecture.

> **Build. Learn. Improve. Ship. 🚀**