Simple Flask webapp (demo) - Option A (quick demo with hardcoded coordinates)
-------------------------------------------------------------------------
What's included:
- app.py : Flask backend that queries NASA POWER API for daily precipitation.
- templates/index.html : Minimal frontend.
- static/style.css : Basic styling.
- requirements.txt : Python dependencies.

How to run (locally):
1. Create a Python virtual environment:
   python3 -m venv venv
   source venv/bin/activate    (Linux/macOS) or venv\Scripts\activate (Windows)

2. Install requirements:
   pip install -r requirements.txt

3. Run the app:
   python app.py

4. Open your browser at http://127.0.0.1:5000/

Notes:
- This is a minimal hackathon MVP (Option A). The location input is not converted to coordinates;
  instead the app uses hardcoded latitude/longitude for Bangalore (12.9716, 77.5946).
- To improve: add geocoding (convert city -> lat/lon) and expand output metrics.
