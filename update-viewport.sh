#!/bin/bash

# すべてのHTMLファイルのビューポート設定を最適化

files=(
  "index.html"
  "divisions.html"
  "dashboard.html"
  "phenomenon.html"
  "login.html"
  "missions.html"
  "map.html"
  "chat.html"
  "classified.html"
  "entities.html"
  "modules.html"
  "mission-detail.html"
  "personnel-detail.html"
)

for file in "${files[@]}"; do
  if [ -f "$file" ]; then
    # 既存のviewportを最適化されたものに置換
    sed -i 's|<meta name="viewport" content="width=device-width, initial-scale=1.0">|<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">|' "$file"
    echo "Updated viewport in $file"
  fi
done

# divisionsフォルダ内のファイル
for file in divisions/*.html; do
  if [ -f "$file" ]; then
    sed -i 's|<meta name="viewport" content="width=device-width, initial-scale=1.0">|<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">|' "$file"
    echo "Updated viewport in $file"
  fi
done

echo "Done!"
