# Deployment Troubleshooting Guide

## Common Digital Ocean Deployment Errors

### Error: "Non-Zero Exit Code"

This error means your application crashed during startup. Here are the most common causes and fixes:

#### 1. Missing Environment Variables

**Problem**: Required environment variables not set in Digital Ocean.

**Solution**:
- Go to your Digital Ocean App Platform dashboard
- Navigate to Settings → App-Level Environment Variables
- Add the following required variables:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=${APP_DOMAIN}
```

**To generate a secure SECRET_KEY**, run this in Python:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use this online: https://djecrety.ir/

#### 2. Database Not Connected

**Problem**: App can't connect to the database.

**Solution**:
- In Digital Ocean App Platform, add a PostgreSQL database to your app
- Digital Ocean automatically creates a `DATABASE_URL` environment variable
- Ensure your app settings are configured to use it (already done in settings.py)

#### 3. Static Files Collection Failed

**Problem**: `collectstatic` command fails during build.

**Solution**:
Update your build command in Digital Ocean:
```bash
python manage.py collectstatic --noinput --clear
python manage.py migrate --noinput
```

#### 4. Port Binding Issues

**Problem**: Gunicorn not binding to the correct port.

**Solution**:
Digital Ocean expects your app to listen on port 8080. The Procfile should be:
```
web: gunicorn --worker-tmp-dir /dev/shm --bind 0.0.0.0:8080 sales_api.wsgi:application
```

#### 5. Python Version Mismatch

**Problem**: Digital Ocean using wrong Python version.

**Solution**:
Ensure `runtime.txt` exists with:
```
python-3.11.9
```

## Step-by-Step Deployment Fix

### Method 1: Using Digital Ocean App Platform (Recommended)

1. **Clone your repo fresh** (if needed):
   ```bash
   git clone https://github.com/Ogujor1/new-sales-api.git
   cd new-sales-api
   ```

2. **Create/Update App on Digital Ocean**:
   - Go to https://cloud.digitalocean.com/apps
   - Click "Create App"
   - Select "GitHub" and connect to `Ogujor1/new-sales-api`
   - Branch: `main`

3. **Configure Build Settings**:
   - **Build Command**:
     ```bash
     pip install -r requirements.txt && python manage.py collectstatic --noinput --clear && python manage.py migrate --noinput
     ```
   - **Run Command**:
     ```bash
     gunicorn --worker-tmp-dir /dev/shm --bind 0.0.0.0:8080 sales_api.wsgi:application
     ```

4. **Add Database**:
   - In the app configuration, click "Add Resource"
   - Select "Database" → "PostgreSQL"
   - Choose Dev Database (free) or Production
   - Digital Ocean will auto-configure `DATABASE_URL`

5. **Set Environment Variables**:
   Go to Settings → Environment Variables and add:

   ```
   SECRET_KEY=<generate-a-new-secret-key>
   DEBUG=False
   ALLOWED_HOSTS=${APP_DOMAIN}
   ```

6. **Deploy**:
   - Click "Next" → "Deploy"
   - Monitor the build logs for errors

### Method 2: Check Logs

View deployment logs to identify specific errors:

1. In Digital Ocean App Platform, go to your app
2. Click "Runtime Logs" or "Build Logs"
3. Look for error messages

Common log errors and fixes:

**Error**: `ModuleNotFoundError: No module named 'X'`
- **Fix**: Add missing package to `requirements.txt`

**Error**: `django.core.exceptions.ImproperlyConfigured: Set the SECRET_KEY environment variable`
- **Fix**: Add `SECRET_KEY` to environment variables

**Error**: `django.db.utils.OperationalError: could not connect to server`
- **Fix**: Ensure database is added and `DATABASE_URL` is set

**Error**: `CommandError: You must set settings.ALLOWED_HOSTS`
- **Fix**: Set `ALLOWED_HOSTS` environment variable to `${APP_DOMAIN}`

## Quick Fix Checklist

Before redeploying, ensure:

- [ ] `requirements.txt` has all dependencies
- [ ] `Procfile` exists with correct gunicorn command
- [ ] `runtime.txt` specifies Python version
- [ ] Environment variables are set in Digital Ocean:
  - `SECRET_KEY`
  - `DEBUG=False`
  - `ALLOWED_HOSTS=${APP_DOMAIN}`
- [ ] PostgreSQL database is added to your app
- [ ] Build command includes: `collectstatic` and `migrate`
- [ ] Latest code is pushed to GitHub

## Testing Locally Before Deploying

Test your production setup locally:

```bash
# Set environment variables
export SECRET_KEY="your-test-secret-key"
export DEBUG="False"
export ALLOWED_HOSTS="localhost,127.0.0.1"

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Test with gunicorn
gunicorn sales_api.wsgi:application
```

If this works locally, it should work on Digital Ocean.

## Still Having Issues?

1. **Check Digital Ocean Status**: https://status.digitalocean.com/
2. **Review Build Logs**: Look for the exact error message
3. **Check GitHub Issues**: https://github.com/Ogujor1/new-sales-api/issues
4. **Digital Ocean Community**: https://www.digitalocean.com/community/

## Contact Support

- Digital Ocean Support: https://cloud.digitalocean.com/support/tickets
- Create an issue on GitHub with your error logs
