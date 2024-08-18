import time
import newrelic.agent

newrelic.agent.initialize('newrelic.ini')

def generate_load():
    for i in range(100):
        print(f"Operation {i+1}")
        time.sleep(0.1)  # Simulate some work

if __name__ == "__main__":
    generate_load()
