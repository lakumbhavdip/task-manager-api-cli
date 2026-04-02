import typer
import requests
from typing import Optional

app = typer.Typer()
API_URL = "http://127.0.0.1:8000/tasks"

@app.command()
def add(title: str, description: Optional[str] = None, priority: Optional[str] = "medium", due_date: Optional[str] = typer.Option(None, "--due_date")):
    payload = {"title": title, "description": description, "priority": priority, "due_date": due_date}
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        print(f"Task created with ID: {response.json()['id']}")
    else:
        print(f"Error {response.status_code}: {response.text}")


@app.command()
def list(status: Optional[str] = None, priority: Optional[str] = None):
    params = {} 
    if status: params["status"] = status
    if priority: params["priority"] = priority
    
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        tasks = response.json()
        print(f"{'ID':<3} | {'Title':<20} | {'Status':<12} | {'Priority':<8} | {'Description'}")
        print("-" * 80)
        for t in tasks:
            desc = t.get('description') or "N/A"
            print(f"{t['id']:<3} | {t['title']:<20} | {t['status']:<12} | {t['priority']:<8} | {desc}")
    else:
        print(f"Error {response.status_code}: {response.text}")

@app.command()
def get(task_id: int):
    response = requests.get(f"{API_URL}/{task_id}")
    if response.status_code == 200:
        t = response.json()
        for key, value in t.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print(f"Error {response.status_code}: {response.text}")

@app.command()
def update(task_id: int, title: Optional[str] = None, description: Optional[str] = None, status: Optional[str] = None, priority: Optional[str] = None):
    payload = {}
    if title: payload["title"] = title
    if status: payload["status"] = status
    if priority: payload["priority"] = priority
    if description is not None: payload["description"] = description
    
    response = requests.patch(f"{API_URL}/{task_id}", json=payload)
    if response.status_code == 200:
        print(f"Task {task_id} updated successfully!")
    else:
        print(f"Error {response.status_code}: {response.text}")

@app.command()
def complete(task_id: int):
    response = requests.patch(f"{API_URL}/{task_id}", json={"status": "completed"})
    if response.status_code == 200:
        print(f"Task {task_id} marked as completed!")
    else:
        print(f"Error {response.status_code}: {response.text}")

@app.command()
def delete(task_id: int):
    response = requests.delete(f"{API_URL}/{task_id}")
    if response.status_code == 200:
        print(f"Task {task_id} deleted!")
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    app()
