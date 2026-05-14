# Deployment Guide: Push to GitHub and Deploy on Streamlit Community Cloud

Your app is now ready to be deployed! Follow these steps to push your code to GitHub and deploy it on Streamlit Community Cloud.

## Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and log in to your account
2. Click the **"+"** icon in the top right corner and select **"New repository"**
3. Fill in the repository details:
   - **Repository name**: `board-game-recommender` (or your preferred name)
   - **Description**: "A Streamlit app that helps you decide which board game to play"
   - **Visibility**: Public (required for Streamlit Community Cloud)
   - **Initialize with README**: ❌ (leave unchecked - we already have a README)
4. Click **"Create repository"**

## Step 2: Push Your Code to GitHub

After creating the repository, GitHub will show you commands to push your code. We'll use a slightly modified version:

### Option A: Using HTTPS (Recommended for beginners)

```powershell
# Navigate to your project
cd board_game_recommender

# Add GitHub as remote (replace YOUR_USERNAME with your GitHub username)
& 'C:\Program Files\Git\bin\git.exe' remote add origin https://github.com/YOUR_USERNAME/board-game-recommender.git

# Push your code
& 'C:\Program Files\Git\bin\git.exe' push -u origin master
```

When prompted, enter your GitHub username and password (or personal access token if you have two-factor authentication enabled).

### Option B: Using SSH (More secure, requires SSH key setup)

If you have SSH keys set up with GitHub:

```powershell
cd board_game_recommender
& 'C:\Program Files\Git\bin\git.exe' remote add origin git@github.com:YOUR_USERNAME/board-game-recommender.git
& 'C:\Program Files\Git\bin\git.exe' push -u origin master
```

## Step 3: Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"Sign up"** or **"Login"** (use your GitHub account)
3. Once logged in, click **"New app"**
4. Fill in the deployment details:
   - **Repository**: Select `board-game-recommender` from the dropdown
   - **Branch**: `master` (or `main` if that's what you used)
   - **App file path**: `app.py`
5. Click **"Deploy!"**

## Step 4: Access Your Deployed App

After deployment (usually takes 1-2 minutes), Streamlit will provide you with a unique URL like:
```
https://your-username-board-game-recommender-app-abc123.streamlit.app
```

You can share this URL with anyone, and they'll be able to use your app!

## Troubleshooting

### Git Push Issues

**Authentication failed:**
- If using HTTPS, make sure you're using the correct GitHub credentials
- If you have 2FA enabled, you'll need a personal access token instead of your password
- Create a token at: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)

**Repository not found:**
- Double-check the repository URL
- Make sure the repository is public (Streamlit Community Cloud requires public repos)

### Streamlit Deployment Issues

**App fails to deploy:**
- Check that `requirements.txt` is in the root directory
- Verify that `app.py` is the correct filename
- Look at the deployment logs in Streamlit Cloud for error messages

**App deploys but doesn't work:**
- Make sure all imports are correct
- Check that you're not using any local file paths
- Verify that the app works locally first

## Updating Your App

To make changes and deploy updates:

1. Edit your files locally
2. Commit the changes:
   ```powershell
   cd board_game_recommender
   & 'C:\Program Files\Git\bin\git.exe' add .
   & 'C:\Program Files\Git\bin\git.exe' commit -m "Your update message"
   & 'C:\Program Files\Git\bin\git.exe' push
   ```
3. Streamlit Cloud will automatically redeploy when it detects changes

## Additional Resources

- [Streamlit Community Cloud Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- [GitHub Docs: Pushing to a remote repository](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository)
- [Streamlit Deployment Guide](https://docs.streamlit.io/knowledge-base/tutorials/deploy)

---

**Note:** Streamlit Community Cloud is free for public repositories. For private repositories or advanced features, you may need a paid plan.

Good luck with your deployment! 🚀