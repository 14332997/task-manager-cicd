#!/bin/bash
set -e

echo "Starting Task Manager CI/CD pipeline..."

echo "Running todo.py..."
python3 /app/.github/scripts/todo.py | tee /app/task_output.txt

echo "Running todo-test.py..."
python3 /app/.github/scripts/todo-test.py | tee /app/test_output.txt

echo "Updating index.html..."
bash /app/.github/scripts/update_index.sh /app/task_output.txt /app/test_output.txt

echo "Pipeline completed successfully."
