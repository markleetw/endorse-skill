# Endorse

**有根據、有個人特色的 LinkedIn 推薦文。**

**繁體中文** · [English](README.md) · [Skill 完整規則](SKILL.md) · [v1.0 發布說明](RELEASE_NOTES.md)

Endorse 是一份不綁定特定 AI 平台的 Agent Skill，協助你寫出可信、有辨識度且自然的 LinkedIn 推薦文。它只在關鍵資訊不足時進行訪談，從推薦人的親身觀察找出值得強調的能力，並在**第一次交稿前自行完成審稿與精修**。

最終交付包含**可直接發布的英文推薦文**、**繁體中文語意對照**，以及簡短的編輯判斷。

## Endorse 的特色

- **具體而不空泛：** 用真實觀察、決策與個人貢獻證明能力，不只是堆疊形容詞。
- **不套用制式開頭：** 不預設從「I worked with…」或「I managed…」開始，而是優先呈現人物特有的觀察。
- **有洞察力的結尾：** 呈現推薦人為何信任或欣賞對方，避免在結尾重複列出優點。
- **準確區分貢獻與成果：** 不把團隊產出寫成個人功勞，也不編造業務指標與成效。
- **內建兩輪審稿：** 先審查事實與歸因，再精修敘事、語氣、結構及精簡度；不必另外提醒 AI「review / refine」。

## 安裝方式

Endorse **只是一份 Markdown Skill，不是可執行的軟體**，不需要 API Key、套件管理工具或外部整合。實際安裝方式依 AI 助理而異。

### 方式 A：ChatGPT 專案

1. 下載 [SKILL.md](SKILL.md)，或取得 [v1.0 安裝包](https://github.com/markleetw/endorse-skill/releases)。
2. 開啟你想用來撰寫推薦文的 ChatGPT 專案。
3. 把 `SKILL.md` 加入專案的「參考資料／檔案」。
4. 在**該專案內開新對話**，輸入：「我要寫一篇 LinkedIn 推薦文，請依照專案參考資料的 SKILL.md 執行。」

這是透過 ChatGPT 專案參考檔案提供指示，**不代表安裝原生 ChatGPT 工具，也無法保證每次都自動執行**。後續更新 Skill 時，記得替換專案裡的舊檔案。

### 方式 B：支援 Agent Skills 的 AI 助理

將 `SKILL.md` 放到你的 AI 助理支援的 Skill 目錄，例如：

```text
<你的 Agent Skills 目錄>/
  endorse/
    SKILL.md
```

再依該平台的規則啟用或呼叫 Endorse。各平台的目錄、安裝方式及自動載入機制可能不同，請以各平台文件為準。

### 方式 C：一般 AI 聊天／自訂指示

直接貼上 [SKILL.md](SKILL.md) 的內容，或將檔案附在聊天中，明確告訴 AI 按照其規則執行即可。不同模型對長篇指示的遵循程度可能不同。

## 使用方式

直接用**中文或英文**描述需求即可，不必先填問卷。

**中文範例：**

> 我要寫一篇前同事的 LinkedIn 推薦文。他擅長處理複雜的產品決策，也會主動協助其他同事。請依照 SKILL.md 訪談我，只問必要的問題，完成審稿後再交稿。

**English example:**

> Help me write a LinkedIn recommendation for a former colleague. I was their manager. They handled difficult trade-offs across product, business, and operations. Interview me for any essential details, then draft and refine the recommendation.

Endorse 只會在影響真實性或人物特色時提出必要問題。資訊足夠後，它會自行完成草稿、審稿與精修，交付：

1. **English | LinkedIn Recommendation**：可複製到 LinkedIn 的英文正式版。
2. **繁體中文｜語意對照**：完整保留英文版本的事實、語氣與不確定性。
3. **Editorial judgment**：簡要說明核心定位，以及是否仍有事實待確認。

發布前，仍應由推薦人確認涉及人物與經歷的事實準確無誤。

## 寫作原則

**證據優先於形容詞；個人特色優先於模板；專業判斷優先於一味附和。**

開頭不靠公式，正文展現當事人**實際做了什麼、為什麼重要**，結尾則提煉推薦人特有的觀察。內容的資訊密度與可信度，優先於固定字數。

Endorse 不會虛構成就、指標、個人動機、獨自負責的範圍或業務成效，也會將內部專案轉換成外部讀者能理解的脈絡。

## 適用範圍與隱私

**包含：** LinkedIn 書面推薦文、適應式訪談、事實與敘事審稿、英文推薦文及繁體中文對照。

**不包含：** LinkedIn 技能背書點選、正式推薦信、背景查核、LinkedIn 自動發布、外部研究或第三方整合。

未經當事人同意，請勿將未公開的推薦文或可識別個人身分的案例提交到公開 Issue、Commit 或示範文件。這份公開儲存庫**不包含真實人物的推薦文案例**。

## 版本與下載

- **版本：** v1.0.0（首個正式穩定版本）
- **正式規則：** [SKILL.md](SKILL.md)
- **安裝包：** `endorse-v1.0.0.zip`，包含 Skill 與中英雙語文件
- **更新摘要：** [發布說明](RELEASE_NOTES.md)

## 授權

本儲存庫目前未提供開放原始碼授權條款。公開可見不代表允許任意修改、重新散布或再授權；若需要超出 GitHub 平台條款所允許的使用權限，請聯繫儲存庫擁有者。
