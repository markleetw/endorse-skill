# Endorse v1.0.0 — Release Notes / 發布說明

**Release date / 發布日期:** 2026-10-25

## English

The first stable version of **Endorse**: a Markdown-based, platform-independent AI Agent Skill for credible and distinctive LinkedIn recommendations.

### Highlights
- **Evidence-led interviewing:** Focused follow-up questions only when missing information materially affects accuracy or differentiation.
- **Person-specific writing:** Strong openings that avoid repetitive tenure-first introductions; concrete examples that demonstrate individual contributions.
- **Earned conclusions:** Manager- or colleague-specific insights rather than generic praise or a recap of traits.
- **Two mandatory editorial passes:** Evidence/attribution verification, then narrative refinement, before the first draft is delivered.
- **Careful calibration:** No invented metrics, results, motivations, or sole ownership of team work.
- **Bilingual delivery:** Natural English recommendations paired with faithful Traditional Chinese semantic translations.
- **Portable installation:** ChatGPT Project reference files, agent-skill directories, or ordinary custom instructions.

### Package contents
```text
endorse/
├── SKILL.md
├── README.md
├── README.zh-TW.md
└── RELEASE_NOTES.md
```

### Install
See [README.md](README.md#install). For ChatGPT Projects, add `SKILL.md` to the project's reference files and request that the assistant follow it.

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
- **可攜式安裝：** 支援透過 ChatGPT 專案參考檔案、Agent Skills 目錄或一般自訂指示使用。

### 安裝與使用
請參考 [繁體中文 README](README.zh-TW.md#安裝方式)。ChatGPT 使用者可將 `SKILL.md` 加入專案參考資料，再於專案內請 AI 依該檔案撰寫推薦文。

### 相容性
不需執行環境或外部依賴；實際品質取決於所用模型與平台。Endorse 不會自動發布 LinkedIn 內容。

### 隱私與授權
安裝包不包含真實人物推薦文範例。目前尚未選定開放原始碼授權條款，一般著作權限制仍適用。
