#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def parse_dump_choices(dump_path):
    """Extract choices from dump file"""
    choices_map = {}
    current_q = None
    current_choices = []
    in_table = False

    with open(dump_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Question heading
            if re.match(r'^# Q\d+\s*$', line):
                if current_q and current_choices:
                    choices_map[current_q] = current_choices
                current_q = line.strip().replace('# ', '').strip()
                current_choices = []
                in_table = False
                continue

            # Table separator (start of choices)
            if re.match(r'^\|\s*-+\s*\|', line):
                in_table = True
                continue

            # Parse choice rows
            if in_table and line.strip().startswith('|'):
                parts = [p.strip() for p in line.strip().split('|')]
                if len(parts) >= 3 and parts[1] and parts[2]:
                    # parts[1] is letter, parts[2] is description
                    if re.match(r'^[A-E]$', parts[1]):
                        current_choices.append((parts[1], parts[2]))

            # End of table
            if in_table and not line.strip().startswith('|'):
                in_table = False

    # Save last
    if current_q and current_choices:
        choices_map[current_q] = current_choices

    return choices_map

def parse_current_answers(answers_path):
    """Parse current answers_4.md format"""
    questions = {}
    current_q = None
    current_data = {
        'answer': '',
        'explanation_lines': []
    }

    with open(answers_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Question heading: ### Q301
            q_match = re.match(r'^###\s+(Q\d+)\s*$', line)
            if q_match:
                if current_q:
                    questions[current_q] = current_data
                current_q = q_match.group(1)
                current_data = {
                    'answer': '',
                    'explanation_lines': []
                }
                continue

            # Answer line: **정답: C**
            ans_match = re.match(r'^\*\*정답:\s*(.+?)\*\*\s*$', line)
            if ans_match:
                current_data['answer'] = ans_match.group(1)
                continue

            # Skip **풀이:** header
            if line.strip() == '**풀이:**':
                continue

            # Explanation bullets
            if current_q and line.strip().startswith('-'):
                current_data['explanation_lines'].append(line.strip()[2:])  # Remove "- "

    # Save last
    if current_q:
        questions[current_q] = current_data

    return questions

def format_question(q_num, answer_data, choices):
    """Format a single question in new format"""
    answer_letters = [a.strip() for a in answer_data['answer'].split(',')]
    explanation = answer_data['explanation_lines']

    # Separate problem analysis and choice evaluations
    problem_lines = []
    choice_evals = {}

    for line in explanation:
        # Check if this line mentions a specific service/choice
        # Lines like "AWS DataSync(C): ..." or "DataSync(B)는..." or "(A)은..."
        found_choice = False
        for letter in ['A', 'B', 'C', 'D', 'E']:
            if f'({letter})' in line or f'{letter}:' in line:
                if letter not in choice_evals:
                    choice_evals[letter] = []
                choice_evals[letter].append(line)
                found_choice = True
                break

        if not found_choice:
            problem_lines.append(line)

    # Build output
    lines = []
    lines.append(f"# {q_num}")
    lines.append(f"**정답: {answer_data['answer']}**")
    lines.append("")
    lines.append("**문제 분석:**")

    # Add first few problem lines
    for line in problem_lines[:3]:
        lines.append(f"- {line}")

    lines.append("")
    lines.append("**선택지 분석:**")
    lines.append("")
    lines.append("| 번호 | 방식 | 평가 |")
    lines.append("|------|------|------|")

    # Add each choice
    for letter, description in choices:
        # Check mark if correct
        checkmark = "✅ " if letter in answer_letters else ""

        # Truncate description if too long
        desc_display = description
        if len(desc_display) > 70:
            desc_display = desc_display[:70] + "..."

        # Get evaluation for this choice
        if letter in choice_evals:
            # Use the evaluation from explanation
            eval_text = " ".join(choice_evals[letter])
            # Limit length
            if len(eval_text) > 120:
                eval_text = eval_text[:120] + "..."
        else:
            # Generic evaluation
            if letter in answer_letters:
                # Find any explanation mentioning this choice
                relevant = [l for l in explanation if letter in l]
                if relevant:
                    eval_text = relevant[0]
                    if len(eval_text) > 120:
                        eval_text = eval_text[:120] + "..."
                else:
                    eval_text = "정답"
            else:
                # Find negative explanation
                relevant = [l for l in explanation if letter in l]
                if relevant:
                    eval_text = relevant[0]
                    if len(eval_text) > 120:
                        eval_text = eval_text[:120] + "..."
                else:
                    eval_text = "오답"

        # Add emoji to evaluation if not present
        if letter in answer_letters and not eval_text.startswith('✅'):
            eval_text = f"✅ {eval_text}"
        elif letter not in answer_letters and not eval_text.startswith('❌'):
            eval_text = f"❌ {eval_text}"

        lines.append(f"| {checkmark}{letter} | {desc_display} | {eval_text} |")

    lines.append("")
    lines.append("---")
    lines.append("")

    return "\n".join(lines)

def main():
    dump_path = r"C:\Users\yongs\Documents\vault76\AWS\문제집\덤프\dump_4.md"
    answers_path = r"C:\Users\yongs\Documents\vault76\AWS\문제집\덤프\answers_4.md"
    output_path = r"C:\Users\yongs\Documents\vault76\AWS\문제집\덤프\answers_4_converted.md"

    print("Step 1: Parsing dump file for choices...")
    choices = parse_dump_choices(dump_path)
    print(f"  Found {len(choices)} questions with choices")

    print("Step 2: Parsing current answers file...")
    answers = parse_current_answers(answers_path)
    print(f"  Found {len(answers)} answers")

    print("Step 3: Formatting questions...")
    output_lines = ["# Answers for Q301-Q400", ""]

    # Get all question numbers sorted
    all_q_nums = sorted(set(choices.keys()) | set(answers.keys()),
                        key=lambda x: int(x[1:]))

    for q_num in all_q_nums:
        if q_num in answers and q_num in choices:
            formatted = format_question(q_num, answers[q_num], choices[q_num])
            output_lines.append(formatted)
        else:
            if q_num not in answers:
                print(f"  Warning: No answer found for {q_num}")
            if q_num not in choices:
                print(f"  Warning: No choices found for {q_num}")

    print(f"Step 4: Writing output to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines))

    print("✅ Conversion complete!")
    print(f"Output written to: {output_path}")

if __name__ == "__main__":
    main()
