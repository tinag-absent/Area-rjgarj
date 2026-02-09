import re
import os

def update_html_file(filepath):
    """HTMLファイルのサイドバーを更新"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # サイドバーの開始タグを見つける
    sidebar_start = content.find('<aside class="sidebar">')
    if sidebar_start == -1:
        print(f"Sidebar not found in {filepath}")
        return False
    
    # サイドバーの終了タグを見つける
    sidebar_end = content.find('</aside>', sidebar_start)
    if sidebar_end == -1:
        print(f"Sidebar end tag not found in {filepath}")
        return False
    
    # サイドバーを空のコンテナに置き換え
    new_sidebar = '<aside class="sidebar">\n      <!-- Sidebar content will be loaded by sidebar.js -->\n    </aside>'
    
    new_content = content[:sidebar_start] + new_sidebar + content[sidebar_end + len('</aside>'):]
    
    # sidebar.jsのスクリプトタグが既に存在するか確認
    if 'sidebar.js' not in new_content:
        # </body>の前にsidebar.jsを追加
        # まず、既存のスクリプトタグを探す
        script_pattern = r'<script src="[^"]*main\.js"></script>'
        match = re.search(script_pattern, new_content)
        
        if match:
            # main.jsの前にsidebar.jsを追加
            # パスを判定
            is_in_divisions = '/divisions/' in filepath or filepath.endswith('divisions/convergence.html')
            script_path = '../js/sidebar.js' if is_in_divisions else './js/sidebar.js'
            
            insert_pos = match.start()
            sidebar_script = f'  <script src="{script_path}"></script>\n  '
            new_content = new_content[:insert_pos] + sidebar_script + new_content[insert_pos:]
    
    # ファイルを保存
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated: {filepath}")
    return True

# すべてのHTMLファイルを更新
html_files = [
    'index.html',
    'divisions.html',
    'dashboard.html',
    'phenomenon.html',
    'login.html',
    'missions.html',
    'map.html',
    'chat.html',
    'classified.html',
    'entities.html',
    'modules.html',
    'mission-detail.html',
    'personnel-detail.html',
]

# divisionsフォルダ内のファイル
division_files = [
    'divisions/convergence.html',
    'divisions/support.html',
    'divisions/engineering.html',
    'divisions/foreign.html',
    'divisions/port.html',
]

all_files = html_files + division_files

for filename in all_files:
    if os.path.exists(filename):
        update_html_file(filename)
    else:
        print(f"File not found: {filename}")

print("\nAll files updated!")
