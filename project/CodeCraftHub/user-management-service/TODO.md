Anladım. **CodeCraftHub** projesini (sunucu tarafı) **mikroservis mimarisiyle** başlatıp, ilk olarak **User Management Service (Node.js + MongoDB)** mikroservisini ayağa kaldıracağız. Bu yaklaşım, proje yönergesindeki öneri akışına (mikroservis + Node.js/MongoDB ile User Service) uygundur.

Aşağıda sana **çalışır bir başlangıç repo iskeleti** ve **oluşturulacak her dosyanın tam kodu** var. Sonuç: Docker ile MongoDB + User Service birlikte kalkar; `/api/users/register`, `/api/users/login`, `/api/users/me` endpoint’leri çalışır.

---

## A) Kurulum ve Tasarım Özeti

### 1) Mimari yaklaşım

* **Mikroservis mimarisi** : Başlangıç için en kritik servis olan **User Management Service** ile başlıyoruz.
* Sonraki adımda (istersen) bu yapıya Recommendation / Exercises / Feedback gibi servisleri ayrı klasörler olarak ekleyebiliriz.

### 2) Bu teslimatta neler var?

* `services/user-service`: Node.js + Express + MongoDB (Mongoose)
* JWT ile login, `Authorization: Bearer <token>` ile korumalı örnek endpoint: `GET /api/users/me`
* Dockerfile + docker-compose: Tek komutla servis + MongoDB çalışır
* cURL ile test adımları

---

## B) Oluşturulan Dosyalar (Tam Kod)

Aşağıdaki yapı **repo kök dizininde** olacak şekilde tasarlanmıştır:

```
codecraft-hub/
├── docker-compose.yml
└── services/
    └── user-service/
        ├── Dockerfile
        ├── package.json
        ├── .env.example
        ├── .gitignore
        ├── README.md
        └── src/
            ├── app.js
            ├── config/
            │   ├── db.js
            │   ├── env.js
            │   └── server.js
            ├── controllers/
            │   └── userController.js
            ├── middlewares/
            │   └── authMiddleware.js
            ├── models/
            │   └── userModel.js
            ├── routes/
            │   └── userRoutes.js
            ├── services/
            │   └── userService.js
            └── utils/
                ├── errorHandler.js
                └── logger.js
```

---

### 1) `docker-compose.yml` (repo kökü)

```yaml
version: "3.8"

services:
  mongo:
    image: mongo:7
    container_name: codecraft-mongo
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db

  user-service:
    build:
      context: ./services/user-service
      dockerfile: Dockerfile
    container_name: codecraft-user-service
    depends_on:
      - mongo
    environment:
      PORT: "5000"
      MONGO_URI: "mongodb://mongo:27017/codecrafthub_users"
      JWT_SECRET: "change_this_in_production"
      JWT_EXPIRES_IN: "1h"
    ports:
      - "5000:5000"

volumes:
  mongo-data:
```

---

### 2) `services/user-service/package.json`

```json
{
  "name": "codecraft-user-service",
  "version": "1.0.0",
  "description": "User Management Service for CodeCraftHub (Node.js + MongoDB)",
  "main": "src/app.js",
  "scripts": {
    "start": "node src/app.js",
    "dev": "nodemon src/app.js"
  },
  "keywords": [
    "node",
    "express",
    "mongodb",
    "mongoose",
    "jwt",
    "users",
    "microservices"
  ],
  "license": "MIT",
  "dependencies": {
    "bcrypt": "^5.1.1",
    "cors": "^2.8.5",
    "dotenv": "^16.4.5",
    "express": "^4.19.2",
    "helmet": "^7.1.0",
    "jsonwebtoken": "^9.0.2",
    "mongoose": "^8.5.2",
    "morgan": "^1.10.0",
    "winston": "^3.13.1"
  },
  "devDependencies": {
    "nodemon": "^3.1.4"
  }
}
```

---

### 3) `services/user-service/.env.example`

```bash
PORT=5000
MONGO_URI=mongodb://localhost:27017/codecrafthub_users
JWT_SECRET=change_this_in_production
JWT_EXPIRES_IN=1h
```

---

### 4) `services/user-service/.gitignore`

```gitignore
node_modules
.env
npm-debug.log
yarn.lock
.DS_Store
```

---

### 5) `services/user-service/Dockerfile`

```dockerfile
FROM node:20-alpine

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install --only=production

COPY . .

EXPOSE 5000

CMD ["node", "src/app.js"]
```

---

### 6) `services/user-service/README.md`

```md
# CodeCraftHub - User Service

Node.js + Express + MongoDB (Mongoose) ile basit bir User Management Service.

## Endpoints

- POST /api/users/register
- POST /api/users/login
- GET  /api/users/me (JWT korumalı)

## Local Çalıştırma

```bash
cd services/user-service
cp .env.example .env
npm install
npm run start
```

## Docker ile Çalıştırma (Repo kökünden)

```bash
docker compose up --build
```

Servis: [http://localhost:5000](http://localhost:5000/)

```

---

### 7) `services/user-service/src/config/env.js`

```js
"use strict";

const path = require("path");
const dotenv = require("dotenv");

// .env dosyası varsa yükle (Docker environment değişkenleri varsa onları override etmez)
dotenv.config({ path: path.resolve(process.cwd(), ".env") });

const required = ["MONGO_URI", "JWT_SECRET"];

for (const key of required) {
  if (!process.env[key]) {
    // Eğitim amaçlı basit bir uyarı; prod ortamında process.exit(1) tercih edilebilir.
    console.warn(`[env] Missing required environment variable: ${key}`);
  }
}

module.exports = {
  PORT: process.env.PORT || "5000",
  MONGO_URI: process.env.MONGO_URI || "",
  JWT_SECRET: process.env.JWT_SECRET || "secret",
  JWT_EXPIRES_IN: process.env.JWT_EXPIRES_IN || "1h"
};
```

---

### 8) `services/user-service/src/config/server.js`

```js
"use strict";

const express = require("express");
const cors = require("cors");
const helmet = require("helmet");
const morgan = require("morgan");

function initServer() {
  const app = express();

  app.use(helmet());
  app.use(cors());
  app.use(express.json({ limit: "1mb" }));
  app.use(morgan("dev"));

  return app;
}

module.exports = initServer;
```

---

### 9) `services/user-service/src/config/db.js`

```js
"use strict";

const mongoose = require("mongoose");
const logger = require("../utils/logger");

async function connectDB(mongoUri) {
  if (!mongoUri) {
    logger.warn("[db] MONGO_URI is empty. Skipping MongoDB connection.");
    return;
  }

  try {
    await mongoose.connect(mongoUri);
    logger.info("[db] MongoDB connected successfully.");
  } catch (err) {
    logger.error(`[db] MongoDB connection failed: ${err?.message || err}`);
    process.exit(1);
  }
}

module.exports = connectDB;
```

---

### 10) `services/user-service/src/utils/logger.js`

```js
"use strict";

const winston = require("winston");

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || "info",
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.printf((info) => {
      return `${info.timestamp} [${info.level}] ${info.message}`;
    })
  ),
  transports: [new winston.transports.Console()]
});

module.exports = logger;
```

---

### 11) `services/user-service/src/utils/errorHandler.js`

```js
"use strict";

const logger = require("./logger");

function errorHandler(err, req, res, next) {
  logger.error(`[error] ${err?.message || err}`);

  const status = err?.statusCode || 500;
  const message =
    status >= 500 ? "Internal server error" : (err?.message || "Request error");

  res.status(status).json({ message });
}

module.exports = errorHandler;
```

---

### 12) `services/user-service/src/models/userModel.js`

```js
"use strict";

const mongoose = require("mongoose");

const userSchema = new mongoose.Schema(
  {
    username: { type: String, required: true, unique: true, trim: true, minlength: 3 },
    email: { type: String, required: true, unique: true, trim: true, lowercase: true },
    passwordHash: { type: String, required: true },
    role: {
      type: String,
      enum: ["student", "instructor", "admin"],
      default: "student"
    }
  },
  { timestamps: true }
);

userSchema.index({ username: 1 }, { unique: true });
userSchema.index({ email: 1 }, { unique: true });

const User = mongoose.model("User", userSchema);

module.exports = User;
```

---

### 13) `services/user-service/src/services/userService.js`

```js
"use strict";

const User = require("../models/userModel");

async function findById(id) {
  return User.findById(id).select("-passwordHash");
}

async function findByUsername(username) {
  return User.findOne({ username });
}

async function findByEmail(email) {
  return User.findOne({ email });
}

async function createUser({ username, email, passwordHash, role }) {
  const user = new User({ username, email, passwordHash, role });
  return user.save();
}

module.exports = {
  findById,
  findByUsername,
  findByEmail,
  createUser
};
```

---

### 14) `services/user-service/src/controllers/userController.js`

```js
"use strict";

const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const userService = require("../services/userService");
const { JWT_SECRET, JWT_EXPIRES_IN } = require("../config/env");

function normalizeEmail(email) {
  return String(email || "").trim().toLowerCase();
}

exports.registerUser = async (req, res, next) => {
  try {
    const username = String(req.body?.username || "").trim();
    const email = normalizeEmail(req.body?.email);
    const password = String(req.body?.password || "");

    if (!username || !email || !password) {
      return res.status(400).json({ message: "Missing required fields: username, email, password" });
    }

    const existingByUsername = await userService.findByUsername(username);
    if (existingByUsername) {
      return res.status(409).json({ message: "Username already exists" });
    }

    const existingByEmail = await userService.findByEmail(email);
    if (existingByEmail) {
      return res.status(409).json({ message: "Email already exists" });
    }

    const passwordHash = await bcrypt.hash(password, 10);

    const created = await userService.createUser({
      username,
      email,
      passwordHash,
      role: "student"
    });

    return res.status(201).json({
      message: "User registered successfully",
      user: {
        id: created._id,
        username: created.username,
        email: created.email,
        role: created.role
      }
    });
  } catch (err) {
    // Duplicate key hatası (race-condition vs.)
    if (err?.code === 11000) {
      return res.status(409).json({ message: "User already exists" });
    }
    return next(err);
  }
};

exports.loginUser = async (req, res, next) => {
  try {
    const identifier = String(req.body?.identifier || "").trim(); // username veya email
    const password = String(req.body?.password || "");

    if (!identifier || !password) {
      return res.status(400).json({ message: "Missing required fields: identifier, password" });
    }

    const isEmail = identifier.includes("@");
    const user = isEmail
      ? await userService.findByEmail(normalizeEmail(identifier))
      : await userService.findByUsername(identifier);

    if (!user) {
      return res.status(401).json({ message: "Invalid credentials" });
    }

    const ok = await bcrypt.compare(password, user.passwordHash);
    if (!ok) {
      return res.status(401).json({ message: "Invalid credentials" });
    }

    const token = jwt.sign(
      {
        sub: String(user._id),
        username: user.username,
        role: user.role
      },
      JWT_SECRET,
      { expiresIn: JWT_EXPIRES_IN }
    );

    return res.status(200).json({
      message: "Login successful",
      token,
      user: {
        id: user._id,
        username: user.username,
        email: user.email,
        role: user.role
      }
    });
  } catch (err) {
    return next(err);
  }
};

exports.getMe = async (req, res, next) => {
  try {
    const userId = req.user?.sub;
    if (!userId) {
      return res.status(401).json({ message: "Unauthorized" });
    }

    const me = await userService.findById(userId);
    if (!me) {
      return res.status(404).json({ message: "User not found" });
    }

    return res.status(200).json({ user: me });
  } catch (err) {
    return next(err);
  }
};
```

---

### 15) `services/user-service/src/middlewares/authMiddleware.js`

```js
"use strict";

const jwt = require("jsonwebtoken");
const { JWT_SECRET } = require("../config/env");

function authMiddleware(req, res, next) {
  const auth = req.headers["authorization"] || "";
  const [scheme, token] = auth.split(" ");

  if (scheme !== "Bearer" || !token) {
    return res.status(401).json({ message: "Missing or invalid Authorization header" });
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.user = decoded;
    return next();
  } catch (err) {
    return res.status(403).json({ message: "Invalid or expired token" });
  }
}

module.exports = authMiddleware;
```

---

### 16) `services/user-service/src/routes/userRoutes.js`

```js
"use strict";

const express = require("express");
const { registerUser, loginUser, getMe } = require("../controllers/userController");
const authMiddleware = require("../middlewares/authMiddleware");

const router = express.Router();

router.post("/register", registerUser);
router.post("/login", loginUser);
router.get("/me", authMiddleware, getMe);

module.exports = router;
```

---

### 17) `services/user-service/src/app.js`

```js
"use strict";

require("./config/env");

const initServer = require("./config/server");
const connectDB = require("./config/db");
const { PORT, MONGO_URI } = require("./config/env");
const userRoutes = require("./routes/userRoutes");
const errorHandler = require("./utils/errorHandler");

const app = initServer();

app.get("/health", (req, res) => {
  res.status(200).json({ status: "ok", service: "user-service" });
});

app.use("/api/users", userRoutes);

// Error handler (en sonda)
app.use(errorHandler);

(async () => {
  await connectDB(MONGO_URI);

  app.listen(Number(PORT), () => {
    // eslint-disable-next-line no-console
    console.log(`User Service listening on port ${PORT}`);
  });
})();
```

---

## C) Test (cURL / Postman)

> Docker ile çalıştırıyorsan  **repo kökünde** :

```bash
docker compose up --build
```

### 1) Health Check

```bash
curl -s http://localhost:5000/health
```

### 2) Register

```bash
curl -s -X POST http://localhost:5000/api/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "johndoe@example.com",
    "password": "Password123!"
  }'
```

### 3) Login (JWT al)

```bash
curl -s -X POST http://localhost:5000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "identifier": "john_doe",
    "password": "Password123!"
  }'
```

Çıktıdan `token` değerini al.

### 4) Korumalı Endpoint: `GET /api/users/me`

```bash
TOKEN="BURAYA_LOGIN_CIKTISINDAKI_TOKEN"
curl -s http://localhost:5000/api/users/me \
  -H "Authorization: Bearer $TOKEN"
```

---

## Örnek Seed Kullanıcı JSON’u

Yönergede örnek kullanıcı datası JSON formatında isteniyor; aşağıdaki formatı kullanabilirsin.

```json
[
  { "username": "john_doe", "email": "johndoe@example.com", "password": "Password123!" },
  { "username": "john_smith", "email": "johnsmith@example.com", "password": "Password123!" }
]
```

---

İstersen bir sonraki adımda:

1. Bu repo yapısına **API Gateway** ekleyelim,
2. Ardından **Interactive Coding Exercises** ve **Real-time Feedback** servislerini “stub + contract” seviyesinde çıkaralım (route’lar + DTO’lar + event/message taslağı).
