import random

class Deck:                                       ##instance 없이 쓰는 static method로 Deck.make_deck()
    

    def __init__(self):
        print ("good")
    
    def make_deck(self):                               ## deck 을 만든다
        deck = []
        shape = ["S","D","H","C"]
        number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]

                card = res_shape + res_number
                
                deck.append(card)
        return deck
        
        
    def shuffle(self):
        new = self.make_deck()
        random.shuffle(new)
        return new

    
    def pop_card(self):
        new1 = self.shuffle()
        received_card = []
        for i in range(1,3):
            card = new1.pop(i)
            received_card.append(card)
        return received_card
    
    def hit(self, received):
        a = received 
        new1 = self.shuffle()             ## hit 하는거
        return a.append(new1.pop(0))
        


class Participant:

    received_card = []

    def __init__(self):
        
        self.received_card = received_card

    
    def hit(self):                             ## hit 하는거
        
        self.received_card.append(new1.pop(1))
        



class Player(Participant):

    def __init__(self):

        self.name = 'player'

   

class Dealer(Participant):

    def __init__(self):

        self.name = 'dealer'
    
    
    def machine_hit(self):
        
        if Sum.sum_result() <= 17:
            self.hit()
        elif Sum.sum_result > 17:
            return dealer.received_card 

###-----------------------------------------------------------------------------------            

class Sum:                                          ## Match 클래스에 상속?????

    
    sum_result = 0   

    def sum(self):
        
        for i in self.received_card:
            
            sum_result += int(i[1])
        

    def a_decision():
        
        if i[1] == 'A' and sum_result + 11 > 21:
            a = i[1]
            a = 1
            d = a + sum_result
        elif i[1] == 'A' and sum_result + 11 < 21:
            a = i[1]
            a = 11
            d = a + sum_result  
             
             
    def jqk_decision():
        a = 0
        if i[1] == 'J' or i[1] == 'Q' or i[1] == 'K':
            a = i[1]
            a = 10
   

class Match(Sum):                     ## Match 클래스가 Sum 클래스를 상속
    
    def fail(self):                   ## 가진 카드의 합이 21이 넘으면 패한다
    
        if self.received_card.sum() > 21:

            print(self.name, "Lose!!!")


    def match():                            ## sum 을 비교하여 승부를 낸다

        if player.received_card.sum() - dealer.received_card.sum() > 0:

            print("You win!!")

        elif player.received_card.sum() - dealer.received_card.sum() == 0:

            print("Draw!!")

        else:

            print("You lose~")

                                             
#---------------Main Flow-------------------

invite = input('게임에 참석하시겠습니까? (Yes / No)'+'\n')       ## 시작

if invite == 'Yes':

    player = Deck()
    dealer = Deck()
    a = player.pop_card()
    b = dealer.pop_card()
    
    print("P>>>", a)
    print("D>>>", b)
    
elif invite == 'No':

    print('>>>','다음에 만나요')

else :
    print("=============================================Error!!! 다시 입력해주세요.===============================")

while True:                                                ## 둘째 턴 ~ 종료
    
    gesture = input('카드를 한장 받으시겠습니까? (Yes / No)/n')

    if gesture == 'Yes':
        
        c = player.hit(a)
        d = dealer.hit(b)


        print("P>>>", c)
        print("D>>>", d)

        continue
    
    elif gesture == 'No':

        dealer.machine_hit()
        
        print("P>>>", player.received_card)
        print("D>>>", dealer.received_card)

        Match.match()

        
        break