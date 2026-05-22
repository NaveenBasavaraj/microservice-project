# 🎯 **Phase 4: Docker PostgreSQL**

## **Goal**
Run PostgreSQL database in a Docker container and connect to it manually to verify it works.

---

## 📖 **Mini Theory: Why Docker? Why PostgreSQL?**

### **Why PostgreSQL?**

**PostgreSQL** is a powerful, open-source relational database. It's:
- Industry standard (used by Instagram, Spotify, Netflix)
- Free and open-source
- Supports complex queries, relationships, transactions
- Better than SQLite for production apps

### **Why Docker?**

**Docker** packages software into "containers" - isolated environments that run the same way everywhere.

**Without Docker:**
```
You: "My database works!"
Teammate: "Mine doesn't install..."
You: "Did you install PostgreSQL 15?"
Teammate: "I have version 12..."
You: "Did you set the password?"
Teammate: "What password?"
```

**With Docker:**
```
You: "Run `docker-compose up`"
Teammate: "It works!"
```

**Benefits:**
- Everyone has the EXACT same database version
- No installation mess on your computer
- Easy to reset (delete container, start fresh)
- Same setup works on Mac, Windows, Linux
- Production servers can use the same setup

---

## 🐳 **What is Docker Compose?**

**Docker** runs containers  
**Docker Compose** runs multiple containers together from one file

We'll create `docker-compose.yml` that defines:
- PostgreSQL container (database)
- pgAdmin container (optional, visual database tool)

One command starts everything! 🚀

---

## 💻 **Let's Build It!**

### **Step 1: Install Docker Desktop**

**Download:** https://www.docker.com/products/docker-desktop/

**Installation:**
- Windows: Download and install (requires WSL 2)
- Mac: Download and install
- Linux: Install Docker Engine + Docker Compose

**Verify installation:**
```bash
docker --version
docker-compose --version
```

You should see something like:
```
Docker version 24.0.0
Docker Compose version v2.20.0
```

**Start Docker Desktop** (the app with the whale icon) and make sure it's running!

---

### **Step 2: Create `docker-compose.yml`**

Create this file in the ROOT folder (same level as `app/` folder):

```yaml name=docker-compose.yml
# Docker Compose configuration for ShortLink API
# This file defines all the services (containers) our application needs

version: '3.8'

services:
  # PostgreSQL Database Service
  db:
    image: postgres:15-alpine          # Use PostgreSQL version 15 (alpine = smaller image)
    container_name: shortlink_db       # Name of the container
    restart: unless-stopped            # Auto-restart if it crashes
    
    # Environment variables for PostgreSQL
    environment:
      POSTGRES_USER: postgres          # Database username
      POSTGRES_PASSWORD: postgres      # Database password (CHANGE IN PRODUCTION!)
      POSTGRES_DB: shortlink_db        # Database name
      PGDATA: /var/lib/postgresql/data/pgdata  # Where data is stored inside container
    
    # Port mapping: host_port:container_port
    ports:
      - "5432:5432"                    # Access database at localhost:5432
    
    # Persist data even if container is deleted
    volumes:
      - postgres_data:/var/lib/postgresql/data
    
    # Health check (verify database is ready)
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # pgAdmin (Optional - Database Management Tool)
  pgadmin:
    image: dpage/pgadmin4:latest       # pgAdmin 4 - web-based database UI
    container_name: shortlink_pgadmin
    restart: unless-stopped
    
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com     # Login email
      PGADMIN_DEFAULT_PASSWORD: admin            # Login password
      PGADMIN_CONFIG_SERVER_MODE: 'False'        # Run in desktop mode
    
    ports:
      - "5050:80"                      # Access pgAdmin at localhost:5050
    
    depends_on:
      - db                             # Start db before pgadmin
    
    volumes:
      - pgadmin_data:/var/lib/pgadmin

# Named volumes (persistent storage)
volumes:
  postgres_data:                       # Database files stored here
    driver: local
  pgadmin_data:                        # pgAdmin settings stored here
    driver: local
```

**📝 Let's Break This Down:**

**Line 1:** Comments start with `#`

**Line 4:** `version: '3.8'`
- Docker Compose file format version
- Use 3.8 for modern features

**Lines 7-32:** PostgreSQL service (`db`)
- `image`: Which Docker image to use (postgres:15-alpine)
- `container_name`: What to call this container
- `environment`: Configuration variables for PostgreSQL
- `ports`: Map port 5432 in container to 5432 on your computer
- `volumes`: Save data permanently (survives container deletion!)
- `healthcheck`: Verify database is ready before app connects

**Lines 35-51:** pgAdmin service (optional, but super helpful!)
- Web-based tool to view/manage your database
- Access at `http://localhost:5050`
- Default login: admin@admin.com / admin

**Lines 54-59:** Volumes
- Named storage that persists data
- Even if you delete containers, data remains!

---

### **Step 3: Start the Database!**

Open terminal in your project folder and run:

```bash
docker-compose up -d
```

**What does this do?**
- `up`: Start services
- `-d`: Detached mode (runs in background)

**First time:** Docker will download images (takes 1-2 minutes)

You should see:
```
[+] Running 4/4
 ✔ Network shortlink-api_default      Created
 ✔ Volume "shortlink-api_postgres_data"  Created
 ✔ Container shortlink_db             Started
 ✔ Container shortlink_pgadmin        Started
```

**Verify containers are running:**
```bash
docker-compose ps
```

Should show:
```
NAME                 IMAGE                    STATUS
shortlink_db         postgres:15-alpine       Up
shortlink_pgadmin    dpage/pgadmin4:latest    Up
```

---

### **Step 4: Test PostgreSQL Connection (Command Line)**

Let's connect to PostgreSQL using the command line tool!

**Enter the container:**
```bash
docker exec -it shortlink_db psql -U postgres -d shortlink_db
```

**What does this mean?**
- `docker exec`: Run a command in a running container
- `-it`: Interactive terminal
- `shortlink_db`: Our container name
- `psql`: PostgreSQL command-line tool
- `-U postgres`: Connect as user "postgres"
- `-d shortlink_db`: Connect to database "shortlink_db"

**You should see:**
```
psql (15.x)
Type "help" for help.

shortlink_db=#
```

**Now you're INSIDE the database!** 🎉

---

### **Step 5: Run Some SQL Commands**

Try these commands (type them in the `psql` prompt):

**1. List all databases:**
```sql
\l
```

You should see `shortlink_db` in the list!

**2. Check current database:**
```sql
SELECT current_database();
```

Should return: `shortlink_db`

**3. List all tables:**
```sql
\dt
```

Should say: `Did not find any relations.` (no tables yet - we'll create them in Phase 8!)

**4. Create a test table:**
```sql
CREATE TABLE test (
    id SERIAL PRIMARY KEY,
    message TEXT
);
```

**5. Insert test data:**
```sql
INSERT INTO test (message) VALUES ('Hello from PostgreSQL!');
INSERT INTO test (message) VALUES ('Docker is awesome!');
```

**6. Query the data:**
```sql
SELECT * FROM test;
```

Should show:
```
 id |         message
----+-------------------------
  1 | Hello from PostgreSQL!
  2 | Docker is awesome!
```

**7. Delete test table (cleanup):**
```sql
DROP TABLE test;
```

**8. Exit psql:**
```sql
\q
```

You're back in your normal terminal! ✅

---

### **Step 6: Test pgAdmin (Visual Database Tool)**

**Open your browser:** `http://localhost:5050`

**Login:**
- Email: `admin@admin.com`
- Password: `admin`

**Add a server connection:**

1. Click **"Add New Server"**
2. **General tab:**
   - Name: `ShortLink DB`
3. **Connection tab:**
   - Host: `db` (this is the service name from docker-compose.yml)
   - Port: `5432`
   - Username: `postgres`
   - Password: `postgres`
   - Save password: ✅ (check this)
4. Click **Save**

**Explore the database:**
- Expand: `ShortLink DB` → `Databases` → `shortlink_db` → `Schemas` → `public` → `Tables`
- No tables yet (we'll create them in Phase 8!)

**pgAdmin is your visual database explorer** - you can see tables, run queries, view data, etc. Super helpful for debugging! 🔍

---

## 🎓 **What You Just Learned**

✅ **Docker basics** - containers and images  
✅ **Docker Compose** - orchestrating multiple services  
✅ **PostgreSQL** - professional database  
✅ **Port mapping** - accessing container services  
✅ **Volumes** - persistent data storage  
✅ **psql** - command-line database access  
✅ **pgAdmin** - visual database management  
✅ **SQL basics** - CREATE, INSERT, SELECT, DROP  

---

## 🐳 **Docker Commands Cheat Sheet**

```bash
# Start services (in background)
docker-compose up -d

# Stop services
docker-compose down

# Stop and remove volumes (deletes all data!)
docker-compose down -v

# View running containers
docker-compose ps

# View logs
docker-compose logs

# View logs for specific service
docker-compose logs db

# Follow logs in real-time
docker-compose logs -f db

# Restart a service
docker-compose restart db

# Access PostgreSQL shell
docker exec -it shortlink_db psql -U postgres -d shortlink_db

# Access container bash shell
docker exec -it shortlink_db bash
```

---

## 🔧 **Common Issues & Solutions**

### **Issue 1: "Port 5432 is already in use"**

**Cause:** PostgreSQL is already installed on your computer

**Solution:** Change the port in `docker-compose.yml`:
```yaml
ports:
  - "5433:5432"  # Use port 5433 on your computer instead
```

Then update `.env`:
```
DATABASE_URL="postgresql://postgres:postgres@localhost:5433/shortlink_db"
```

---

### **Issue 2: "Cannot connect to Docker daemon"**

**Cause:** Docker Desktop is not running

**Solution:** Start Docker Desktop (look for the whale icon)

---

### **Issue 3: pgAdmin shows "Unable to connect"**

**Cause:** Wrong host name

**Solution:** Use `db` as the host (not `localhost`)
- Inside Docker, containers talk to each other by service name
- `db` is the name in `docker-compose.yml`

---

## 🧪 **Try These Experiments**

**Experiment 1: Data persistence**

1. Connect to psql and create a test table with data
2. Stop containers: `docker-compose down`
3. Start containers: `docker-compose up -d`
4. Connect to psql again - your data is still there! ✅

**Experiment 2: Fresh start**

```bash
# Delete everything including data
docker-compose down -v

# Start fresh
docker-compose up -d
```

Data is gone! This is useful when you want to reset.

**Experiment 3: View logs**

```bash
docker-compose logs -f db
```

Watch database logs in real-time. Open another terminal and connect with psql - you'll see the connection logged!

---

## 📦 **Step 7: Update `.env` (Verify)**

Your `.env` should have this (should already be there from Phase 3):

```text name=.env
# ... other settings ...

# Database Settings
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/shortlink_db"
```

**Breaking down this URL:**
- `postgresql://` - Database type
- `postgres:postgres` - username:password
- `@localhost:5432` - host:port
- `/shortlink_db` - database name

---

## 📂 **Your Project Now Looks Like This**

```
shortlink-api/
├── venv/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── root.py
│   ├── models/
│   │   └── __init__.py
│   └── schemas/
│       └── __init__.py
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml       ← NEW! Database containers
└── requirements.txt
```

---

## 🎯 **Phase 4 Complete! 🎉**

**What you have now:**
- ✅ PostgreSQL database running in Docker
- ✅ pgAdmin for visual database management
- ✅ Persistent data storage with volumes
- ✅ Easy start/stop/reset capabilities
- ✅ Same database environment as production
- ✅ Manual database access verified

**You now have a professional development database setup!** 🐘

---

## 🔗 **Coming in Phase 5: SQLAlchemy Connection**

We'll:
- Install SQLAlchemy (Python ORM)
- Create `app/database.py`
- Connect Python to PostgreSQL
- Test the connection with a simple script

**ORM = Object-Relational Mapping** - Write Python code instead of SQL!

---

## 📸 **Before Moving On - Checklist**

- [ ] Docker Desktop installed and running
- [ ] `docker-compose up -d` starts without errors
- [ ] You can connect via psql command line
- [ ] You successfully ran SQL commands in psql
- [ ] pgAdmin opens at localhost:5050
- [ ] You can see the database in pgAdmin
- [ ] You understand what volumes do (persistent data)
- [ ] You know how to stop containers (`docker-compose down`)

---

## 💡 **Pro Tips**

**Tip 1:** Keep Docker Desktop running while developing
- Your database needs to be running for the app to work!

**Tip 2:** Use pgAdmin for debugging
- When something goes wrong, check pgAdmin to see actual data

**Tip 3:** Reset database when needed
```bash
docker-compose down -v  # Delete everything
docker-compose up -d    # Start fresh
```

**Tip 4:** Check logs when debugging
```bash
docker-compose logs db
```

---

