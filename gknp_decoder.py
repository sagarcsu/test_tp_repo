#!/usr/bin/env python3
"""
GKNP 1.0 Decoder – Works with encoder above
"""

import json

DICTIONARY = {0: "I want to", 1: "Show me", 2: "Create a", 3: "Open url", 4: "Navigate to",
              5: "Play", 6: "Turn on", 7: "Turn off", 8: "Set", 9: "Reboot", 10: "Ping",
              11: "Curl", 12: "SSH to", 13: "Speedtest", 14: "Traceroute", 15: "Nslookup",
              # ... same full 100 entries as encoder (copy from above) ...
              90: "Save", 91: "Load", 92: "Backup", 93: "Restore", 94: "Update",
              95: "Upgrade", 96: "Install", 97: "Uninstall", 98: "Run", 99: "Execute"}

def gknp_decode(packet: dict) -> str:
    if "code" in packet:
        code = packet["code"]
        phrase = DICTIONARY.get(code, "[UNKNOWN]")
        args = packet.get("args", [])
        return (phrase + " " + " ".join(args)).strip()
    elif "fallback" in packet:
        hex_str = "".join(f"{(d-1000)//100:x}" for d in packet["fallback"])
        return bytes.fromhex(hex_str).decode("utf-8")
    else:
        return "[INVALID PACKET]"

# ============ QUICK TEST ============
if __name__ == "__main__":
    from gknp_encoder import gknp_encode
    test = "I want to open url news.google.com"
    encoded = gknp_encode(test)
    decoded = gknp_decode(encoded)
    print("Original :", test)
    print("Decoded  :", decoded)
    print("Match?   :", test.lower() == decoded.lower())
