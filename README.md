<h2>🔐 Python-Based Network Port Scanner</h2>

<h3>📌 Project Overview</h3>
The Python-Based Network Port Scanner is a simple cybersecurity tool developed for educational purposes. It scans a local system (localhost) to identify open TCP ports and the services running on them, helping understand basic concepts of networking, port scanning, and vulnerability assessment.
This project simulates the core functionality of professional tools like Nmap, while strictly following ethical scanning practices.


<h3>🎯 Objectives</h3>
• Understand how port scanning works
• Learn Python socket programming
• Identify open ports and exposed services
• Practice ethical cybersecurity principles


<h3>🚀 Features</h3>
• ✅ TCP port scanning
• ✅ Service detection for common ports (HTTP, HTTPS, SSH, etc.)
• ✅ Fast scanning using socket timeouts
• ✅ Scan duration calculation
• ✅ Graceful handling of user interruption (Ctrl + C)
• ✅ Restricted to localhost for ethical use


<h3>🛠️ Technologies Used</h3>
• Python 3
• Socket Programming
• Networking Fundamentals
• Cybersecurity Basics


<h3>🧠 How It Works</h3>
1. Attempts a TCP connection to selected ports on 127.0.0.1
2. If the connection succeeds, the port is marked OPEN
3. Maps open ports to their commonly associated services
4. Displays scan results with timestamps and duration


<h3>▶️ How to Run the Project</h3>
<h4>Prerequisites</h4>
• Python 3.8 or higher
Steps
python port_scanner.py
⚠️ Note: This scanner is restricted to localhost for safety.


<h3>📊 Sample Output</h3>
[+] Port 80 | Service: HTTP | Status: OPEN
[+] Port 443 | Service: HTTPS | Status: OPEN

<h3>⚠️ Ethical Disclaimer</h3>
This tool is developed strictly for educational purposes. Scanning systems without proper authorization is illegal and unethical. The scanner is intentionally restricted to localhost (127.0.0.1) to prevent misuse.

<h3>🧩 Future Enhancements</h3>
• Add UDP port scanning
• Accept command-line arguments
• Generate scan reports
• Multi-threaded scanning for performance
