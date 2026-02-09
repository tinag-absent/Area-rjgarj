import re
import os

def add_sidebar_script(filepath):
    """sidebar.jsのスクリプトタグを追加"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 既にsidebar.jsが追加されているか確認
    if 'sidebar.js' in content:
        print(f"sidebar.js already in {filepath}")
        return False
    
    # パスを判定
    is_in_divisions = 'divisions/' in filepath
    script_path = '../js/sidebar.js' if is_in_divisions else './js/sidebar.js'
    
    # main.jsの前に追加
    if './js/main.js' in content:
        content = content.replace(
            '<script src="./js/main.js"></script>',
            f'<script src="{script_path}"></script>\n  <script src="./js/main.js"></script>'
        )
    elif '../js/main.js' in content:
        content = content.replace(
            '<script src="../js/main.js"></script>',
            f'<script src="{script_path}"></script>\n  <script src="../js/main.js"></script>'
        )
    else:
        # main.jsが見つからない場合、</body>の前に追加
        content = content.replace(
            '</body>',
            f'  <script src="{script_path}"></script>\n</body>'
        )
    
    # ファイルを保存
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Added sidebar.js to: {filepath}")
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
        add_sidebar_script(filename)
    else:
        print(f"File not found: {filename}")

print("\nAll files updated!")
