# 說明

將 Facebook 粉專的文章、圖片一張匯出，並匯入至 WordPress

# 使用

1. 在 config.py 設定 Access Token 
2. 在 main.py 設定要抓取的粉絲頁 ID 
3. 執行 main.py ，圖檔會存在 images 資料夾，文字內容則在 posts.json
4. 手動上傳圖檔到 WordPress 後台
5. 在 main.php 設定圖檔 ID(會自動設定特色圖片)
6. 將所有檔案設為 777 後上傳至 WordPress
7. 啟用外掛的同時會自動匯入文章