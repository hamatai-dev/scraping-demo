import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    """指定されたURLからデータを取得する関数"""
    print(f"アクセス中: {url}")
    
    try:
        # Webサイトにアクセス
        response = requests.get(url, timeout=10)
        
        # ステータスコードが200(成功)かチェック
        if response.status_code == 200:
            print("✓ アクセス成功！")
            
            # HTMLを解析
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # データを取得
            data = {
                'title': soup.title.string if soup.title else 'タイトルなし',
                'h1_tags': [h1.text.strip() for h1 in soup.find_all('h1')],
                'p_count': len(soup.find_all('p'))
            }
            
            print("✓ データ取得完了！")
            return data
        else:
            print(f"✗ エラー: ステータスコード {response.status_code}")
            return None
            
    except Exception as e:
        print(f"✗ エラーが発生しました: {e}")
        return None