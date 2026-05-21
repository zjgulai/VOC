#!/usr/bin/env python3
"""批量移除HTML文件中的emoji表情符号，保留中文、英文和HTML标签"""
import re
import sys
from pathlib import Path

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001F9FF"  # Miscellaneous Symbols, Pictographs, Emoticons, etc
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002600-\U000027BF"  # Miscellaneous Symbols
    "\U0001F600-\U0001F64F"  # Emoticons
    "\U0001F680-\U0001F6FF"  # Transport and Map
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001F1E0-\U0001F1FF"  # Flags
    "\U00002B50"             # Star
    "\U00002764"             # Heart
    "\U00002705"             # Check mark
    "\U0000274C"             # Cross mark
    "\U000026A0"             # Warning
    "\U0000FE0F"             # Variation Selector-16
    "\U0000200D"             # Zero Width Joiner
    "\U00002694"             # Crossed swords
    "\U00002713"             # Check mark (text)
    "\U00002702"             # Scissors
    "\U000026A1"             # Lightning
    "\U00002600"             # Sun
    "\U00002728"             # Sparkles
    "\U0000274E"             # Cross mark boxed
    "\U00002753"             # Question mark ornament
    "\U0001F4A1"             # Lightbulb (missed by some ranges)
    "\U0001F4CA"             # Chart (missed)
    "\U0001F3AF"             # Dart
    "\U0001F3C6"             # Trophy
    "\U0001F49A"             # Green heart
    "\U0001F511"             # Key
    "\U0001F525"             # Fire
    "\U0001F48E"             # Gem
    "\U0001F4CB"             # Clipboard
    "\U0001F630"             # Anxious face
    "\U0001F624"             # Face with steam
    "\U0001F5FA"             # Map
    "\U0001F4E1"             # Satellite
    "\U0001F465"             # Busts in silhouette
    "\U0001F4C5"             # Calendar
    "\U0001F3DB"             # Classical building
    "\U0001F3F7"             # Label
    "\U0001F4A1"             # Light bulb
    "\U0001F680"             # Rocket
    "\U0001F4AA"             # Flexed biceps
    "\U0001F534"             # Red circle
    "\U0001F535"             # Blue circle
    "\U0001F4B0"             # Money bag
    "\U0001F4C8"             # Chart increasing
    "\U0001F31F"             # Glowing star
    "\U0001F310"             # Globe
    "\U0001F50D"             # Magnifying glass
    "\U0001F4AC"             # Speech balloon
    "\U0001F4D1"             # Bookmark tabs
    "\U0001F4CC"             # Pushpin
    "\U0001F3A8"             # Artist palette
    "\U0001F37C"             # Baby bottle
    "\U0001F4CF"             # Straight ruler
    "\U0001F532"             # Black square button
    "\U00002668"             # Hot springs
    "\U00002699"             # Gear
    "\U0001F3AC"             # Clapper board
    "\U0001F4D0"             # Triangular ruler
    "\U0001F524"             # Input latin letters
    "\U0001F504"             # Counterclockwise arrows
    "\U0001F6E1"             # Shield
    "\U0001F4E6"             # Package
    "\U0001F4D6"             # Open book
    "\U0001F514"             # Bell
    "\U0001F4DF"             # Pager
    "\U0001F446"             # Backhand index pointing up
    "\U0001F6D2"             # Shopping cart
    "\U0001F3E0"             # House
    "\U0001F7E1"             # Yellow circle
    "\U0001F7E2"             # Green circle
    "\U0001F6CD"             # Shopping bags
    "\U00002605"             # Black star
    "\U0001F4F1"             # Mobile phone
    "\U0001F49D"             # Heart with ribbon
    "\U0001F517"             # Link
    "\U0001F4CD"             # Round pushpin
    "\U0001F4E3"             # Cheering megaphone
    "\U0001F53B"             # Red triangle pointed down
    "\U0001F500"             # Twisted arrows
    "\U0001F5BC"             # Framed picture
    "\U0000270F"             # Pencil
    "\U0001F6AB"             # Prohibited
    "\U0001F392"             # School backpack
    "\U0001F4BC"             # Briefcase
    "\U0001F311"             # New moon
    "\U0001F467"             # Girl
    "\U0001F468"             # Man
    "\U0001F319"             # Crescent moon
    "\U0001F469"             # Woman
    "\U0001F5B1"             # Computer mouse
    "\U0001F381"             # Wrapped gift
    "\U0001F3B5"             # Musical note
    "\U0001F375"             # Teacup without handle
    "\U0001F4FD"             # Film projector
    "\U0001F495"             # Two hearts
    "\U0001F697"             # Automobile
    "\U0001F9F9"             # Broom
    "\U0001F4F7"             # Camera
    "\U0001F3A5"             # Video camera
    "\U0001F507"             # Speaker with cancellation stroke
    "\U0001F4F9"             # Video camera
    "]",
    flags=re.UNICODE,
)

def strip_emoji(text):
    return EMOJI_PATTERN.sub('', text)

def process_file(filepath):
    path = Path(filepath)
    if not path.exists():
        print(f"[跳过] 文件不存在: {filepath}")
        return False

    original = path.read_text(encoding='utf-8')
    cleaned = strip_emoji(original)

    if cleaned == original:
        print(f"[跳过] 无变化: {filepath}")
        return False

    path.write_text(cleaned, encoding='utf-8')
    removed = len(original) - len(cleaned)
    print(f"[完成] {path.name}: 移除 {removed} 字符")
    return True

if __name__ == "__main__":
    files = sys.argv[1:] if len(sys.argv) > 1 else []
    if not files:
        print("用法: python3 strip_emoji.py file1.html file2.html ...")
        sys.exit(1)
    for f in files:
        process_file(f)
