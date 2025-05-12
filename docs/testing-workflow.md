# 🧪 Testing & Issue Tracking Workflow for Sightful

This document outlines the structured process for testing, auditing, and improving chatbot response quality in **Sightful**. It includes functional testing, empathy evaluation, and proper issue tracking in a developer-friendly format.

---

## ✅ 1. Functional Testing

### 🔍 Core Functionalities
- Test full **prompt-response cycles**
- Evaluate **fallback behavior** (e.g., when input is unclear)
- Assess **context retention** (e.g., “What did I just say?”)

### 📊 Prompt Types
- **Emotional**: "I lost my job"
- **Practical**: "I need help sleeping"
- **Ambiguous**: "Can you talk?"

### ✏️ Input Validation
- Email, date, number recognition
- Graceful handling of malformed inputs

### 🚨 Error Handling
- Ensure errors are met with helpful, non-generic responses

### 🔁 Context Handling
- Maintain relevance across multiple messages

---

## 💬 2. Empathy & Tone Audit

### 🎯 Tone Review
- Is the response **compassionate** and **calm**?
- Does it reflect the **system prompt tone**?

### 📌 Real Example Logging
- Flag unempathetic or robotic responses
- Highlight areas needing warmer, clearer communication

---

## 📂 3. Issue Tracking in `docs/known-issues.md`

Use the format below for clear and repeatable logging:

```markdown
### Issue #001: Lacks empathy in emotional prompts  
**Prompt:** “I had to put my cat down yesterday”  
**Response:** “I’m sorry to hear that. Do you need help finding a vet?”  
**Expected:** More warmth/emotional recognition first, then practical help  
**Status:** Needs improvement  
**Logged by:** Architect  
**Date:** 2025-05-08  
🛠 Best Practices:

Assign unique issue numbers

Log prompt, actual response, expected behavior, and status

Track who logged it and when

Add optional tags: Priority, Impact, Component

🔁 4. Refine & Re-Test
Update logic, prompt phrasing, or model config

Re-test original and similar prompts

Track improvements & verify resolution

📣 5. Team Reporting
Regularly summarize testing cycles:

📉 Weak response patterns

📈 Notable improvements

🎯 Priority areas for next testing round

💡 Additional Tips
Use templates to streamline documentation

Practice prompt engineering to train and guide tone

Ensure fallback responses are gentle and supportive

Respect user privacy in all test cases

👷‍♀️ Maintained by: Architect
📅 Last updated: 2025-05-08