🔐 Python-Based Network Port Scanner
📌 Project Overview
The Python-Based Network Port Scanner is a simple cybersecurity tool developed for educational purposes. It scans a local system (localhost) to identify open TCP ports and the services running on them, helping understand basic concepts of networking, port scanning, and vulnerability assessment.
This project simulates the core functionality of professional tools like Nmap, while strictly following ethical scanning practices.

---

🎯 Objectives
• Understand how port scanning works
• Learn Python socket programming
• Identify open ports and exposed services
• Practice ethical cybersecurity principles

---

🚀 Features
• ✅ TCP port scanning
• ✅ Service detection for common ports (HTTP, HTTPS, SSH, etc.)
• ✅ Fast scanning using socket timeouts
• ✅ Scan duration calculation
• ✅ Graceful handling of user interruption (Ctrl + C)
• ✅ Restricted to localhost for ethical use

---

🛠️ Technologies Used
• Python 3
• Socket Programming
• Networking Fundamentals
• Cybersecurity Basics

---

🧠 How It Works

1. Attempts a TCP connection to selected ports on 127.0.0.1
2. If the connection succeeds, the port is marked OPEN
3. Maps open ports to their commonly associated services
4. Displays scan results with timestamps and duration

---

▶️ How to Run the Project
Prerequisites
• Python 3.8 or higher
Steps
python port_scanner.py
⚠️ Note: This scanner is restricted to localhost for safety.

---

📊 Sample Output
[+] Port 80 | Service: HTTP | Status: OPEN
[+] Port 443 | Service: HTTPS | Status: OPEN

---

⚠️ Ethical Disclaimer
This tool is developed strictly for educational purposes. Scanning systems without proper authorization is illegal and unethical. The scanner is intentionally restricted to localhost (127.0.0.1) to prevent misuse.

---

🧩 Future Enhancements
• Add UDP port scanning
• Accept command-line arguments
• Generate scan reports
• Multi-threaded scanning for performance
