import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_flash_card(flash_cards: list[str], path: str = "./flash_cards.csv"):
    """
    Save the flash cards to a file
    """
    # Save the flash cards to a csv file
    try:
        with open(path, "w") as f:
            for flash_card in flash_cards:
                f.write(f"{flash_card}\n")
    except Exception as e:
        logger.error(e)
        logger.error(f"Couldn't save the flash cards to path: {path}")

    return None
