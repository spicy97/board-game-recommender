# How to Share Your Board Game Recommender App

There are several ways to make your app accessible to people on other networks:

## Option 1: Streamlit Community Cloud (Recommended - Free & Easy)

This is the easiest and most reliable way to share your app with anyone, anywhere.

### Steps:
1. **Go to [share.streamlit.io](https://share.streamlit.io)**
2. **Log in with your GitHub account** (spicy97)
3. **Click "New app"**
4. **Connect your repository:**
   - Repository: `board-game-recommender`
   - Branch: `master`
   - App file path: `app.py`
5. **Click "Deploy!"**

### Result:
You'll get a public URL like: `https://spicy97-board-game-recommender.streamlit.app`

**Anyone can access this URL from any device, anywhere in the world!**

### Benefits:
- ✅ Free
- ✅ No setup required
- ✅ Automatically updates when you push to GitHub
- ✅ HTTPS secure connection
- ✅ Reliable hosting

## Option 2: Streamlit Cloud with Tunnel (For Testing)

If you want to test sharing temporarily without deploying:

```powershell
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

Then use a tunneling service like **ngrok**:

1. Download ngrok from [ngrok.com](https://ngrok.com)
2. Run: `ngrok http 8501`
3. Share the ngrok URL it provides

**Note:** This is temporary and only works while your computer and ngrok are running.

## Option 3: Deploy on Your Local Network

To allow people on your home network to access the app:

### Find your local IP address:
```powershell
ipconfig
```
Look for "IPv4 Address" under your network adapter (e.g., 192.168.1.178)

### Run Streamlit with network access:
```powershell
cd board_game_recommender
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

### Share the URL:
Tell others on your network to visit: `http://YOUR_IP_ADDRESS:8501`

Example: `http://192.168.1.178:8501`

**Limitations:**
- ❌ Only works for people on your WiFi/network
- ❌ Your computer must stay on and running
- ❌ Not secure for public internet access

## Option 4: Deploy to Cloud Platforms (More Control)

For more advanced deployment with full control:

### Heroku:
1. Create a Heroku account at [heroku.com](https://heroku.com)
2. Install Heroku CLI
3. Follow Heroku's Python deployment guide
4. Add a `Procfile` with: `web: streamlit run app.py --server.port $PORT`

### Railway:
1. Go to [railway.app](https://railway.app)
2. Connect your GitHub repository
3. Deploy automatically

### PythonAnywhere:
1. Sign up at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload your code
3. Set up a web app with Streamlit

## Recommended: Use Streamlit Community Cloud

For your use case, **Streamlit Community Cloud is the best option** because:

- It's completely free
- Takes 5 minutes to set up
- Anyone can access it from anywhere
- No maintenance required
- Automatic updates when you push code changes

## Quick Deployment Checklist

To deploy on Streamlit Community Cloud:

1. ✅ Your code is already on GitHub: https://github.com/spicy97/board-game-recommender
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Log in with GitHub
4. Click "New app"
5. Select your repository
6. Click "Deploy"
7. Share the URL with friends!

## Troubleshooting

**"Repository not found" on Streamlit Cloud:**
- Make sure your GitHub repository is **Public** (not Private)
- Check that you're logged into the correct GitHub account

**App won't deploy:**
- Ensure `requirements.txt` is in the root directory
- Check the deployment logs for errors
- Verify the app runs locally first

**People can't access the URL:**
- Double-check you're sharing the correct URL
- Make sure the deployment completed successfully
- Try accessing it yourself from a different device/network

---

**Need help?** Check the [Streamlit Community Cloud documentation](https://docs.streamlit.io/streamlit-community-cloud) or the [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) file in your project.