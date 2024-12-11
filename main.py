from src.models.dealer import Dealer
from src.models.shoe import Shoe
from src.models.deck import Deck
from src.models.table import Table
from src.models.card_counter import CardCounter
from src.models.card import Card
from src.models.hand import Hand


num_decks = 1
minimum_bet_amount = 10

card_counter = CardCounter()
dealer = Dealer()
deck = Deck()
shoe = Shoe(num_decks, deck)
table = Table(dealer, card_counter, shoe, minimum_bet_amount)
play_records = {}


def play_round():
    play_id = len(play_records) + 1
    play_records["play_id"] = play_id

    table.initial_deal()
    table.card_counter.check_initial_hand()
    
    # Check if card_counter has blackjack
    if 21 in [table.card_counter.hands[0].card_sums]:
        if 21 in [table.dealer.hand.card_sums]:
            play_records["win_amount"] = 0
        else:
            play_records["win_amount"] = table.minimum_bet_amount*1.5
        
        play_records["card_counter_cards"] = [card.card_type for card in table.card_counter.hands[0].cards]
        play_records["dealer_cards"] = [card.card_type for card in table.dealer.hand.cards]
        play_records["running_count"] = table.shoe.running_count
        play_records["true_count"] = table.shoe.true_count
        play_records["cards_remaining"] = len(table.shoe.cards)
        return

    table.card_counter.choose_starting_strategy()
    table.card_counter.check_hand_key(table.card_counter.hands[0])
    table.card_counter.check_play_strategy(table.dealer.hand.cards[-1], table.shoe.true_count, table.shoe.running_count)
    
    # stay action
    if table.card_counter.play_decision == "stay":
        while table.dealer.hand.card_sums:
            if table.dealer.hand_card_sums == [17] or max(table.dealer.hand_card_sums) in {18, 19, 20, 21}:
                if max(table.card_counter.hands[0].card_sums) > max(table.dealer.hand_card_sums):
                    play_records["win_amount"] = table.minimum_bet_amount
                elif max(table.card_counter.hands[0].card_sums) == max(table.dealer.hand_card_sums):
                    play_records["win_amount"] = 0
                else:
                    play_records["win_amount"] = table.minimum_bet_amount
            play_records["card_counter_cards"] = [card.card_type for card in table.card_counter.hands[0].cards]
            play_records["dealer_cards"] = [card.card_type for card in table.dealer.hand.cards]
            play_records["running_count"] = table.shoe.running_count
            play_records["true_count"] = table.shoe.true_count
            play_records["cards_remaining"] = len(table.shoe.cards)

            if max(table.dealer.hand_card_sums) < 17:
                table.dealer.hand.add_card(table.shoe.deal_card())
            if set(table.dealer.hand.card_sums) == {17, 7}:
                table.dealer.hand.add_card(table.shoe.deal_card())
            if not table.dealer.card_sums:
                play_records["win_amount"] = table.minimum_bet_amount
                play_records["card_counter_cards"] = [card.card_type for card in table.card_counter.hands[0].cards]
                play_records["dealer_cards"] = [card.card_type for card in table.dealer.hand.cards]
                play_records["running_count"] = table.shoe.running_count
                play_records["true_count"] = table.shoe.true_count
                play_records["cards_remaining"] = len(table.shoe.cards)
            return
            



    






        # table.dealer.play(table.shoe.deal_card())

        if not table.dealer.hand.card_sums:
            play_round_record["win_amount"] = table.minimum_bet_amount
            play_round_record["card_counter_cards"] = [card.card_type for card in table.card_counter.hands[0].cards]
            play_round_record["dealer_cards"] = [card.card_type for card in table.dealer.hand.cards]
            play_round_record["running_count"] = table.shoe.running_count
            play_round_record["true_count"] = table.shoe.true_count
            play_round_record["cards_remaining"] = len(table.shoe.cards)
            return

        card_counter_hand_sum = max(table.card_counter.hands[0].card_sums)
        dealer_hand_sum = max(table.dealer.hand.card_sums)
        if card_counter_hand_sum > dealer_hand_sum:
            play_round_record["win_amount"] = table.minimum_bet_amount
        elif card_counter_hand_sum == dealer_hand_sum:
            play_round_record["win_amount"] = 0
        else:
            play_round_record["win_amount"] = -table.minimum_bet_amount

        play_round_record["card_counter_cards"] = [card.card_type for card in table.card_counter.hands[0].cards]
        play_round_record["dealer_cards"] = [card.card_type for card in table.dealer.hand.cards]
        play_round_record["running_count"] = table.shoe.running_count
        play_round_record["true_count"] = table.shoe.true_count
        play_round_record["cards_remaining"] = len(table.shoe.cards)
        return

    # surrender action
    if table.card_counter.play_decision == "surrender":
        play_round_record["win_amount"] = -table.minimum_bet_amount/2
        play_round_record["card_counter_cards"] = [card.card_type for card in table.card_counter.hands[0].cards]
        play_round_record["dealer_cards"] = [card.card_type for card in table.dealer.hand.cards]
        play_round_record["running_count"] = table.shoe.running_count
        play_round_record["true_count"] = table.shoe.true_count
        play_round_record["cards_remaining"] = len(table.shoe.cards)
        return
    
    # double action
    if table.card_counter.play_decision == "double":
        table.card_counter.hands[0].add_card(table.shoe.deal_card())
        if not table.card_counter.hands[0].card_sums:
            play_round_record["win_amount"] = -table.minimum_bet_amount*2
            play_round_record["card_counter_cards"] = [card.card_type for card in table.card_counter.hands[0].cards]
            play_round_record["dealer_cards"] = [card.card_type for card in table.dealer.hand.cards]
            play_round_record["running_count"] = table.shoe.running_count
            play_round_record["true_count"] = table.shoe.true_count
            play_round_record["cards_remaining"] = len(table.shoe.cards)
            return
        else:
            card_counter_hand_sum = max(table.card_counter.hands[0].card_sums)
            dealer_hand_sum = max(table.dealer.hand.card_sums)
            if card_counter_hand_sum > dealer_hand_sum:
                play_round_record["win_amount"] = table.minimum_bet_amount*2
            elif card_counter_hand_sum == dealer_hand_sum:
                play_round_record["win_amount"] = 0
            else:
                play_round_record["win_amount"] = -table.minimum_bet_amount*2
 
            play_round_record["card_counter_cards"] = [card.card_type for card in table.card_counter.hands[0].cards]
            play_round_record["dealer_cards"] = [card.card_type for card in table.dealer.hand.cards]
            play_round_record["running_count"] = table.shoe.running_count
            play_round_record["true_count"] = table.shoe.true_count
            play_round_record["cards_remaining"] = len(table.shoe.cards)
            return

    # action to get to 21, stay, or bust
    while table.card_counter.play_decision == "hit":
        table.card_counter.hands[0].add_card(table.shoe.deal_card())
        if not table.card_counter.hands[0].card_sums:
            play_round_record["win_amount"] = -table.minimum_bet_amount
            play_round_record["card_counter_cards"] = [card.card_type for card in table.card_counter.hands[0].cards]
            play_round_record["dealer_cards"] = [card.card_type for card in table.dealer.hand.cards]
            play_round_record["running_count"] = table.shoe.running_count
            play_round_record["true_count"] = table.shoe.true_count
            play_round_record["cards_remaining"] = len(table.shoe.cards)
            return

        if len(table.card_counter.hands[0].card_sums) == 1:
            table.card_counter.hand_type = "hard"
            table.card_counter.choose_starting_strategy()
            table.card_counter.check_hand_key(table.card_counter.hands[0])
            table.card_counter.check_play_strategy(table.dealer.hand.cards[-1], table.shoe.true_count, table.shoe.running_count)

            if not table.card_counter.hands[0].card_sums:
                play_round_record["win_amount"] = -table.minimum_bet_amount
                play_round_record["card_counter_cards"] = [card.card_type for card in table.card_counter.hands[0].cards]
                play_round_record["dealer_cards"] = [card.card_type for card in table.dealer.hand.cards]
                play_round_record["running_count"] = table.shoe.running_count
                play_round_record["true_count"] = table.shoe.true_count
                play_round_record["cards_remaining"] = len(table.shoe.cards)
                return




        # if table.card_counter.play_decision == "split":
        #     table.card_counter.hands.append(Hand())
        #     table.card_counter.hands[-1].cards.append(table.card_counter.hands[0].cards.pop())
        #     for hand in table.card_counter.hands:



    
    # play_round_record["card_counter_cards"] = [card.card_type for card in table.card_counter.hands[0].cards]
    # play_round_record["dealer_cards"] = [card.card_type for card in table.dealer.hand.cards]





table.shoe.shuffle()
play_round()
