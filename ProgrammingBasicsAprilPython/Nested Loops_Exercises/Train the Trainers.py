total_presentation_sum = 0
presentation_count = 0
judges_count = int(input())
command = input()

while command != "Finish":
    current_presentation = command
    current_presentation_sum = 0
    for _ in range(judges_count):
        current_judge_score = float(input())
        current_presentation_sum += current_judge_score
    total_presentation_sum += current_presentation_sum
    presentation_count += 1
    avg_score = current_presentation_sum / judges_count
    print(f"{current_presentation} - {avg_score:.2f}.")
    command = input()

avg_total_score = total_presentation_sum / (presentation_count * judges_count)
print(f"Student's final assessment is {avg_total_score:.2f}.")
