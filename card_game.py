import random

# ============================================================================
# Card Class
# ============================================================================
# Represents a single playing card with a suit and rank
class Card:
    def __init__(self, suit, rank):
        """
        Initialize a card with a suit and rank
        
        Args:
            suit (str): One of 'Hearts', 'Diamonds', 'Clubs', 'Spades'
            rank (str): One of '2', '3', ..., '10', 'Jack', 'Queen', 'King', 'Ace'
        """
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        """Return a formatted string representation of the card"""
        return f"{self.rank} of {self.suit}"


# ============================================================================
# Deck Class
# ============================================================================
# Manages a collection of all 52 standard playing cards
class Deck:
    def __init__(self):
        """Initialize the deck with all 52 standard playing cards"""
        self.cards = []
        self._create_deck()
    
    def _create_deck(self):
        """
        Private method to populate the deck with all 52 cards.
        Creates 4 suits × 13 ranks = 52 cards total
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    
    def get_random_card(self):
        """
        Get a random card from the deck without removing it.
        This allows the same deck to be used multiple times.
        
        Returns:
            Card: A random card object
        """
        return random.choice(self.cards)
    
    def deck_size(self):
        """Return the total number of cards in the deck"""
        return len(self.cards)


# ============================================================================
# Main Program
# ============================================================================
# Entry point that creates a deck and displays a random card
if __name__ == "__main__":
    # Create a new deck
    deck = Deck()
    
    # Get a random card from the deck
    random_card = deck.get_random_card()
    
    # Display the random card
    print(f"🎴 Your card: {random_card}")
    print(f"📊 Total cards in deck: {deck.deck_size()}")
