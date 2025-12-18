# GAEZ API - Vercel Deployment Guide

This guide explains how to deploy the GAEZ Soil Quality Index API to Vercel as a serverless FastAPI application.

## Overview

The GAEZ API provides crop-specific soil quality assessments using the FAO GAEZ v4 methodology adapted for the United States. It automatically retrieves SSURGO spatial data and calculates soil quality indices for various crops.

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **Vercel CLI** (optional but recommended):
   ```bash
   npm install -g vercel
   ```
3. **Git Repository**: Your code should be in a Git repository (GitHub, GitLab, or Bitbucket)

## Project Structure

The following files have been created for Vercel deployment:

```
├── api/
│   └── index.py              # Vercel serverless entry point
├── code/
│   └── US_scripts/
│       └── api/
│           ├── main.py       # FastAPI application
│           ├── models.py     # Pydantic models
│           ├── service.py    # Business logic
│           └── ...           # Other API files
├── vercel.json               # Vercel configuration
├── requirements.txt          # Python dependencies
└── .vercelignore            # Files to exclude from deployment
```

## Deployment Steps

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Push your code to Git**:
   ```bash
   git add .
   git commit -m "Add Vercel deployment configuration"
   git push origin main
   ```

2. **Import Project in Vercel**:
   - Go to [vercel.com/new](https://vercel.com/new)
   - Import your Git repository
   - Vercel will auto-detect the configuration

3. **Configure Project** (if needed):
   - Framework Preset: **Other**
   - Root Directory: **./** (leave as is)
   - Build Command: (leave empty)
   - Output Directory: (leave empty)

4. **Deploy**:
   - Click "Deploy"
   - Wait for the build to complete (first deployment may take 5-10 minutes)

### Option 2: Deploy via Vercel CLI

1. **Login to Vercel**:
   ```bash
   vercel login
   ```

2. **Deploy**:
   ```bash
   cd /path/to/GAEZ-Hyperlocalization
   vercel
   ```

3. **Follow the prompts**:
   - Set up and deploy? **Y**
   - Which scope? (Select your account/team)
   - Link to existing project? **N**
   - What's your project's name? **gaez-api**
   - In which directory is your code located? **./**

4. **Production deployment**:
   ```bash
   vercel --prod
   ```

## Configuration Details

### vercel.json

The `vercel.json` file configures:
- **Python runtime**: Uses `@vercel/python` builder
- **Entry point**: `api/index.py`
- **Timeout**: 30 seconds (maximum for Hobby plan)
- **Memory**: 3008 MB (maximum available)
- **Region**: `iad1` (US East, change as needed)

### requirements.txt

Contains all necessary Python packages:
- FastAPI and Uvicorn for the web framework
- NumPy, Pandas, SciPy for data processing
- GeoPandas, Shapely, Rasterio for geospatial operations
- Mangum for AWS Lambda/serverless compatibility

### .vercelignore

Excludes large files and unnecessary content:
- Data directories
- R notebooks and outputs
- Documentation
- Test files

## API Endpoints

Once deployed, your API will be available at `https://your-project.vercel.app` with these endpoints:

- `GET /` - Root endpoint with welcome message
- `GET /health` - Health check endpoint
- `GET /crops` - List available crops
- `POST /calculate` - Calculate soil quality indices
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

## Testing the Deployment

### Health Check
```bash
curl https://your-project.vercel.app/health
```

### List Crops
```bash
curl https://your-project.vercel.app/crops
```

### Calculate SQI (example)
```bash
curl -X POST https://your-project.vercel.app/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "latitude": 41.2427,
    "longitude": -101.6338,
    "crop_id": "4",
    "input_level": "L"
  }'
```

## Environment Variables

If your API requires environment variables:

1. **Via Vercel Dashboard**:
   - Go to Project Settings → Environment Variables
   - Add your variables (e.g., `API_KEY`, `DATABASE_URL`)

2. **Via Vercel CLI**:
   ```bash
   vercel env add VARIABLE_NAME
   ```

## Limitations & Considerations

### Vercel Serverless Limits

- **Execution Time**: 30 seconds max (Hobby), 60 seconds (Pro)
- **Memory**: 1024 MB (Hobby), 3008 MB (Pro)
- **Deployment Size**: 250 MB compressed
- **Cold Starts**: First request may be slow (~5-10 seconds)

### Recommendations

1. **Large Data Files**: Store in external storage (AWS S3, Google Cloud Storage)
2. **Long-Running Tasks**: Consider using Vercel's background functions or external workers
3. **Database**: Use serverless databases (Vercel Postgres, PlanetScale, Supabase)
4. **Caching**: Implement caching for frequently accessed data

## Monitoring

### View Logs

1. **Via Dashboard**: 
   - Go to your project → Deployments → Select deployment → Function Logs

2. **Via CLI**:
   ```bash
   vercel logs
   ```

### Performance Monitoring

Vercel provides built-in analytics:
- Request count
- Response times
- Error rates
- Bandwidth usage

Access at: `https://vercel.com/your-team/your-project/analytics`

## Troubleshooting

### Deployment Fails

1. **Check build logs** in Vercel dashboard
2. **Verify dependencies** in `requirements.txt`
3. **Check file paths** - use absolute imports
4. **Review .vercelignore** - ensure critical files aren't excluded

### Runtime Errors

1. **Check function logs** for error messages
2. **Verify Python version** compatibility (Vercel uses Python 3.9)
3. **Test locally** with the same environment

### Timeout Issues

1. **Optimize queries** and data processing
2. **Implement caching** for repeated calculations
3. **Consider upgrading** to Vercel Pro for 60s timeout

## Local Development

To run the API locally:

```bash
cd code/US_scripts
pip install -r api/requirements.txt
python run_api.py
```

Visit: http://localhost:8000/docs

## Updating the Deployment

### Automatic Deployments

Vercel automatically deploys when you push to your Git repository:
- **main/master branch** → Production
- **Other branches** → Preview deployments

### Manual Redeployment

```bash
vercel --prod
```

## Custom Domain

To use a custom domain:

1. Go to Project Settings → Domains
2. Add your domain
3. Configure DNS records as instructed
4. Wait for SSL certificate provisioning

## Support

- **API Documentation**: See `code/US_scripts/api/README.md`
- **Vercel Documentation**: https://vercel.com/docs
- **FastAPI Documentation**: https://fastapi.tiangolo.com/

## Next Steps

1. ✅ Deploy to Vercel
2. Test all endpoints
3. Set up custom domain (optional)
4. Configure monitoring and alerts
5. Optimize for production usage
6. Document API usage for your team

---

**Note**: This is a serverless deployment. For high-traffic production use, consider implementing caching, rate limiting, and monitoring solutions.
