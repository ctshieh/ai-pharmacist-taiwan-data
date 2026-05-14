# AI 藥師的呢喃：台灣用藥安全資料包

這個 repository 用來發布「AI 藥師的呢喃 / 安心藥盒」免費版 App 使用的公開離線資料包。

資料包用途：

- 台灣藥品名稱、健保碼、TFDA 許可證字號與成分正規化
- 同成分重複用藥偵測
- 同類藥物、老人高風險、腎肝功能、交互作用規則的本機比對基礎資料
- 手機 App 離線查詢與保守安全提醒

本資料包不是診斷工具，也不是完整的商用藥物交互作用資料庫。App 與資料包只作為用藥安全提醒與就醫/藥師諮詢輔助，不取代醫師、藥師或正式醫療判斷。

## 發布方式

正式資料包不 commit 進 git history。每次資料包會透過 GitHub Releases 發布：

- `manifest.json`
- `mobile_safety_package.sqlite3.gz`
- `checksums.txt`
- `NOTICE.md`
- `release_notes.md`

App 預設可讀取：

```text
https://github.com/ctshieh/ai-pharmacist-taiwan-data/releases/latest/download/manifest.json
```

App 下載後必須驗證 SHA-256 與簽章，驗證失敗不得啟用該資料包。

## iOS / Android 使用方式

手機 App 只下載資料，不下載可執行程式碼。資料包應放在 App sandbox 內，並標記為可重新下載資料，避免進入 iCloud 備份。

建議流程：

1. 下載 `manifest.json`
2. 比對版本與最低 App 版本
3. 下載 `mobile_safety_package.sqlite3.gz`
4. 驗 SHA-256
5. 驗 detached signature
6. 解壓到 staging SQLite
7. 執行 SQLite `integrity_check`
8. 切換為 active SQLite
9. 保留上一版供 rollback

## 安全原則

- 找不到藥品或成分時，不得顯示「安全」或綠色結果。
- 缺少必要資料時，必須顯示資料不足並建議詢問藥師或醫師。
- 不得建議病人自行停藥、減藥或換藥。
- 嚴重風險時，應建議立即詢問藥師或醫師；若已有嚴重症狀，應就醫或撥打緊急電話。

## 授權與資料來源

請見：

- [DATA_SOURCES.md](DATA_SOURCES.md)
- [NOTICE.md](NOTICE.md)
- [RELEASE_SCHEMA.md](RELEASE_SCHEMA.md)
