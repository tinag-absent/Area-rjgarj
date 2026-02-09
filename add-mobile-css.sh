#!/bin/bash

# すべてのHTMLファイルにmobile.cssを追加

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
    # mobile.cssが既に含まれているかチェック
    if ! grep -q "mobile.css" "$file"; then
      # sidebar.cssの後にmobile.cssを追加
      sed -i 's|<link rel="stylesheet" href="./css/sidebar.css">|<link rel="stylesheet" href="./css/sidebar.css">\n  <link rel="stylesheet" href="./css/mobile.css">|' "$file"
      echo "Added mobile.css to $file"
    else
      echo "mobile.css already in $file"
    fi
  fi
done

# divisionsフォルダ内のファイル
for file in divisions/*.html; do
  if [ -f "$file" ]; then
    if ! grep -q "mobile.css" "$file"; then
      sed -i 's|<link rel="stylesheet" href="../css/sidebar.css">|<link rel="stylesheet" href="../css/sidebar.css">\n  <link rel="stylesheet" href="../css/mobile.css">|' "$file"
      echo "Added mobile.css to $file"
    else
      echo "mobile.css already in $file"
    fi
  fi
done

echo "Done!"
