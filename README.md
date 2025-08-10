<h1 align="center">ðŸŒŸ Wishing Code in Python ðŸŒŸ</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" />
  <img src="https://img.shields.io/badge/Category-Automation-4CAF50?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Speech-TTS-FF5722?style=for-the-badge" />
</p>

---

## ðŸ“œ Project â€” Wishing Code in Python
**Wishing Code in Python** (`Wishing-code-Python`) is a personal creative project â€” a lightweight script that greets the user based on the current system time and speaks the greeting using an offline Text-to-Speech engine (`pyttsx3`).  
Itâ€™s perfect for practising **conditional logic**, **time handling**, and **simple automation** in Python.

---

## ðŸ“‚ File structure
- `wisher.py` â€” Main Python script (detects time, prints & speaks greeting)  
- `README.md` â€” Project documentation

---

## âš™ï¸ Features
- Reads current system date and time (Python `time` module).  
- Chooses greeting by hour ranges:
  - 00:00â€“05:59 â†’ Early Morning
  - 06:00â€“11:59 â†’ Morning
  - 12:00â€“15:59 â†’ Afternoon
  - 16:00â€“20:59 â†’ Evening
  - 21:00â€“23:59 â†’ Night  
- Speaks greetings using `pyttsx3` (offline, cross-platform).  
- Prints a human-readable date and time stamp.

---

## ðŸš€ Quick start
1. Ensure you have **Python 3.x** installed on your system.  
2. Install dependency:  
   `pip install pyttsx3`  
3. Place `wisher.py` in your desired folder.  
4. Run the script:  
   `python wisher.py`  
Youâ€™ll see the printed date/time and hear the spoken greeting.

---

## ðŸ›  Notes & troubleshooting
- If you hear no voice on Windows: check system audio settings and ensure an installed TTS voice is available.  
- If `pyttsx3` installation fails: try `python -m pip install --upgrade pip` and reinstall.  
- Change timestamp format by editing the `time.strftime` calls in `wisher.py`. For example:  
  `'%I:%M:%S %p'` â†’ 12-hour format with AM/PM  
  `'%H:%M:%S'` â†’ 24-hour format  
- You can test different greetings by manually setting the `hour` variable.

---

## âœ¨ Customization ideas
- Save each greeting with timestamp to a log file.  
- Play a custom sound along with the spoken greeting.  
- Add command-line flags to choose greeting type.  
- Convert it into a desktop app using `tkinter` or bundle with `pyinstaller`.

---

<h2 align="center">ðŸ‘¨â€ðŸ’» Author</h2>

<p align="center">
  <img src="https://img.shields.io/badge/GitHub-Aaryan--Kumar-181717?style=for-the-badge&logo=github" />
  <img src="https://img.shields.io/badge/LinkedIn-Aaryan--Kumar-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
</p>

---
