from flask import Flask, render_template_string

app = Flask(__name__)

# FRONTEND UI LAYER (Gold, White, and Black Casino Theme with Slider)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ERIE GAMES 777</title>
    <style>
        :root {
            --bg-black: #0a0a0a;
            --surface-black: #141414;
            --accent-gold: #d4af37;
            --gold-glow: #f3e5ab;
            --text-white: #ffffff;
            --text-gray: #cccccc;
            --pure-white: #ffffff;
        }

        body {
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-black);
            color: var(--text-white);
            margin: 0;
            padding: 0;
        }

        /* Header / Logo Section */
        header {
            background: linear-gradient(180deg, #000000 70%, #1a1508 100%);
            border-bottom: 3px solid var(--accent-gold);
            padding: 30px 20px;
            text-align: center;
        }

        .logo-container img {
            max-height: 120px;
            width: auto;
            margin-bottom: 10px;
            filter: drop-shadow(0px 0px 8px rgba(212, 175, 55, 0.6));
        }

        header h1 {
            color: var(--text-white);
            font-size: 2.8rem;
            margin: 5px 0 0 0;
            text-transform: uppercase;
            letter-spacing: 3px;
            text-shadow: 0px 2px 10px rgba(212, 175, 55, 0.5);
        }

        header p {
            color: var(--accent-gold);
            font-size: 1.2rem;
            margin: 5px 0 0 0;
            font-weight: 600;
            letter-spacing: 1px;
        }

        .container {
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
        }

        /* Split Screen Showcase Layout */
        .showcase-split {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            background-color: var(--surface-black);
            border: 1px solid #222;
            border-top: 4px solid var(--accent-gold);
            border-radius: 12px;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.7);
            margin-top: 20px;
        }

        @media (max-width: 768px) {
            .showcase-split {
                grid-template-columns: 1fr;
                gap: 30px;
                padding: 25px;
            }
        }

        /* Left Side Layout */
        .split-left {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        /* CSS PURE IMAGE SLIDER */
        .slider-frame {
            width: 100%;
            height: 320px;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #333;
            position: relative;
        }

        .slider-container {
            display: flex;
            width: 300%; /* Three images = 300% width */
            height: 100%;
            animation: slideAnimation 12s infinite ease-in-out;
        }

        .slider-container img {
            width: 33.333%; /* Each image takes up exactly 1/3 of container */
            height: 100%;
            object-fit: cover;
        }

        /* Keyframes for smooth looping transition across 3 pictures */
        @keyframes slideAnimation {
            0% { margin-left: 0%; }
            25% { margin-left: 0%; }
            33% { margin-left: -100%; }
            58% { margin-left: -100%; }
            66% { margin-left: -200%; }
            91% { margin-left: -200%; }
            100% { margin-left: 0%; }
        }

        .store-address {
            font-size: 1.15rem;
            color: var(--pure-white);
            line-height: 1.5;
            font-weight: 500;
            margin: 5px 0;
        }

        .maps-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #d4af37 0%, #aa841b 100%);
            color: #000000;
            padding: 14px 24px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            max-width: 280px;
            box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
        }

        .maps-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(212, 175, 55, 0.5);
            background: linear-gradient(135deg, #f3e5ab 0%, #d4af37 100%);
        }

        /* Right Side Layout */
        .split-right {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .lounge-pitch {
            font-size: 1.3rem;
            line-height: 1.7;
            color: var(--text-white);
            margin-bottom: 35px;
            border-left: 4px solid var(--accent-gold);
            padding-left: 15px;
        }

        .perk-item {
            display: flex;
            align-items: flex-start;
            margin-bottom: 20px;
            background: rgba(255,255,255,0.02);
            padding: 15px 20px;
            border-radius: 8px;
            border: 1px solid #222;
        }

        .perk-icon {
            font-size: 1.8rem;
            margin-right: 15px;
            color: var(--accent-gold);
        }

        .perk-text h4 {
            margin: 0 0 4px 0;
            font-size: 1.15rem;
            color: var(--accent-gold);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .perk-text p {
            margin: 0;
            color: var(--text-gray);
            font-size: 0.95rem;
        }

        footer {
            text-align: center;
            padding: 40px 20px;
            color: var(--text-gray);
            font-size: 0.95rem;
            border-top: 1px solid #222;
            margin-top: 60px;
            background-color: #000000;
        }
    </style>
</head>
<body>

    <header>
        <div class="logo-container">
            <img src="/static/logo.png" alt="Store Logo" onerror="this.style.display='none'">
        </div>
        <h1>777 Skill Games Lounge</h1>
        <p>Premium Entertainment Experience</p>
    </header>

    <div class="container">
        
        <!-- Main Split Layout Card -->
        <div class="showcase-split">
            
            <!-- Left Side: Sliding Pictures, Address & Navigation -->
            <div class="split-left">
                <div class="slider-frame">
                    <div class="slider-container">
                        <!-- System looks for local files store1, store2, store3. Fallback links keep it working out of the box. -->
                        <img src="/static/store1.jpg" alt="Store Image 1" onerror="this.src='https://images.unsplash.com/photo-1543269664-76bc3997d9ea?auto=format&fit=crop&w=600&q=80'">
                        <img src="/static/store2.jpg" alt="Store Image 2" onerror="this.src='https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=600&q=80'">
                        <img src="/static/store3.jpg" alt="Store Image 3" onerror="this.src='https://images.unsplash.com/photo-1518609878373-06d740f60d8b?auto=format&fit=crop&w=600&q=80'">
                    </div>
                </div>
                
                <div class="store-address">
                    <strong>Our Location:</strong><br>
                    2421 Asbury rd,<br>
                    Erie, PA 16506
                </div>
                <a href="https://www.google.com/maps/place/42%C2%B004'24.6%22N+80%C2%B010'52.8%22W/@42.0734285,-80.1816019,21z/data=!4m4!3m3!8m2!3d42.073509!4d-80.181342?entry=ttu&g_ep=EgoyMDI2MDYyNC4wIKXMDSoASAFQAw%3D%3D" target="_blank" class="maps-btn">📍 Get Directions on Maps</a>
            </div>
            
            <!-- Right Side: Store Description & Core Features -->
            <div class="split-right">
                <div class="lounge-pitch">
                    A high-class 21+ entertainment lounge featuring the latest legal skill-based games. We offer a welcoming environment with complimentary beverages.
                </div>
                
                <!-- Feature 1 -->
                <div class="perk-item">
                    <div class="perk-icon">🎰</div>
                    <div class="perk-text">
                        <h4>Skill-Based Games</h4>
                        <p>Play the latest legal games.</p>
                    </div>
                </div>

                <!-- Feature 2 -->
                <div class="perk-item">
                    <div class="perk-icon">🥤</div>
                    <div class="perk-text">
                        <h4>Free soft Drinks</h4>
                        <p>Enjoy complimentary refreshments.</p>
                    </div>
                </div>

                <!-- Feature 3 -->
                <div class="perk-item">
                    <div class="perk-icon">🕒</div>
                    <div class="perk-text">
                        <h4>Daily Hours</h4>
                        <p>Open from 10:00 AM to 12:00 PM.</p>
                    </div>
                </div>
            </div>

        </div>

    </div>

    <footer>
        <p>&copy; 2026 777 Skill Games Lounge. Must be 21+ to enter. All rights reserved.</p>
    </footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    print("\\n[+] Launching Slider Lounge Floor Server... Open your browser to http://127.0.0.1:5000\\n")
    app.run(debug=True, port=5000)
