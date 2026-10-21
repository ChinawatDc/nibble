# nibble (สรุปภาษาไทย)

**nibble** คือ skill สำหรับ AI coding agent ที่ช่วยให้อ่าน context น้อยลงโดยคุณภาพไม่ลด มี skill เดียว และเลือกโหมดให้อัตโนมัติ 3 โหมด: **code**, **docs**, **chat** (โหมด chat ยังเป็นแบบทดลอง)

## ติดตั้ง
คัดลอก `SKILL.md` และโฟลเดอร์ `modes/` ไปไว้ในโฟลเดอร์ skill ของ agent เช่น `.claude/skills/nibble/`, `.cursor/skills/nibble/`, `.codex/skills/nibble/` หรือ `.agents/skills/nibble/` (ดูคำสั่งใน [README.md](./README.md))

## Benchmark
**รอผล** v0.2.0 จะวัดผลกับชุดเทสใหม่ที่ล็อกแล้ว และล็อก sha ของ skill ก่อนรัน มีรอบทดลอง (pilot) ก่อนหน้านี้อยู่ใน [bench/RESULTS.md](./bench/RESULTS.md) แต่นำไปอ้างอิงไม่ได้

## ข้อควรรู้
- v0.2.0 ยังไม่ได้ทดสอบ ยังไม่มีตัวเลขที่อ้างอิงได้
- โหมด chat ยังเป็นแบบทดลอง ยังไม่แนะนำให้ใช้
