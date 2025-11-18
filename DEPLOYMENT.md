# Deployment Guide - Digital Ocean

This guide will help you deploy the Sales API to Digital Ocean.

## Prerequisites

- Digital Ocean account
- Domain name (optional but recommended)
- Basic knowledge of Linux commands

## Deployment Options

### Option 1: Digital Ocean App Platform (Easiest)

1. **Push your code to GitHub** (already done)

2. **Create a new app on Digital Ocean App Platform:**
   - Go to https://cloud.digitalocean.com/apps
   - Click "Create App"
   - Connect your GitHub repository: `https://github.com/Ogujor1/new-sales-api.git`
   - Select the branch: `main`

3. **Configure the app:**
   - **Name**: sales-api
   - **Region**: Choose closest to your users
   - **Plan**: Select based on your needs (Basic plan is fine to start)

4. **Add Environment Variables:**
   ```
   SECRET_KEY=your-generated-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.ondigitalocean.app
   DATABASE_URL=postgresql://user:password@host:port/dbname
   ```

5. **Add Database:**
   - In the app settings, add a PostgreSQL database
   - Digital Ocean will automatically set the `DATABASE_URL` environment variable

6. **Configure Build Settings:**
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - Run Command: `gunicorn sales_api.wsgi:application`

7. **Deploy:**
   - Click "Deploy"
   - Wait for deployment to complete

### Option 2: Digital Ocean Droplet (More Control)

#### Step 1: Create a Droplet

1. Create a new Ubuntu 22.04 droplet
2. Choose your plan (minimum 1GB RAM recommended)
3. Add your SSH key
4. Create the droplet

#### Step 2: Connect to Your Droplet

```bash
ssh root@your-droplet-ip
```

#### Step 3: Update System and Install Dependencies

```bash
# Update system
apt update && apt upgrade -y

# Install Python and PostgreSQL
apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl -y

# Install virtualenv
pip3 install virtualenv
```

#### Step 4: Create PostgreSQL Database

```bash
# Switch to postgres user
sudo -u postgres psql

# In PostgreSQL prompt:
CREATE DATABASE sales_api_db;
CREATE USER sales_api_user WITH PASSWORD 'your_strong_password';
ALTER ROLE sales_api_user SET client_encoding TO 'utf8';
ALTER ROLE sales_api_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE sales_api_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE sales_api_db TO sales_api_user;
\q
```

#### Step 5: Clone and Setup Project

```bash
# Create project directory
mkdir -p /var/www
cd /var/www

# Clone your repository
git clone https://github.com/Ogujor1/new-sales-api.git sales_api
cd sales_api

# Create virtual environment
virtualenv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Step 6: Configure Environment Variables

```bash
# Create .env file
nano .env

# Add the following (replace with your actual values):
SECRET_KEY=your-generated-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com,your-droplet-ip
DATABASE_URL=postgresql://sales_api_user:your_strong_password@localhost:5432/sales_api_db
```

#### Step 7: Run Migrations and Create Superuser

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

#### Step 8: Configure Gunicorn

```bash
# Test Gunicorn
gunicorn sales_api.wsgi:application --bind 0.0.0.0:8000

# Create Gunicorn systemd service
nano /etc/systemd/system/gunicorn.service
```

Add the following content:

```ini
[Unit]
Description=gunicorn daemon for sales_api
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/sales_api
ExecStart=/var/www/sales_api/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/var/www/sales_api/gunicorn.sock \
          sales_api.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
# Start and enable Gunicorn
systemctl start gunicorn
systemctl enable gunicorn
systemctl status gunicorn
```

#### Step 9: Configure Nginx

```bash
# Create Nginx configuration
nano /etc/nginx/sites-available/sales_api
```

Add the following content:

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com your-droplet-ip;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        alias /var/www/sales_api/staticfiles/;
    }

    location /media/ {
        alias /var/www/sales_api/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/sales_api/gunicorn.sock;
    }
}
```

```bash
# Enable the site
ln -s /etc/nginx/sites-available/sales_api /etc/nginx/sites-enabled/

# Test Nginx configuration
nginx -t

# Restart Nginx
systemctl restart nginx

# Allow Nginx through firewall
ufw allow 'Nginx Full'
```

#### Step 10: Setup SSL with Let's Encrypt (Optional but Recommended)

```bash
# Install Certbot
apt install certbot python3-certbot-nginx -y

# Get SSL certificate
certbot --nginx -d your-domain.com -d www.your-domain.com

# Test auto-renewal
certbot renew --dry-run
```

## Post-Deployment Tasks

1. **Test your API:**
   ```bash
   curl http://your-domain.com/api/posts/
   ```

2. **Access Admin Panel:**
   - Visit: `http://your-domain.com/admin/`
   - Login with your superuser credentials

3. **Monitor Logs:**
   ```bash
   # Gunicorn logs
   journalctl -u gunicorn -f

   # Nginx logs
   tail -f /var/log/nginx/access.log
   tail -f /var/log/nginx/error.log
   ```

## Updating Your Application

```bash
# On your droplet
cd /var/www/sales_api
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
systemctl restart gunicorn
```

## Troubleshooting

### 502 Bad Gateway
- Check if Gunicorn is running: `systemctl status gunicorn`
- Check Gunicorn logs: `journalctl -u gunicorn -f`
- Restart Gunicorn: `systemctl restart gunicorn`

### Static files not loading
- Run: `python manage.py collectstatic --noinput`
- Check Nginx configuration for static file paths
- Restart Nginx: `systemctl restart nginx`

### Database connection errors
- Verify DATABASE_URL in .env file
- Check PostgreSQL is running: `systemctl status postgresql`
- Verify database credentials

## Backup Strategy

```bash
# Backup database
pg_dump -U sales_api_user sales_api_db > backup_$(date +%Y%m%d).sql

# Backup media files
tar -czf media_backup_$(date +%Y%m%d).tar.gz media/
```

## Security Recommendations

1. Change default SSH port
2. Setup firewall (UFW)
3. Enable automatic security updates
4. Use strong passwords
5. Regularly update dependencies
6. Monitor logs for suspicious activity

## Support

For issues or questions:
- GitHub Issues: https://github.com/Ogujor1/new-sales-api/issues
- Django Documentation: https://docs.djangoproject.com/
- Digital Ocean Community: https://www.digitalocean.com/community/
