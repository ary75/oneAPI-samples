import time
import newrelic.agent
import logging

logging.basicConfig(level=logging.DEBUG)

newrelic.agent.initialize('newrelic.ini')

def generate_load():
    for i in range(100):
        logging.info(f"Operation {i+1}")
        try:
            newrelic.agent.record_custom_event("CustomLoadEvent", {"operation": i+1})
            logging.info(f"Successfully recorded event {i+1}")
        except Exception as e:
            logging.error(f"Error recording event {i+1}: {e}")
        time.sleep(0.1)  # Simulate some work

if __name__ == "__main__":
    logging.info("Starting load generation")
    generate_load()
    logging.info("Finished load generation")
