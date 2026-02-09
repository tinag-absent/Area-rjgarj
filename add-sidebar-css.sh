#!/bin/bash

# すべてのHTMLファイルにsidebar.cssを追加

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
    # sidebar.cssが既に含まれているかチェック
    if ! grep -q "sidebar.css" "$file"; then
      # style.cssの後にsidebar.cssを追加
      sed -i 's|<link rel="stylesheet" href="./css/style.css">|<link rel="stylesheet" href="./css/style.css">\n  <link rel="stylesheet" href="./css/sidebar.css">|' "$file"
      echo "Added sidebar.css to $file"
    else
      echo "sidebar.css already in $file"
    fi
  fi
done

# divisionsフォルダ内のファイル
for file in divisions/*.html; do
  if [ -f "$file" ]; then
    if ! grep -q "sidebar.css" "$file"; then
      sed -i 's|<link rel="stylesheet" href="../css/style.css">|<link rel="stylesheet" href="../css/style.css">\n  <link rel="stylesheet" href="../css/sidebar.css">|' "$file"
      echo "Added sidebar.css to $file"
    else
      echo "sidebar.css already in $file"
    fi
  fi
done

echo "Done!"
