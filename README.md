# 🎲 Board Game Recommender

A Streamlit web application that helps you decide which board game to play from your collection!

## Features

- **Add Multiple Games**: Input your board game options with details like rating, play count, player count, and play time
- **Multiple Recommendation Methods**:
  - **Random Pick**: Completely random selection
  - **Weighted by Rating**: Favors higher-rated games
  - **Weighted by Play Count**: Favors less-played games (inverse weighting)
  - **Least Played**: Picks from your least-played games
- **Game Management**: View, add, and remove games from your list
- **Recommendation History**: Track your previous recommendations
- **Beautiful UI**: Clean, modern interface with custom styling
- **Session Persistence**: Games and history persist during your session

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone or download this repository**

2. **Navigate to the project directory**:
   ```bash
   cd board_game_recommender
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**:
   The app will automatically open in your default web browser at `http://localhost:8501`

## How to Use

1. **Add Games**: Use the form on the left to add board games to your selection pool
   - Enter the game name
   - Rate the game (1-10)
   - Enter how many times you've played it
   - Set player count range
   - Set approximate play time

2. **Choose Recommendation Method**: In the sidebar, select how you want the recommendation to be made

3. **Get Recommendation**: Click the "🎯 Recommend a Game!" button

4. **View Results**: See your recommended game with all its details and the reasoning behind the selection

5. **Try Again**: Click "🔄 Try Again" to get another recommendation, or add/remove games and try different methods

## Example Workflow

1. Add 3-5 games you're considering for game night
2. Select "Weighted by Rating" if you want to play your favorite
3. Select "Least Played" if you want to try something new
4. Click recommend and enjoy your chosen game!

## Project Structure

```
board_game_recommender/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Requirements

- `streamlit>=1.28.0` - Web framework for the application

## Development

To modify the application:

1. Edit `app.py` with your preferred code editor
2. The app will auto-reload when you save changes (if running with `streamlit run`)
3. Refresh your browser to see changes

## Contributing

Feel free to fork this project and submit pull requests with improvements!

## License

This project is open source and available for personal and commercial use.

## Support

If you encounter any issues or have suggestions, please open an issue in the repository.

---

Made with ❤️ for board game lovers everywhere 🎲