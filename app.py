from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Navratri Wishes 🌺</title>
<style>
*{box-sizing:border-box}
body{
margin:0;min-height:100vh;display:flex;justify-content:center;
align-items:center;text-align:center;font-family:Arial,sans-serif;
background:linear-gradient(135deg,#fff3e0,#ffccbc,#ffe0b2);
}
.card{
width:90%;max-width:650px;padding:45px 25px;border-radius:30px;
background:rgba(255,255,255,.85);
box-shadow:0 15px 50px rgba(120,50,0,.25);
}
.flowers{font-size:45px}
h1{font-size:40px;color:#d84315}
h2{color:#8d3b00}
p{color:#6d4c41;font-size:19px;line-height:1.6}
button{
padding:14px 30px;border:0;border-radius:30px;
background:#e65100;color:white;font-size:18px;cursor:pointer;
}
button:hover{background:#bf360c;transform:scale(1.05)}
.diyas{font-size:38px;margin:25px}
</style>
</head>
<body>
<div class="card">
<div class="flowers">🌺 🌸 🌺</div>
<h1>🙏 Happy Navratri 🙏</h1>
<h2>✨ Maa Durga aapko hamesha khush rakhein ✨</h2>
<p>Maa Durga ki kripa aap aur aapke parivaar par hamesha bani rahe. ❤️</p>
<div class="diyas">🪔 🪔 🪔</div>
<button onclick="alert('🌺 Jai Mata Di! 🙏✨')">🙏 Jai Mata Di 🙏</button>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
