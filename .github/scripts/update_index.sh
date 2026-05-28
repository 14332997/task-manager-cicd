#!/bin/bash
set -e

TASK_FILE="$1"
TEST_FILE="$2"
HTML_FILE="index.html"

if [ -z "$TASK_FILE" ] || [ -z "$TEST_FILE" ]; then
    echo "Usage: bash update_index.sh <task_output_file> <test_output_file>"
    exit 1
fi

python3 - "$TASK_FILE" "$TEST_FILE" "$HTML_FILE" <<'PY'
import sys
import re
import html
from pathlib import Path

task_file = Path(sys.argv[1])
test_file = Path(sys.argv[2])
html_file = Path(sys.argv[3])

task_output = task_file.read_text()
test_output = test_file.read_text()

todo_match = re.search(r"ToDo Tasks:\s*(.*?)(?:\n\s*Done Tasks:|$)", task_output, re.S)
done_match = re.search(r"Done Tasks:\s*(.*)$", task_output, re.S)

todo_text = todo_match.group(1).strip() if todo_match else "No ToDo tasks found"
done_text = done_match.group(1).strip() if done_match else "No Done tasks found"
test_text = test_output.strip() if test_output.strip() else "No test results found"

content = html_file.read_text()

def update_pre(content, pre_id, text):
    pattern = rf'(<pre id="{pre_id}">)(.*?)(</pre>)'

    def replace(match):
        return match.group(1) + html.escape(text) + match.group(3)

    return re.sub(pattern, replace, content, flags=re.S)

content = update_pre(content, "todo-tasks", todo_text)
content = update_pre(content, "done-tasks", done_text)
content = update_pre(content, "test-results", test_text)

html_file.write_text(content)
PY

echo "index.html updated successfully"
