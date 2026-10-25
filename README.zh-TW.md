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

## 安裝為 Agent Skill

Endorse 採用標準 **Agent Skills** 目錄結構：以 `endorse` 為資料夾名稱，裡面放一份具有 YAML frontmatter 的 `SKILL.md`。不需安裝腳本、相依套件、API Key 或外部服務。

下載 Release 裡的 `endorse-v1.0.0.zip`，或自行將 [SKILL.md](SKILL.md) 放進 `endorse/` 資料夾。請把**整個 Skill 資料夾**放到 AI Agent 支援的 Skills 目錄，而非安裝 README。

```text
endorse/
└── SKILL.md
```

**常見的 Skills 安裝位置：**

| Agent | 個人 Skills | 工作目錄／儲存庫 Skills |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/endorse/SKILL.md` | `.claude/skills/endorse/SKILL.md` |
| Codex（CLI／IDE） | `~/.agents/skills/endorse/SKILL.md` | `.agents/skills/endorse/SKILL.md` |
| 其他支援 Agent Skills 的工具 | 依該 Agent 官方文件指定的位置 | 依該 Agent 官方文件指定的位置 |

如果 Agent 提供 Skill installer，也可依其支援的方式指定 GitHub 儲存庫或 Skill 目錄完成安裝。安裝後，可使用 Agent 的 Skill 選擇器或明確呼叫（例如 Claude Code 的 `/endorse`、Codex 的 `$endorse`），也能直接描述需求讓 Agent 依 Skill description 判斷是否套用。能否自動啟用取決於所用工具。

更新時，替換已安裝的 `endorse/SKILL.md` 即可；若 Agent 未偵測到變更，重新啟動後再試。

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
