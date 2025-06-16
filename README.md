# 🔐 Log Event Extractor

A Python script to extract `login` and `logout` events from multiple `.log` files based on **serial numbers**. Organizes the output neatly into folders per serial number with timestamped results and event counts.

---

## 📂 Features

- ✅ Scans multiple `.log` files for `login` and `logout` events
- 🔍 Uses regular expressions to identify events by timestamp and serial number
- 🗂️ Creates structured output folders for each serial
- 📝 Outputs include matched lines and total event count per file
- 🧾 Supports multiple serial numbers and event types

---

## 📁 Input Files

Supports any `.log` files. Example list:
- `NEUF-DWS-Core.81.log`
- `NEUF-DWS-Core.83.log`
- `NEUF-DWS-jQuery-UI.main.49.log`
- `NEUF-DWS-jQuery-UI.main.50.log`
- `NEUF-HPOmniWeb-Bundle.main.229.log`
- `NEUF-HPOmniWeb-Bundle.main.224.log`
- `NEUF-Impl-Bundle.145.log`
- `NEUF-Impl-Bundle.149.log`

---

## 📤 Output Structure

