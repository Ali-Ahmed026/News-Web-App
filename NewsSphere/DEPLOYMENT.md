# Render Deployment Guide

This guide provides step-by-step instructions to deploy NewsSphere on Render.

## Prerequisites

- GitHub account with this repository pushed
- Render account (free at [render.com](https://render.com))
- News API key from [newsapi.org](https://newsapi.org)
- A generated Django secret key

## What's Been Configured

✅ **Procfile** - Tells Render how to run the app  
✅ **runtime.txt** - Specifies Python 3.11.7  
✅ **requirements.txt** - Updated with `psycopg2-binary` and `dj-database-url`  
✅ **settings.py** - Configured for PostgreSQL and production security  

## Step-by-Step Deployment

### Step 1: Create a PostgreSQL Database on Render

1. Go to [render.com](https://render.com) and sign in
2. Click **"New +"** → **"PostgreSQL"**
3. Configure:
   - **Name**: `newssphere-db`
   - **Database**: `newssphere`
   - **User**: `newssphere`
   - **Region**: Choose closest to your location
   - **Plan**: Free
4. Click **"Create Database"**
5. Wait 2-3 minutes for the database to be created
6. **Copy the internal database URL** from the database dashboard (looks like: `postgresql://user:password@host:5432/dbname`)

### Step 2: Create a Web Service

1. Click **"New +"** → **"Web Service"**
2. Select your GitHub repository (`News-Web-App`)
3. Configure:
   - **Name**: `newssphere` (or any name you prefer)
   - **Region**: Same as your database
   - **Branch**: `main`
   - **Runtime**: Python 3
   - **Build Command**: 
     ```
     pip install -r NewsSphere/requirements.txt && python NewsSphere/manage.py collectstatic --no-input && python NewsSphere/manage.py migrate
     ```
   - **Start Command**: 
     ```
     gunicorn NewsSphere.newssphere.wsgi
     ```
   - **Plan**: Free tier
4. Click **"Create Web Service"**
5. Render will now build and deploy your app (takes 3-5 minutes)

### Step 3: Set Environment Variables

While the service is building, configure environment variables:

1. Go to your Web Service dashboard
2. Click the **"Environment"** tab
3. Add these variables:

| Key | Value | Notes |
|-----|-------|-------|
| `DEBUG` | `False` | Disable debug mode in production |
| `SECRET_KEY` | Generate a new one | Run: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` |
| `NEWS_API_KEY` | Your News API key | Get from [newsapi.org](https://newsapi.org) |
| `DATABASE_URL` | Your PostgreSQL URL | Paste the internal URL from Step 1 |
| `ALLOWED_HOSTS` | Your Render domain | Format: `your-service-name.onrender.com` |

4. Click **"Save Changes"**
5. Render will automatically redeploy with the new variables

### Step 4: Create Superuser

Once deployment is complete:

1. In your Web Service dashboard, go to the **"Shell"** tab
2. Run:
   ```bash
   python NewsSphere/manage.py createsuperuser
   ```
3. Follow the prompts to create your admin account
4. Your app will be live at: `https://your-service-name.onrender.com`
5. Access admin dashboard at: `https://your-service-name.onrender.com/admin`

## Troubleshooting

### Build Fails
- Check the **Logs** tab for errors
- Verify all environment variables are set
- Ensure `requirements.txt` has correct packages

### Database Won't Connect
- Verify `DATABASE_URL` matches exactly from your PostgreSQL database
- Ensure database is in the same region as your web service
- Check that DATABASE_URL is using the **internal** connection string

### Static Files Not Loading
- Already configured with WhiteNoise
- Ensure `STATIC_ROOT` and `STATIC_URL` are correct in settings.py

### News API Not Working
- Verify `NEWS_API_KEY` environment variable is set
- Check that your API key is valid at newsapi.org

### 500 Error After Deploy
- Check **Logs** tab
- May need to manually run migrations in Shell:
  ```bash
  python NewsSphere/manage.py migrate
  ```

## Free Tier Limitations

⚠️ **Important to Know:**

- Web service spins down after 15 minutes of inactivity (first request takes ~30 seconds)
- Free PostgreSQL database has storage limits
- Upgrade to paid plans if you need:
  - Always-on service
  - More database storage
  - Better performance

## Monitoring & Logs

- **View Logs**: Go to Web Service → Logs tab
- **Monitor Performance**: Check CPU/Memory usage
- **Redeploy**: Push to GitHub or click "Manual Deploy" button

## Update Your App

To deploy updates:

1. Make changes locally
2. Commit: `git commit -am "Update message"`
3. Push: `git push origin main`
4. Render automatically redeploys

## Custom Domain (Optional)

1. Go to Web Service → Settings → Custom Domain
2. Add your domain
3. Update DNS records with provided CNAME
4. SSL certificate is automatically provisioned

---

**Your app is ready for production!** 🚀

For support, visit [render.com/docs](https://render.com/docs)
