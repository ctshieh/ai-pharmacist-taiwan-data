# 安心藥盒 Android APK 安裝手冊

因 Google Play 暫時無法作為 Android 發佈管道，安心藥盒 Android 版改由官方網站連到 GitHub Release 提供 APK 下載。

請只從下列官方來源下載：

- 官方網站：<https://safemed.bridgeaiworks.com/downloads/>
- Android 安裝圖文教學：<https://safemed.bridgeaiworks.com/downloads/android-install-guide/>
- GitHub 最新 release：<https://github.com/ctshieh/ai-pharmacist-taiwan-data/releases/latest>

請不要從來路不明的網站、群組、短網址或朋友轉傳的 APK 安裝，避免拿到被修改過的檔案。

## 安裝前請先確認手機是否支援

安心藥盒 Android 版目前需要：

```text
Android 8.0 以上
```

若手機顯示「無法安裝」、「不支援此應用程式」或「應用程式未安裝」，請先到手機「設定」→「關於手機」或「軟體資訊」確認 Android 版本。

若 Android 版本低於 8.0，這支手機無法安裝目前版本，請改用較新的 Android 手機，或使用 iPhone / 網頁版。

## 1. 開啟官方下載頁

請先用手機瀏覽器開啟安心藥盒官方網站的 Android 下載頁，再按「前往 GitHub 最新 release」。

![開啟官方下載頁](https://safemed.bridgeaiworks.com/downloads/android-install-guide/assets/step-01-download.svg)

## 2. 在 GitHub 下載 APK

進入 GitHub Release 後，往下找到 **Assets**，點選檔名以 `safemed` 開頭、結尾是 `.apk` 的檔案。

請不要下載：

- `Source code (zip)`
- `Source code (tar.gz)`

這些是原始碼壓縮檔，不是手機安裝檔。

![在 GitHub Release 下載 APK](https://safemed.bridgeaiworks.com/downloads/android-install-guide/assets/step-02-apk.svg)

## 3. 允許此來源安裝

第一次安裝時，Android 可能顯示：

```text
為了安全性，您的手機目前不得安裝這個來源的未知應用程式
```

請依手機畫面前往設定，開啟「允許此來源」。

不同手機文字可能略有不同，例如：

- 安裝未知 App
- 未知來源
- 允許來自此來源
- Install unknown apps
- Allow from this source

只需要對你剛剛使用的瀏覽器開啟，例如 Chrome、Samsung Internet 或手機內建瀏覽器。

![允許此來源安裝](https://safemed.bridgeaiworks.com/downloads/android-install-guide/assets/step-03-allow.svg)

## 4. 返回並按「安裝」

開啟允許後，請回到剛剛的下載畫面或通知列，重新點選 APK。看到「是否要安裝此應用程式？」時，按下「安裝」。

如果找不到下載檔，可打開手機的「檔案」或「下載」App，點選剛下載的 APK。

![安裝安心藥盒 APK](https://safemed.bridgeaiworks.com/downloads/android-install-guide/assets/step-04-install.svg)

## 5. 第一次開啟與權限

第一次打開安心藥盒時，手機可能詢問通知、相機等權限。

- 若你要使用用藥提醒，請允許通知。
- 若要拍藥袋或掃 QR，請允許相機。
- 若一開始按了拒絕，也可以稍後到 Android「設定」中的 App 權限重新開啟。

![第一次開啟與權限](https://safemed.bridgeaiworks.com/downloads/android-install-guide/assets/step-05-permissions.svg)

## 6. 日後如何更新

有新版時，請回到官方下載頁，再下載最新 APK。下載後直接安裝新版，系統會覆蓋舊版。

請不要先解除安裝舊版。解除安裝通常會刪掉手機內的 App 資料，可能造成用藥清單、提醒、健康紀錄或設定消失。

![日後更新 Android APK](https://safemed.bridgeaiworks.com/downloads/android-install-guide/assets/step-06-update.svg)

## 常見問題

### 手機說「不支援此應用程式」或「無法安裝」怎麼辦？

安心藥盒 Android 版目前需要 **Android 8.0 以上**。請到手機「設定」→「關於手機」或「軟體資訊」確認 Android 版本。

如果 Android 版本已經是 8.0 以上，請再檢查以下項目：

- 確認下載的是 `.apk`，不是 GitHub 的 `Source code` 壓縮檔。
- 確認手機儲存空間足夠，至少先保留 300 MB 以上可用空間。
- 若手機是公司、學校或家長監護管理裝置，可能被管理政策禁止安裝 APK。
- 若已安裝過不同來源或不同簽章的測試版，請先備份重要資料，再聯絡支援，不要自行解除安裝。
- 若 Play Protect 或手機安全中心攔截，請只在確認來源是官方網站與官方 GitHub Release 時才繼續。

### 手機說「應用程式未安裝」怎麼辦？

這通常不是單一原因。最常見是下載檔不完整、手機空間不足、Android 版本太舊，或手機已經裝過不同簽章的舊測試版。請重新從官方 GitHub Release 下載一次 APK，確認空間足夠後再安裝。

如果仍然失敗，請截圖錯誤訊息，並附上手機型號、Android 版本與 APK 檔名，寄到支援信箱。

### 手機說「無法開啟檔案」怎麼辦？

請確認下載的是 `.apk` 檔案，不是 `.zip` 或 `.tar.gz`。若檔名不是 APK，請回 GitHub Release 的 Assets 重新下載。

### 手機說「為了安全性已封鎖」怎麼辦？

請依手機畫面前往設定，對目前使用的瀏覽器開啟「允許此來源」。安裝完成後，如果你不常安裝 APK，也可以回到設定把這個允許關掉。

### 更新後資料會不見嗎？

正常覆蓋安裝不應該刪除 App 資料。請不要先解除安裝舊版；解除安裝通常會刪掉手機內的 App 資料。

### 可以從朋友傳來的 APK 安裝嗎？

不建議。請從官方網站或官方 GitHub Release 下載，避免拿到被改過的檔案。

## 重要提醒

安心藥盒是用藥安全提醒與照護參考工具，不能取代醫師、藥師或正式醫療判斷。若有嚴重不適、異常數值或用藥疑問，請詢問醫師或藥師。
