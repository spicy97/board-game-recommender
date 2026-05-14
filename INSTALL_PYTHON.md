# Python Installation Guide for Windows

To run the Board Game Recommender app, you need Python 3.8 or higher installed on your system.

## Quick Installation Steps

### Option 1: Install from Microsoft Store (Easiest)

1. Open the **Microsoft Store** on your Windows 11 computer
2. Search for **"Python 3.11"** (or the latest version available)
3. Click **"Get"** or **"Install"**
4. Wait for the installation to complete
5. Open a new Command Prompt or PowerShell window
6. Type `python --version` to verify installation

### Option 2: Install from Python.org (Recommended)

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest Python 3.x.x installer (usually Python 3.11 or 3.12)
3. **Important:** During installation, check the box that says **"Add Python to PATH"**
4. Click **"Install Now"**
5. After installation, open a new Command Prompt or PowerShell window
6. Type `python --version` to verify installation

### Option 3: Install via Winget (Command Line)

1. Open PowerShell as Administrator
2. Run the command:
   ```powershell
   winget install Python.Python.3.11
   ```
3. Follow any prompts
4. Open a new terminal window
5. Type `python --version` to verify

## Verifying Installation

After installation, verify Python is working:

```powershell
python --version
```

You should see output like: `Python 3.11.5` or similar.

Also verify pip (Python's package installer) is working:

```powershell
pip --version
```

## Installing Streamlit

Once Python is installed, install Streamlit:

1. Open Command Prompt or PowerShell
2. Navigate to the project folder:
   ```powershell
   cd board_game_recommender
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Running the App

After installing Streamlit:

```powershell
cd board_game_recommender
streamlit run app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`.

## Troubleshooting

### "Python was not found" error

If you still see this error after installation:

1. **Restart your computer** - This helps refresh the PATH environment variables
2. **Check PATH manually:**
   - Press `Win + R`, type `sysdm.cpl`, and press Enter
   - Go to the "Advanced" tab and click "Environment Variables"
   - Under "System variables", find and select "Path", then click "Edit"
   - Make sure these paths are present:
     - `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\`
     - `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\Scripts\`
   - (Replace `Python311` with your actual version)

### "pip" not recognized

If `pip` is not recognized but Python works:

1. Try using `python -m pip` instead of `pip`:
   ```powershell
   python -m pip install streamlit
   ```

2. Or add pip to your PATH following the steps above.

### Permission errors during installation

If you get permission errors when installing packages:

1. Try installing for the current user only:
   ```powershell
   pip install --user streamlit
   ```

2. Or run PowerShell as Administrator and try again.

## Alternative: Using a Virtual Environment (Recommended for Development)

For better package management, consider using a virtual environment:

1. Navigate to your project folder:
   ```powershell
   cd board_game_recommender
   ```

2. Create a virtual environment:
   ```powershell
   python -m venv venv
   ```

3. Activate it:
   ```powershell
   .\venv\Scripts\Activate
   ```

4. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

5. Run the app:
   ```powershell
   streamlit run app.py
   ```

To deactivate the virtual environment later, simply type:
```powershell
deactivate
```

## Need More Help?

- Python official documentation: [https://docs.python.org/3/using/windows.html](https://docs.python.org/3/using/windows.html)
- Streamlit documentation: [https://docs.streamlit.io/](https://docs.streamlit.io/)

---

Once Python is installed and you've followed these steps, you'll be ready to use the Board Game Recommender app!