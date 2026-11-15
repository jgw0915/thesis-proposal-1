# 最終 PowerPoint 原生公式轉換規範

**採用日期：2026-11-16｜高優先度**。此規範覆蓋「必須先在 Canva 使用 LaTeX Math 外掛」的舊決定，但不改變單一 Canva 主簡報、繁體中文或來源標示規則。

## 核心決策
- **最終發表檔是 Microsoft PowerPoint（.pptx）**，Canva 是視覺設計與持續編輯的主工作區。
- 正式數學方程式最終須盡可能轉換成 **PowerPoint 原生可編輯的 Office Math（OMML）物件**，而非僅是 Canva LaTeX Math 產生的圖片。
- Canva 的 LaTeX Math 外掛仍可**選擇性**用於 Canva 階段的排版預覽，但**不是必要前置作業**，不得讓外掛輸出圖片阻礙最終 OMML 編輯性。
- 在 Canva 草稿階段，可保留合理的數學佔位符；所有需要轉換的公式必須建立**逐頁 LaTeX 原始碼清單**，包括頁碼、原公式文字、章節來源、符號定義及畫面位置。依最新私有論文 `Master-Thesis` 查核，嚴禁杜撰公式。
- LaTeX 原始碼清單應由目前工作會話的私有交付物或私有 repo 保存，**不可將未公開論文方程式與 Canva 私人編輯連結推入公開的簡報 repo**。

## 操作流程
1. 在唯一的 Canva 主簡報中，依五頁一批產生、檢查並加入投影片。保留使用者已修改的版面。
2. 一邊製作一邊編制公式 manifest；標註哪些是真正的數學公式，哪些只是普通標籤，避免不必要地把每個字母都轉為公式。
3. Canva 完稿後由使用者**匯出 PPTX**，並上傳匯出的 PPTX 到 ChatGPT；這份匯出檔是後製來源。
4. 以 PowerPoint 的原生 Office Math（OMML）取代相應佔位符／圖片，在可能範圍內保持字型、尺寸、位置、配色；保留投影片其他 editable shapes 與 presenter notes。
5. **驗證**：每個公式的符號、上下標、分數、求和、範圍、字型與位置要和論文一致；檢查 XML 是否真的包含 PowerPoint 可編輯的數學結構，而非只是 PNG/SVG 圖片，並在桌面版 PowerPoint 實際開啟試改至少一式。
6. 若某個公式的 LaTeX 無法可靠轉換為 Office Math，須明確列出限制與人工修復步驟，不能宣稱全數成功。
7. 最終交付 PPTX，並以 PDF 預覽檢查無裁切、重疊、破字；此 PDF 只是備份，PPTX 才是發表主檔。

## 注意事項
- Word/PowerPoint 方程式支援的是 Office Math 結構，**不能假設 Canva 的 LaTeX Math 元件匯出後會自動變成原生方程式**。
- 方程式在 Canva 可採易讀的文字佔位或可選的外掛顯示，**最終原生公式轉換安排在 Canva→PPTX 之後**。
- PowerPoint 的部分版本/平台及個別 LaTeX 指令相容性可能不同，最後應以使用者的桌面版 PowerPoint 驗收。
- 新增批次時，任何特殊數學記號的工作紀錄應寫「LaTeX source prepared / pending final PPTX conversion」，除非已真正在 PowerPoint 完成並驗證。
- Canva 主簡報不得每批另起正式專案。若 Canva API 只能匯入中介設計，可以短暫建立中介設計再將頁面併入**同一份主簡報**，並逐頁確認順序。
