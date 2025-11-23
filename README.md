# Cat_Guard_antivitus_free_and_opensource

# 🐾 CatGuard Antivirus (Beta)
CatGuard is a lightweight, open-source antivirus scanner designed for fast directory scanning, hash-based malware detection, and simple threat removal.  
This project is currently in **beta** and under active development.

---

## ✨ Features
- 🔍 **Directory scanning** with recursive file discovery  
- 🔐 **Multi-hash calculation** (SHA-256, SHA-1, MD5)  
- 🗂 **Local threat database** (hash-based detection)  
- 🌐 **MalwareBazaar API integration** for reputation checking  
- ⚠️ **Threat detection counter** displayed in UI  
- 🗑 **Simple threat removal**  
- 🎨 **PyQt5 GUI** – clean and beginner-friendly interface  

---

## 🚧 Beta Limitations
This is an early version. Some components are intentionally simplistic and will be improved in future releases:

- No multithreading (large scans may freeze the UI)
- No quarantine system (files are deleted directly)
- Local hash database is minimal
- No heuristic or behavioral detection
- No auto-updates for threat definitions

---

## 🛠 Planned Features (Roadmap)
CatGuard will evolve into a more robust antivirus engine over time:

### **1.1 — Performance Update**
- Multithreaded scanning  
- Progress bar & improved UI responsiveness  
- File exclusions  

### **1.2 — Threat Intelligence Update**
- External JSON threat database  
- Auto-update mechanism  
- API result caching  

### **1.3 — Security Update**
- Quarantine system  
- Threat metadata viewer  
- Logging system  

### **2.0 — Full AV Core**
- YARA rules scanning  
- PE/ELF heuristics  
- Entropy & packer detection  
- Live system monitoring  

---

## 📦 Installation
Clone the repository:

```bash
git clone https://github.com/yourusername/catguard.git
cd catguard
