from tkinter import Tk, Label, Button
import random

game = [None] * 9
game_left = [x for x in range(9)]
turn = 0

def win(mark):
    if (game[0] == mark and game[1] == mark and game[2] == mark) or (game[3] == mark and game[4] == mark and game[5] == mark) \
            or (game[6] == mark and game[7] == mark and game[8] == mark) or (game[0] == mark and game[3] == mark and game[6] == mark) \
            or (game[1] == mark and game[4] == mark and game[7] == mark) or (game[2] == mark and game[5] == mark and game[8] == mark) \
            or (game[0] == mark and game[4] == mark and game[8] == mark) or (game[2] == mark and game[4] == mark and game[6] == mark):
        return True
    
def stop_game():
    for item in game_left:
        buttons[item].config(bg='beige', state='disabled')

        

def push(place):
    global turn
    game[place] = 'X'
    buttons[place].config(text='X', bg='beige', state='disabled')
    game_left.remove(place)

    if place == 4 and turn == 0:
        comp_turn = random.choice(game_left)
    elif place != 4 and turn == 0:
        comp_turn = 4
    if turn > 0:
        comp_turn = 8 - place
    if comp_turn not in game_left:
        try:
            comp_turn = random.choice(game_left)
        except IndexError:
            label['text'] = 'Ничья!'
            stop_game()

        
    game[comp_turn] = '0'
    buttons[comp_turn].config(text='0', bg='beige', state='disabled')
    if win('X'):
        label['text'] = 'Ура! Вы победили!'
        stop_game()
    elif win('0'):
        label['text'] = 'Вы проиграли:('
        stop_game()
    else:
        if len(game_left) > 1:
            game_left.remove(comp_turn)
        else:
            label['text'] = 'Ничья!'
            stop_game()
        turn += 1
    

window = Tk()
window.title('Добро пожаловать в игру!')
label = Label(width=20, text='Игра крестки-нолики', font=('Tahoma', 20))
label.grid(row=0, column=0, columnspan=3)

buttons = [Button(width=10, height=4, font=(30), bg='dark red', command=lambda x=i: push(x)) for i in range(9)]

row_for_button, column_for_button = 1, 0
for i in range(9):
    buttons[i].grid(row=row_for_button, column=column_for_button)
    column_for_button += 1
    if column_for_button == 3:
        row_for_button += 1
        column_for_button = 0


window.mainloop()

