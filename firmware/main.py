import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation


col_0 = board.GP0
col_1 = board.GP1
col_2 = board.GP2
col_3 = board.GP3
col_4 = board.GP4
col_5 = board.GP5
col_6 = board.GP6
col_7 = board.GP7
col_8 = board.GP8
col_9 = board.GP9
col_10 = board.GP10
col_11 = board.GP11
col_12 = board.GP12
col_13 = board.GP13
col_14 = board.GP14
col_15 = board.GP15
col_16 = board.GP16
col_17 = board.GP17
col_18 = board.GP18

row_0 = board.GP19
row_1 = board.GP20
row_2 = board.GP21
row_3 = board.GP22
row_4 = board.GP23
row_5 = board.GP24




d_pin = board.GP8

keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW # the stripe (+) points towards the row 

keyboard.col_pins = (col_0, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, col_10, col_11, col_12, col_13, col_14, col_15, col_16, col_17, col_18);
keyboard.row_pins = (row_0, row_1, row_2, row_3, row_4, row_5);

keyboard.keymap = [
    [KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.DEL, KC.HOME, KC.END, KC.PGUP, KC.PGDOWN, KC.INS],
    
    [KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.NUMLOCK, KC.KP_SLASH, KC.KP_ASTERISK, KC.KP_MINUS],
    
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.KP_7, KC.KP_8, KC.KP_9, KC.KP_PLUS],
    
    [KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.KP_4, KC.KP_5, KC.KP_6],
    
    [KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.UP, KC.KP_1, KC.KP_2, KC.KP_3, KC.KP_ENTER],
    
    [KC.LCTRL, KC.LGUI, KC.LALT, KC.SPACE, KC.FN, KC.RGUI, KC.APP, KC.LEFT, KC.DOWN, KC.RIGHT, KC.KP_0, KC.KP_DOT, KC.KP_COMMA],
]


if __name__ == '__main__':
    keyboard.go()