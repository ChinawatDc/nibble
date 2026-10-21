# nibble (สรุปภาษาไทย)

[![skills.sh](https://skills.sh/b/ChinawatDc/nibble)](https://skills.sh/ChinawatDc/nibble)

**nibble** คือ skill สำหรับ AI coding agent ที่ช่วยให้อ่าน context น้อยลงโดยคุณภาพไม่ลด มี skill เดียว และเลือกโหมดให้อัตโนมัติ 3 โหมด: **Code**, **Docs**, **Chat**

---

## ติดตั้งแบบ 1 คำสั่ง (ผ่าน skills.sh)
```bash
# ติดตั้งให้ทุก agent (*: Claude Code, Cursor, Codex, Gemini)
npx skills add ChinawatDc/nibble -a '*'

# หรือเลือกเฉพาะตัวที่ใช้
npx skills add ChinawatDc/nibble -a claude-code
npx skills add ChinawatDc/nibble -a cursor
```

หรือคัดลอกไฟล์ `SKILL.md` และโฟลเดอร์ `modes/` ไปไว้ในโฟลเดอร์ skill ของ agent เช่น `.claude/skills/nibble/`, `.cursor/skills/nibble/`, `.codex/skills/nibble/` หรือ `.agents/skills/nibble/` (ดูคำสั่งใน [README.md](./README.md))

---

## ผลการทดสอบ (Benchmark)

| โหมด | Token ที่ลดลง (Median) | คุณภาพคำตอบ | สถานะ |
|---|---|---|---|
| **Code Mode** (`c01–c05`) | **−44.6%** | ผ่าน 100% (ผ่าน trap ตรวจโค้ดข้ามไฟล์ทั้งหมด) | **พร้อมใช้งานจริง** |
| **Docs Mode (ค้นหาทั่วไป)** (`d01–d03`) | **−32.8%** | ผ่าน 100% | **พร้อมใช้งานจริง** |
| **Docs Mode (Trap ข้ามเอกสาร)** (`d04, d05`) | **+7.6% ถึง +18.5%** | ผ่าน 100% (*Cost of Correctness*) | **ยอมรับเพื่อความถูกต้อง** |
| **Chat Mode** (`h01–h05`) | **−24.8%** | ผ่าน 100% (v0.2 ทดสอบจริง ลดลง 50.9% จาก v0.1) | **พร้อมใช้งานจริง** |

---

## จุดเด่นสำคัญ
- **Short-Thread Bypass:** แชทสั้น (< 20 turns) ตอบคำถามทันทีโดยไม่มี Token Overhead
- **Quality Over Cost:** หากบริบทไม่พอ Agent จะยอมอ่านเพิ่มเสมอ ความถูกต้องของงานต้องมาก่อนการประหยัด Token
- **Single-Shot Exemption:** ไฟล์ขนาดเล็ก (< 150 บรรทัด) ให้อ่านครั้งเดียวจบ ป้องกัน Tool-call fragmentation
