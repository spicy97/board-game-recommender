import streamlit as st
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Board Game Recommender",
    page_icon="🎲",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 15px 32px;
        font-size: 16px;
    }
    .game-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .recommendation {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        margin: 20px 0;
    }
    .recommendation h2 {
        font-size: 2.5em;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🎲 Board Game Recommender")
st.markdown("""
### Can't decide which board game to play?
Add your game options below and let the recommender help you choose!
""")

# Initialize session state
if 'games' not in st.session_state:
    st.session_state.games = []
if 'recommendation' not in st.session_state:
    st.session_state.recommendation = None
if 'history' not in st.session_state:
    st.session_state.history = []

# Sidebar for settings and history
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Recommendation method
    method = st.selectbox(
        "Recommendation Method",
        ["Random Pick", "Weighted by Rating", "Weighted by Play Count", "Least Played"],
        help="Choose how the recommendation is made"
    )
    
    st.divider()
    
    # History section
    st.header("📋 Recommendation History")
    if st.session_state.history:
        for i, item in enumerate(st.session_state.history[-5:][::-1], 1):
            with st.expander(f"#{len(st.session_state.history) - i + 1}: {item['game']}"):
                st.write(f"**Date:** {item['date']}")
                st.write(f"**Method:** {item['method']}")
                st.write(f"**Players:** {len(item['games'])} games to choose from")
    else:
        st.info("No recommendations yet")
    
    st.divider()
    
    # Clear all button
    if st.button("🗑️ Clear All", use_container_width=True):
        st.session_state.games = []
        st.session_state.recommendation = None
        st.session_state.history = []
        st.rerun()

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Add Your Games")
    
    # Game input form
    with st.form(key="add_game_form", clear_on_submit=True):
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            game_name = st.text_input("Game Name", placeholder="e.g., Catan")
        
        with col_b:
            rating = st.slider("Your Rating (1-10)", 1, 10, 7)
        
        with col_c:
            play_count = st.number_input("Times Played", min_value=0, value=0)
        
        # Additional options
        col_d, col_e = st.columns(2)
        with col_d:
            min_players = st.number_input("Min Players", min_value=1, max_value=20, value=2)
        with col_e:
            max_players = st.number_input("Max Players", min_value=1, max_value=20, value=4)
        
        game_time = st.slider("Play Time (minutes)", 5, 300, 60)
        
        submitted = st.form_submit_button("➕ Add Game", use_container_width=True)
        
        if submitted and game_name:
            # Check for duplicates
            if any(g['name'].lower() == game_name.lower() for g in st.session_state.games):
                st.error(f"⚠️ '{game_name}' is already in your list!")
            else:
                new_game = {
                    'name': game_name,
                    'rating': rating,
                    'play_count': play_count,
                    'min_players': min_players,
                    'max_players': max_players,
                    'play_time': game_time,
                    'added_at': datetime.now().strftime("%H:%M:%S")
                }
                st.session_state.games.append(new_game)
                st.success(f"✅ Added '{game_name}' to your list!")
                st.rerun()
        elif submitted and not game_name:
            st.warning("⚠️ Please enter a game name!")

with col2:
    st.subheader("🎯 Current Games")
    if st.session_state.games:
        st.write(f"**{len(st.session_state.games)}** game(s) added")
        
        # Display games as cards
        for i, game in enumerate(st.session_state.games):
            with st.container():
                st.markdown(f"""
                    <div class="game-card">
                        <strong>{game['name']}</strong><br>
                        ⭐ {game['rating']}/10 | 🎮 {game['play_count']} plays<br>
                        ⏱️ {game['play_time']} min | 👥 {game['min_players']}-{game['max_players']} players
                    </div>
                """, unsafe_allow_html=True)
                
                # Remove button for each game
                if st.button(f"🗑️ Remove", key=f"remove_{i}", type="secondary"):
                    st.session_state.games.pop(i)
                    st.rerun()
    else:
        st.info("No games added yet.\nAdd some games to get started!")

# Recommendation section
st.divider()
st.subheader("🎲 Get Recommendation")

if len(st.session_state.games) < 2:
    st.warning("⚠️ Add at least 2 games to get a recommendation!")
else:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎯 Recommend a Game!", type="primary", use_container_width=True):
            # Make recommendation based on selected method
            games = st.session_state.games
            
            if method == "Random Pick":
                chosen = random.choice(games)
                reason = "Selected completely at random!"
            
            elif method == "Weighted by Rating":
                weights = [g['rating'] for g in games]
                chosen = random.choices(games, weights=weights, k=1)[0]
                reason = f"Highest rated ({chosen['rating']}/10) with weighted random selection!"
            
            elif method == "Weighted by Play Count":
                # Inverse weighting - less played games have higher chance
                max_plays = max(g['play_count'] for g in games) + 1
                weights = [max_plays - g['play_count'] + 1 for g in games]
                chosen = random.choices(games, weights=weights, k=1)[0]
                reason = f"Least played recently ({chosen['play_count']} plays) - time to try something new!"
            
            elif method == "Least Played":
                chosen = min(games, key=lambda g: g['play_count'])
                # If multiple games have same play count, pick randomly among them
                min_played = [g for g in games if g['play_count'] == chosen['play_count']]
                if len(min_played) > 1:
                    chosen = random.choice(min_played)
                reason = f"One of your least played games ({chosen['play_count']} plays)!"
            
            # Store recommendation
            st.session_state.recommendation = chosen
            st.session_state.history.append({
                'game': chosen['name'],
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'method': method,
                'games': [g['name'] for g in games]
            })
            st.rerun()

# Display recommendation
if st.session_state.recommendation:
    rec = st.session_state.recommendation
    
    st.markdown(f"""
        <div class="recommendation">
            <h2>🎉 {rec['name']}</h2>
            <p><strong>Why this game?</strong> {reason}</p>
            <div style="display: flex; justify-content: space-around; margin-top: 20px;">
                <div>
                    <span style="font-size: 2em;">⭐</span><br>
                    <strong>{rec['rating']}/10</strong><br>
                    <small>Rating</small>
                </div>
                <div>
                    <span style="font-size: 2em;">🎮</span><br>
                    <strong>{rec['play_count']}</strong><br>
                    <small>Times Played</small>
                </div>
                <div>
                    <span style="font-size: 2em;">⏱️</span><br>
                    <strong>{rec['play_time']} min</strong><br>
                    <small>Play Time</small>
                </div>
                <div>
                    <span style="font-size: 2em;">👥</span><br>
                    <strong>{rec['min_players']}-{rec['max_players']}</strong><br>
                    <small>Players</small>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Fun additional features
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔄 Try Again", use_container_width=True):
            st.session_state.recommendation = None
            st.rerun()
    with col2:
        st.metric("Games Considered", len(st.session_state.games))
    with col3:
        st.metric("Recommendation Method", method.split()[-1])

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>Made with ❤️ for board game lovers everywhere</p>
    <p><small>🎲 May the best game win! 🎲</small></p>
</div>
""", unsafe_allow_html=True)