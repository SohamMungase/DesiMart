# 🛒 DesiMart — Grocery Ordering System | Frontend

DesiMart is a **full-stack online grocery ordering system** with a modern React.js frontend that allows customers to browse grocery products, manage their cart, place orders, and track their order status.

The frontend is developed as an **MVP (Minimum Viable Product)** with a focus on a clean user interface, reusable React components, secure authentication, REST API integration, and a smooth shopping experience.

---

## 🚀 Features

### 👤 Customer

- Create an account using email and password
- Login using JWT authentication
- View user profile
- Browse grocery products
- View product details
- Browse products by category
- Add products to cart
- Increase/decrease cart quantity
- Remove products from cart
- View cart subtotal
- View tax and grand total
- Place orders
- View order history
- View order details
- Track order status
- Logout securely

### 🛒 Shopping Experience

- Responsive product listing
- Product cards
- Product images
- Product pricing
- Stock availability
- Category-based browsing
- Cart quantity management
- Dynamic cart calculations
- Checkout interface
- Order confirmation

### 🔐 Authentication

- Customer registration
- Customer login
- JWT access token
- JWT refresh token
- Protected routes
- Automatic authentication handling
- User profile integration
- Logout functionality

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| React.js | Frontend framework |
| JavaScript | Application logic |
| HTML5 | Page structure |
| CSS3 | Styling and responsive design |
| Axios | API communication |
| React Router | Client-side routing |
| JWT | Authentication |
| Vite | Frontend build tool |
| Git & GitHub | Version control |
| REST API | Backend communication |

The frontend communicates with the **Django REST Framework backend** through RESTful APIs.

---

## 🏗️ Frontend Architecture

```text
DesiMart Frontend
│
├── public
│
├── src
│   │
│   ├── components
│   │   ├── Navbar
│   │   ├── Footer
│   │   ├── ProductCard
│   │   ├── CategoryCard
│   │   └── ProtectedRoute
│   │
│   ├── pages
│   │   ├── Home
│   │   ├── Login
│   │   ├── Register
│   │   ├── Products
│   │   ├── ProductDetails
│   │   ├── Cart
│   │   ├── Checkout
│   │   ├── Orders
│   │   ├── OrderDetails
│   │   └── Profile
│   │
│   ├── services
│   │   └── API
│   │
│   ├── hooks
│   │
│   ├── context
│   │
│   ├── assets
│   │
│   ├── App.jsx
│   └── main.jsx
│
├── .env
├── package.json
├── vite.config.js
└── README.md