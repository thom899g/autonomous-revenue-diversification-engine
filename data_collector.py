import logging
from abc import ABC, abstractmethod
from typing import Dict, Any

class DataCollector:
    def __init__(self):
        self.adapters = []
        
    def add_adapter(self, adapter):
        """Adds a new data adapter to the collector."""
        self.adapters.append(adapter)
        logging.info(f"Adapter {adapter.__class__.__name__} added.")
        
    def collect_data(self) -> Dict[str, Any]:
        """Collects financial data from all registered adapters."""
        try:
            data = {}
            for adapter in self.adapters:
                collected = adapter.fetch_data()
                if collected:
                    data.update(collected)
                    logging.info(f"Data collected from {adapter.__class__.__name__}.")
            return data
        except Exception as e:
            logging.error(f"Failed to collect data: {str(e)}")
            raise

class DataAdapter(ABC):
    @abstractmethod
    def fetch_data(self) -> Dict[str, Any]:
        """Fetches financial data from the target source."""
        pass

# Example adapter implementation
class YahooFinanceAdapter(DataAdapter):
    def __init__(self, api_key: str):
        self.api_key = api_key
        
    def fetch_data(self) -> Dict[str, Any]:
        """Fetches financial data from Yahoo Finance API."""
        try:
            # Placeholder for actual API call
            return {"source": "Yahoo Finance", "data": {}}
        except Exception as e:
            logging.error(f"Failed to fetch data from Yahoo Finance: {str(e)}")
            raise

# Example usage
def main():
    collector = DataCollector()
    collector.add_adapter(YahooFinanceAdapter("your_api_key"))
    # Add more adapters as needed
    data = collector.collect_data()
    logging.info(f"Collected data: {data}")

if __name__ == "__main__":
    main()