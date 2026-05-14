# Release Schema

每個 GitHub Release 應包含下列檔案。

## `manifest.json`

App 會先下載 `manifest.json`，驗證後再下載資料包。

必要欄位：

```json
{
  "package_id": "safemed-taiwan-mobile-safety-sqlite",
  "version": "MOBILE_SAFETY_P0_20260514",
  "created_at": "2026-05-14T00:00:00+00:00",
  "minimum_app_version": "0.1.0",
  "package_url": "https://github.com/ctshieh/ai-pharmacist-taiwan-data/releases/download/v2026.05.14-p0/mobile_safety_package.sqlite3.gz",
  "package_format": "sqlite-gzip",
  "package_media_type": "application/gzip",
  "content_encoding": "gzip",
  "sha256": "gzip-file-sha256",
  "sqlite_sha256": "sqlite-file-sha256",
  "gzip_bytes": 123,
  "sqlite_bytes": 456,
  "signature": "detached-signature-or-mvp-signature",
  "signature_algorithm": "MVP_SHA256_PREFIX_SIGNATURE",
  "signature_payload_prefix": "safemed-mobile-data-package-v1:",
  "tables": {
    "mobile_drugs": 0,
    "mobile_ingredients": 0,
    "mobile_aliases": 0,
    "mobile_drug_classes": 0,
    "mobile_drug_tags": 0,
    "mobile_data_source_versions": 0
  },
  "safety_contract": {},
  "data_sources": [],
  "privacy_notice": "手機下載本資料包不需要上傳藥單；使用者藥單預設留在手機本機。"
}
```

正式版應將 `MVP_SHA256_PREFIX_SIGNATURE` 改為 Ed25519 或 RSA detached signature。MVP signature 只用於開發期防止意外檔案不一致，不等於正式安全簽章。

## `mobile_safety_package.sqlite3.gz`

壓縮後的 SQLite 資料包。SQLite 內只應包含 `mobile_*` 與 `package_metadata` 等資料包用表，不得包含：

- `users`
- `patients`
- `caregivers`
- `medication_entries`
- `reminders`
- `audit_logs`
- `ocr_jobs`
- `interaction_results`
- 任何可識別個人的資料

## `checksums.txt`

格式：

```text
<sha256>  manifest.json
<sha256>  mobile_safety_package.sqlite3.gz
<sha256>  mobile_safety_package.sqlite3
```

## `NOTICE.md`

每次 release 應附上資料來源、使用目的與免背書聲明。

## `release_notes.md`

列出：

- 來源資料版本
- 表格筆數
- 已知限制
- 是否為 P0/P1/P2 資料包
- 是否適合正式 App 使用
