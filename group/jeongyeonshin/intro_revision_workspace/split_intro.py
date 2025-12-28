#!/usr/bin/env python3
"""
Split Introduction into 3 parts for separate processing
"""

# Read full introduction
with open('/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_extracted.txt', 'r') as f:
    content = f.read()

# Split into sections
lines = content.split('\n')

# Part 1: Opening (lines 1-11) - 개선된 버전 이미 있음
part1_end = None
for i, line in enumerate(lines):
    if 'Early life stress and neurocognitive functions' in line:
        part1_end = i
        break

# Part 2: Literature review (line 12 - line 56)
part2_end = None
for i, line in enumerate(lines):
    if 'Research gap and objectives' in line:
        part2_end = i
        break

# Part 3: Gap and objectives (line 57 - end)

# Extract parts
part1 = '\n'.join(lines[1:part1_end]).strip()  # Skip "Introduction" title
part2 = '\n'.join(lines[part1_end:part2_end]).strip()
part3 = '\n'.join(lines[part2_end:]).strip()

# Save parts
with open('/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_part1_opening.txt', 'w') as f:
    f.write(part1)

with open('/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_part2_literature.txt', 'w') as f:
    f.write(part2)

with open('/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_part3_gap.txt', 'w') as f:
    f.write(part3)

print("✅ Introduction split into 3 parts:")
print(f"Part 1 (Opening): {len(part1.split())} words")
print(f"Part 2 (Literature Review): {len(part2.split())} words")
print(f"Part 3 (Gap & Objectives): {len(part3.split())} words")
print()
print("Files created:")
print("  - intro_part1_opening.txt")
print("  - intro_part2_literature.txt")
print("  - intro_part3_gap.txt")
