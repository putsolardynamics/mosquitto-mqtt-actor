"""Logging setup class"""
import logging


class Logger:
    """Logger wrapper class"""
    @staticmethod
    def logging_setup(filename: str) -> None:
        """Setup logging for runtime"""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(filename),
                logging.StreamHandler()
            ])

    @staticmethod
    def get_logger() -> logging.Logger:
        """Get logger instance in runtime"""
        return logging.getLogger(__name__)
