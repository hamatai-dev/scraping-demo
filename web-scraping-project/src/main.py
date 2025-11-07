import json
from scraper import scrape_data

def main():
    # 例として、Pythonの公式サイトをスクレイピング
    url = "https://www.python.org/"
    
    print("=" * 50)
    print("スクレイピング開始")
    print("=" * 50)
    
    # データを取得
    data = scrape_data(url)
    
    if data:
        # 取得したデータを画面に表示
        print("\n【取得したデータ】")
        print(f"タイトル: {data['title']}")
        print(f"H1タグの数: {len(data['h1_tags'])}")
        print(f"H1タグの内容: {data['h1_tags']}")
        print(f"段落(p)の数: {data['p_count']}")
        
        # JSONファイルに保存
        output_path = '../data/output.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"\n✓ データを {output_path} に保存しました！")
    else:
        print("\n✗ データの取得に失敗しました")

if __name__ == "__main__":
    main()