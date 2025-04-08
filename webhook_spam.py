import requests
import time

WEBHOOK_URL = "Webhook"  # Webhook URL'nizi buraya ekleyin
MESAJ = "Mesaj İçeriği"  # Gönderilecek mesaj
ARALIK = 1  # Saniye cinsinden gönderim aralığı (örn. 1 saniye)
MAX_GONDERIM = 10  # Kaç adet mesaj gönderilecek?

def webhook_spam():
    for i in range(MAX_GONDERIM):
        try:
            # Webhook'a POST isteği gönder
            response = requests.post(
                WEBHOOK_URL,
                json={"content": MESAJ},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 204:
                print(f"[{i+1}/{MAX_GONDERIM}] Mesaj Gönderildi!")
            else:
                print(f"Hata: {response.status_code} - Webhook geçersiz Olabilir!")
        
        except Exception as e:
            print(f"Hata oluştu: {e}")
        
        time.sleep(ARALIK)

if __name__ == "__main__":
    webhook_spam()