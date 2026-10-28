# Endorse

**有根據、有個人特色，也真正像你會寫的 LinkedIn 推薦文。**

**繁體中文（台灣）** · [English](README.md) · [Skill 完整規則](SKILL.md) · [下載版本](https://github.com/markleetw/endorse-skill/releases)

Endorse 是一份以 Markdown 編寫、不綁定特定 AI 平台的 Agent Skill。它從你親身經歷的合作與決策出發，只在關鍵資訊不足時追問，並在**第一次交稿前自行完成事實檢查與文字精修**。

你會拿到一篇**可供確認後發布的英文 LinkedIn 推薦文**、自然的繁體中文語意對照，以及簡短的編輯判斷。最終事實確認與是否發布，仍由推薦人決定。

## 為什麼用 Endorse？

- **具體，而不是堆疊形容詞：** 讓真實的行為、判斷和成果支持每個稱讚。
- **呈現你獨有的觀察：** 找出你與對方合作後，最有資格說出的專業洞察，而不是套用金句。
- **不誇大功勞：** 分清楚個人提案、主管核准、團隊執行與實際可證實的結果。
- **初稿就完成精修：** 先檢查事實與歸因，再重新審視整篇敘事；可以直接修正的問題，不留給你做第二輪。
- **少問，但問在重點上：** 只有缺少的資訊可能大幅改變推薦文，才補問關鍵問題。

## 快速開始

1. 從 [最新 Release](https://github.com/markleetw/endorse-skill/releases/latest) 下載 **`endorse.zip`**。
2. 依使用的平台安裝：

| 平台 | 安裝方式 |
| --- | --- |
| **ChatGPT**（符合資格的工作區） | **外掛程式 → 技能（Skills）→ 建立 → 從電腦上傳**。是否開放取決於方案與工作區設定。 |
| **Claude**（支援 Skills 的環境） | 開啟 Claude 設定中的 Skills 功能並上傳 Skill；介面名稱依版本及方案而異。 |
| **其他相容 Agent** | 依各平台的官方 Skills 安裝說明操作。 |

ChatGPT 的官方步驟請參考 [ChatGPT 中的技能](https://help.openai.com/zh-hant/articles/20001066-skills-in-chatgpt)。**把 ZIP 當作一般聊天附件上傳，不等於已正式安裝 Skill。**

3. 告訴 AI 要使用 Endorse。支援技能指令的平台也可以嘗試輸入 `/endorse`：

```text
/endorse 我要推薦以前帶過的 PM，請只問我必要的問題。
/endorse 我想寫一位工程主管的 LinkedIn 推薦文。
/endorse 請精修這篇推薦文，確認沒有誇大他的個人貢獻。
```

實際呼叫方式依平台而異。Endorse **不會自動登入或發布到 LinkedIn**。

## Endorse 如何運作

1. **釐清合作關係：** 你和對方的角色、合作經驗及第一手觀察。
2. **找出有證據的特色：** 避免只用能力標籤；必要時確認是否遺漏重要的管理或專業貢獻。
3. **選擇最有說服力的角度：** 在內部比較敘事方向，寫成連貫的人物形象。
4. **交稿前兩輪審稿：** 先檢查事實，再精修開頭、結尾、段落與重複內容。
5. **提供雙語結果：** 英文推薦文、忠實的繁中語意對照，以及簡短編輯說明。

完整執行規則請參考 [SKILL.md](SKILL.md)。

## 一個簡短的虛構例子

以下人物和公司完全是**虛構**的，僅示範怎麼從空泛稱讚找到可信的個人觀察，不是固定寫作模板。

**空泛的說法：**「Sam 是很厲害的 PM，也很會團隊合作。」

**更有價值的證據：**「團隊對一個探索功能還沒有共識時，Sam 同時考慮使用者回饋和工程限制，提出範圍較小的實驗，協助大家做出決策。優先順序由我審核，實驗由團隊共同完成。」

**可能寫成的英文片段：**

> What I appreciated about working with Sam was the way they made uncertain product decisions easier to discuss. When our team had no agreed solution for a discovery problem, Sam helped us compare user needs with engineering constraints and proposed a smaller experiment we could actually learn from.

這樣既呈現 Sam 的貢獻，也不會擅自宣稱實驗帶來多少成長、或整個功能都是 Sam 一個人完成的。

## 相容性與使用限制

Endorse 是純文字的 Agent Skill，不需要額外執行環境，也不會連接外部服務或自動發布內容。不同 AI 平台、模型、權限與對話脈絡，都可能影響實際效果。即使檔案格式正確，也不代表每個平台的輸出品質都相同。**發布前請由推薦人確認內容正確。**

## 品質驗證與隱私

本專案提供[虛構案例回歸測試](evals/README.md)與[評分規準](evals/rubric.md)，檢查事實、成果歸因、人物辨識度、管理職責、文字精修與翻譯一致性。這些測試素材**不代表目前已完成跨模型驗證**。

請勿在公開 Issue、PR 或 Commit 中張貼真實同事的績效資訊、未公開專案或可識別個人身分的推薦文。

## 參與貢獻與版本

- [貢獻指南（英文）](CONTRIBUTING.md) · [安全性回報（英文）](SECURITY.md)
- [更新紀錄](CHANGELOG.md) · [GitHub Releases](https://github.com/markleetw/endorse-skill/releases)
- **Release ZIP** 是固定版本；**`main`** 是持續開發版本，內容可能比最新 ZIP 新。
- **目前正式發布：** [v1.0.1](https://github.com/markleetw/endorse-skill/releases/tag/v1.0.1)。v1.1.0 規劃中，**尚未發布**。

## 授權

本專案尚未選定開源授權條款。GitHub 公開可見不等於允許任意修改、重製、散布或再授權；在授權確定前，仍適用既有著作權限制。
