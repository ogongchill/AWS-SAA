#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Read dump_4.md and parse questions with choices
def parse_dump_file(dump_path):
    """Parse dump file and extract question choices"""
    questions = {}
    current_q = None
    current_choices = []
    in_choices = False

    with open(dump_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Match question heading
            q_match = re.match(r'^# (Q\d+)\s*$', line)
            if q_match:
                # Save previous question if exists
                if current_q and current_choices:
                    questions[current_q] = current_choices
                current_q = q_match.group(1)
                current_choices = []
                in_choices = False
                continue

            # Detect start of table (choices)
            if line.strip().startswith('|') and '|' in line:
                # Check if it's the header separator
                if re.match(r'^\|\s*-+\s*\|\s*-+\s*\|', line):
                    in_choices = True
                    continue

                # Parse choice lines
                if in_choices:
                    parts = line.strip().split('|')
                    if len(parts) >= 3:
                        choice_letter = parts[1].strip()
                        choice_text = parts[2].strip()
                        if choice_letter and choice_text:
                            current_choices.append((choice_letter, choice_text))

    # Save last question
    if current_q and current_choices:
        questions[current_q] = current_choices

    return questions

# Read answers_4.md and parse answers
def parse_answers_file(answers_path):
    """Parse answers file and extract answer explanations"""
    answers = {}
    current_q = None
    current_answer = None
    current_explanation = []

    with open(answers_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Match question heading (### Q301 형식)
            q_match = re.match(r'^###\s+(Q\d+)\s*$', line)
            if q_match:
                # Save previous question if exists
                if current_q:
                    answers[current_q] = {
                        'answer': current_answer,
                        'explanation': current_explanation
                    }
                current_q = q_match.group(1)
                current_answer = None
                current_explanation = []
                continue

            # Match answer line
            ans_match = re.match(r'^\*\*정답:\s*(.+?)\*\*\s*$', line)
            if ans_match:
                current_answer = ans_match.group(1)
                continue

            # Skip "**풀이:**" line
            if line.strip() == '**풀이:**':
                continue

            # Collect explanation lines (bullet points)
            if current_q and line.strip().startswith('-'):
                current_explanation.append(line.strip())

    # Save last question
    if current_q:
        answers[current_q] = {
            'answer': current_answer,
            'explanation': current_explanation
        }

    return answers

# Generate formatted answer with table
def generate_formatted_answer(q_num, answer_data, choices):
    """Generate answer in table format"""
    answer_letter = answer_data['answer']
    explanation_lines = answer_data['explanation']

    # Parse answer letters (could be "A", "A, C", etc.)
    correct_answers = [a.strip() for a in answer_letter.split(',')]

    # Generate problem analysis from explanation
    problem_analysis = []
    choice_details = {}

    for line in explanation_lines:
        # Lines about specific choices (e.g., "- AWS DataSync(C): ...")
        choice_match = re.search(r'[A-E]\)', line)
        if choice_match:
            # This is choice-specific detail
            for choice in choices:
                if f'{choice[0]})' in line or f'({choice[0]})' in line:
                    if choice[0] not in choice_details:
                        choice_details[choice[0]] = []
                    choice_details[choice[0]].append(line[2:])  # Remove "- "
        else:
            # This is general problem analysis
            problem_analysis.append(line[2:])  # Remove "- "

    # Generate output
    output = [f"# {q_num}", f"**정답: {answer_letter}**", "", "**문제 분석:**"]

    # Add problem analysis
    for line in problem_analysis[:3]:  # Take first 3 lines as problem analysis
        output.append(f"- {line}")

    output.extend(["", "**선택지 분석:**", ""])

    # Generate table
    output.append("| 번호 | 방식 | 평가 |")
    output.append("|------|------|------|")

    for choice_letter, choice_text in choices:
        # Truncate long choice text
        if len(choice_text) > 60:
            choice_text = choice_text[:60] + "..."

        # Determine if correct answer
        is_correct = choice_letter in correct_answers
        prefix = "✅ " if is_correct else ""

        # Get evaluation
        if choice_letter in choice_details:
            eval_text = " ".join(choice_details[choice_letter])
            if len(eval_text) > 100:
                eval_text = eval_text[:100] + "..."
        else:
            # Use remaining explanation lines
            remaining = [line for line in explanation_lines if choice_letter in line]
            if remaining:
                eval_text = remaining[0][2:]  # Remove "- "
                if len(eval_text) > 100:
                    eval_text = eval_text[:100] + "..."
            else:
                eval_text = "✅ 정답" if is_correct else "❌ 오답"

        # Add emoji to evaluation
        if is_correct and not eval_text.startswith('✅'):
            eval_text = f"✅ {eval_text}"
        elif not is_correct and not eval_text.startswith('❌'):
            eval_text = f"❌ {eval_text}"

        output.append(f"| {prefix}{choice_letter} | {choice_text} | {eval_text} |")

    output.extend(["", "---", ""])

    return "\n".join(output)

def main():
    dump_path = r"C:\Users\yongs\Documents\vault76\AWS\문제집\덤프\dump_4.md"
    answers_path = r"C:\Users\yongs\Documents\vault76\AWS\문제집\덤프\answers_4.md"
    output_path = r"C:\Users\yongs\Documents\vault76\AWS\문제집\덤프\answers_4_new.md"

    print("Parsing dump file...")
    choices_map = parse_dump_file(dump_path)
    print(f"Found {len(choices_map)} questions with choices")

    print("Parsing answers file...")
    answers_map = parse_answers_file(answers_path)
    print(f"Found {len(answers_map)} answers")

    print("Generating formatted answers...")
    output_lines = ["# Answers for Q301-Q400", ""]

    for q_num in sorted(answers_map.keys(), key=lambda x: int(x[1:])):
        if q_num in choices_map:
            formatted = generate_formatted_answer(q_num, answers_map[q_num], choices_map[q_num])
            output_lines.append(formatted)
        else:
            print(f"Warning: No choices found for {q_num}")

    # Write output
    print(f"Writing to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines))

    print("Done!")

if __name__ == "__main__":
    main()
