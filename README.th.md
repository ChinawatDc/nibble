# nibble (สรุปภาษาไทย)

[![skills.sh](https://skills.sh/b/ChinawatDc/nibble)](https://skills.sh/ChinawatDc/nibble)

**nibble** คือ skill สำหรับ AI coding agent ที่ช่วยให้อ่าน context น้อยลงโดยคุณภาพไม่ลด มี skill เดียว และเลือกโหมดให้อัตโนมัติ 3 โหมด: **Code**, **Docs**, **Chat**

**ที่อยู่ skill ใน repo:** [`skills/nibble/`](./skills/nibble/) (`SKILL.md` + `modes/`)

---

## ติดตั้งแบบ 1 คำสั่ง (ผ่าน skills.sh)

```bash
npx skills add ChinawatDc/nibble -a '*'
npx skills add ChinawatDc/nibble -a claude-code
npx skills add ChinawatDc/nibble -a cursor
```

หรือคัดลอกแพ็กเกจด้วยมือ:

```bash
mkdir -p .cursor/skills/nibble
cp skills/nibble/SKILL.md .cursor/skills/nibble/
cp -R skills/nibble/modes .cursor/skills/nibble/
```

(เปลี่ยน `.cursor` เป็น `.claude` / `.codex` / `.agents` ตาม agent ที่ใช้ — ดู [README.md](./README.md))

---

## จุดเด่นสำคัญ

- **Short-Thread Bypass:** แชทสั้น (< 20 turns) ตอบทันทีโดยไม่โหลดกฎ chat หนัก
- **Quality Over Cost:** ถ้าบริบทไม่พอ ยอมอ่านเพิ่ม ความถูกต้องมาก่อนประหยัด token
- **Single-Shot Exemption:** ไฟล์เล็ก (< 150 บรรทัด) อ่านครั้งเดียวจบ

---

## Benchmark

ชุด fixture หนักอยู่ใน branch [`bench/pilot-v1`](https://github.com/ChinawatDc/nibble/tree/bench/pilot-v1) ไม่ได้อยู่บน `main` เพื่อให้หน้า skills.sh และ `npx skills add` เบาและแสดง `SKILL.md` ได้ครบ
