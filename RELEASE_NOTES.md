# Endorse — Release Notes / 發布說明

For unreleased development changes, see [CHANGELOG.md](CHANGELOG.md). Published release notes below describe historical snapshots; installation details may have changed. / 開發中改動請見 [更新紀錄](CHANGELOG.md)；以下是歷史版本說明，安裝方式可能已更新。

## v1.0.1 — 2026-10-25

**English:** Documentation-only update. Simplified installation and usage instructions to match the RDD Skill: download `endorse.zip` from Releases; install through ChatGPT or Claude's Skills UI; invoke Endorse with a short request. Removed manual directory-path instructions. **SKILL.md is unchanged.**

**繁體中文：** 僅更新文件。參考 RDD Skill，將安裝方式簡化為「下載 `endorse.zip` → 在 ChatGPT 或 Claude 安裝」，並提供簡短使用範例；移除手動設定資料夾路徑的說明。**SKILL.md 內容不變。**

---

## v1.0.0 — 2026-10-25

**First stable release / 首個正式版本。**


## English

The first stable version of **Endorse**: a Markdown-based, platform-independent AI Agent Skill for credible and distinctive LinkedIn recommendations.

### Highlights
- **Evidence-led interviewing:** Focused follow-up questions only when missing information materially affects accuracy or differentiation.
- **Person-specific writing:** Strong openings that avoid repetitive tenure-first introductions; concrete examples that demonstrate individual contributions.
- **Earned conclusions:** Manager- or colleague-specific insights rather than generic praise or a recap of traits.
- **Two mandatory editorial passes:** Evidence/attribution verification, then narrative refinement, before the first draft is delivered.
- **Careful calibration:** No invented metrics, results, motivations, or sole ownership of team work.
- **Bilingual delivery:** Natural English recommendations paired with faithful Traditional Chinese semantic translations.
- **Standard Agent Skill installation:** Place the `endorse/` folder in a supported agent's skills directory (e.g., Claude Code or Codex).

### Package contents
```text
endorse/
├── SKILL.md
├── README.md
├── README.zh-TW.md
└── RELEASE_NOTES.md
```

### Install
See [README.md](https://github.com/markleetw/endorse-skill/blob/v1.0.0/README.md). Extract the archive, then install the `endorse/` folder in your agent's skills directory. Invoke the skill using that agent's standard skill selector or command.

### Compatibility
No runtime dependencies; instruction-following quality depends on the model and host platform. Endorse does not post directly to LinkedIn.

### Privacy and license
No real-person recommendation examples are included. No open-source license has been selected; default copyright restrictions remain.

---

## 繁體中文

**Endorse** 第一個穩定版本正式完成。這是一份不綁定平台的 Markdown Agent Skill，協助撰寫可信、有個人特色的 LinkedIn 推薦文。

### 主要功能
- **以證據為核心的訪談：** 僅在資訊不足以支持判斷、個人貢獻或成果時追問。
- **不套公式的敘事：** 開頭優先呈現人物特質，以具體案例證明貢獻，避免制式年資開場。
- **有洞察力的結尾：** 從主管或同事的親身經驗提煉真正值得記住的觀察。
- **交稿前強制兩輪審稿：** 先檢查證據與成果歸因，再精修文字與敘事；第一次交稿就應完成。
- **避免誇大：** 不捏造指標、商業成果、動機，也不把團隊貢獻歸為個人獨有。
- **雙語交付：** 自然英文推薦文搭配忠實的繁體中文語意對照。
- **標準 Agent Skill 安裝：** 將 `endorse/` 資料夾放進支援 Skills 的 Agent 目錄，例如 Claude Code 或 Codex。

### 安裝與使用
請參考 [繁體中文 README](https://github.com/markleetw/endorse-skill/blob/v1.0.0/README.zh-TW.md)。解壓縮安裝包後，將 `endorse/` 資料夾放到 Agent 支援的 Skills 目錄，並透過該 Agent 的 Skill 選擇器或指令呼叫。

### 相容性
不需執行環境或外部依賴；實際品質取決於所用模型與平台。Endorse 不會自動發布 LinkedIn 內容。

### 隱私與授權
安裝包不包含真實人物推薦文範例。目前尚未選定開放原始碼授權條款，一般著作權限制仍適用。
