"""Generate Moun system electrical schematic SVG from engineering model."""
from pathlib import Path

NET_COLORS = {
    "GND": "#52525b", "VIN12": "#dc2626", "V5": "#ea580c", "V33": "#2563eb",
    "I2C": "#0d9488", "STEP": "#7c3aed", "DIR": "#6d28d9", "LED_PWM": "#ca8a04",
    "LIMIT": "#be123c", "BRG": "#d97706", "MOT": "#4338ca",
}

BLOCKS = [
    ("J1", "DC IN", "12 V nominal", 32, 280, 64, 88),
    ("U2", "BUCK", "12V→5V", 160, 268, 88, 112),
    ("U1", "MCU", "ATmega328P class", 360, 120, 120, 200),
    ("U3", "IMU", "MPU-6050 class", 560, 132, 88, 96),
    ("U4", "STEP DRV", "A4988 class", 560, 300, 96, 112),
    ("J2", "MOTOR", "Bipolar", 692, 312, 52, 72),
    ("J3", "POGO BRIDGE", "B↔C", 360, 380, 200, 72),
    ("Q1", "NFET", "LED dim", 560, 460, 56, 64),
    ("J4", "LIMITS", "Hall / switch", 200, 120, 72, 88),
]

WIRES = [
    ("VIN12", [[96, 308], [160, 308], [160, 300]]),
    ("VIN12", [[248, 300], [520, 300], [520, 332], [560, 332]]),
    ("GND", [[96, 344], [160, 344], [160, 340]]),
    ("GND", [[248, 348], [320, 348], [320, 420], [360, 420]]),
    ("V5", [[248, 308], [320, 308], [320, 156], [360, 156]]),
    ("V5", [[320, 156], [560, 156]]),
    ("I2C", [[480, 164], [520, 164], [520, 148], [560, 148]]),
    ("I2C", [[480, 192], [520, 192], [520, 180], [560, 180]]),
    ("STEP", [[480, 228], [520, 228], [520, 412], [592, 412]]),
    ("DIR", [[480, 256], [520, 256], [520, 412], [624, 412]]),
    ("LED_PWM", [[480, 284], [500, 284], [500, 484], [560, 484]]),
    ("LIMIT", [[272, 152], [320, 152], [320, 228], [360, 228]]),
    ("LIMIT", [[272, 184], [340, 184], [340, 264], [360, 264]]),
    ("MOT", [[656, 340], [674, 340], [692, 340]]),
    ("MOT", [[656, 380], [674, 380], [692, 372]]),
]

LEGEND = [
    ("VIN12", "+12 V bus"), ("V5", "+5 V logic"), ("GND", "Ground"),
    ("I2C", "I2C (SDA/SCL)"), ("STEP", "Step pulse"), ("DIR", "Direction"),
    ("LED_PWM", "LED PWM"), ("LIMIT", "Limit inputs"), ("BRG", "Bridge / motion interface"),
    ("MOT", "Stepper coil drive"),
]

VB_W, VB_H = 820, 560
lines = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VB_W} {VB_H}" role="img" aria-label="Moun system electrical schematic">',
    '<defs><pattern id="schGrid" width="20" height="20" patternUnits="userSpaceOnUse">',
    '<path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e7e5e4" stroke-width="0.5"/></pattern></defs>',
    f'<rect width="{VB_W}" height="{VB_H}" fill="#fafaf9"/>',
    f'<rect width="{VB_W}" height="{VB_H}" fill="url(#schGrid)" opacity="0.65"/>',
    '<text x="24" y="36" font-size="13" font-weight="800" fill="#1c1917">Moun — system schematic (conceptual)</text>',
    '<text x="24" y="52" font-size="9" fill="#78716c">Not a substitute for signed ECAD outputs — design review and BOM discussion only.</text>',
]

for net, pts in WIRES:
    color = NET_COLORS.get(net, "#a8a29e")
    points = " ".join(f"{x},{y}" for x, y in pts)
    lines.append(f'<polyline fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="miter" stroke-linecap="square" points="{points}" opacity="0.92"/>')

for ref, title, detail, x, y, w, h in BLOCKS:
    lines.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#ffffff" stroke="#292524" stroke-width="1.75"/>')
    lines.append(f'<text x="{x + 8}" y="{y + 16}" font-size="10" font-weight="800" fill="#d97706">{ref}</text>')
    lines.append(f'<text x="{x + w/2}" y="{y + 34}" text-anchor="middle" font-size="10" font-weight="700" fill="#1c1917">{title}</text>')
    lines.append(f'<text x="{x + w/2}" y="{y + 48}" text-anchor="middle" font-size="8" fill="#78716c">{detail}</text>')

lines.append('<text x="24" y="496" font-size="8" font-weight="700" fill="#57534e">Net legend</text>')
for i, (net, label) in enumerate(LEGEND):
    col, row = i // 5, i % 5
    lx, ly = 24 + col * 120, 508 + row * 12
    c = NET_COLORS.get(net, "#999")
    lines.append(f'<line x1="{lx}" y1="{ly}" x2="{lx + 18}" y2="{ly}" stroke="{c}" stroke-width="3"/>')
    lines.append(f'<text x="{lx + 24}" y="{ly + 3}" font-size="7.5" fill="#57534e">{label}</text>')

lines.append('<g transform="translate(520, 472)">')
lines.append('<rect x="0" y="0" width="276" height="72" fill="#fff" stroke="#d6d3d1" stroke-width="1" rx="4"/>')
lines.append('<text x="12" y="18" font-size="8" font-weight="800" fill="#1c1917">Title block</text>')
lines.append('<text x="12" y="34" font-size="7.5" fill="#57534e">Moun / RawGraded Pro — Engineering build guide</text>')
lines.append('<text x="12" y="48" font-size="7.5" fill="#57534e">Rev B · 2026-04-09 · Sheet 1/1</text>')
lines.append('<text x="12" y="62" font-size="7" fill="#a8a29e">ECAD sync: pending — diff against KiCad / Altium release.</text>')
lines.append('</g>')
lines.append('<text x="460" y="452" text-anchor="middle" font-size="8" fill="#57534e" font-style="italic">J3 pad field — correlate pads 1–6 to MCU nets in bridge pinout table</text>')
lines.append('</svg>')

out = Path(__file__).resolve().parent.parent / "docs" / "assets" / "themoun" / "moun-system-electrical-schematic.svg"
out.write_text("\n".join(lines), encoding="utf-8")
print("Wrote", out)
