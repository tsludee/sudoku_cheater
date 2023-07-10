from tkinter import *
import sudoku_solver


root = Tk()
root.title('Sudoku Solver')

def submit():
    return

# create puzzle entry
# row 1
row1_col1 = Entry(root)
row1_col2 = Entry(root)
row1_col3 = Entry(root)
row1_col4 = Entry(root)
row1_col5 = Entry(root)
row1_col6 = Entry(root)
row1_col7 = Entry(root)
row1_col8 = Entry(root)
row1_col9 = Entry(root)

# row 2
row2_col1 = Entry(root)
row2_col2 = Entry(root)
row2_col3 = Entry(root)
row2_col4 = Entry(root)
row2_col5 = Entry(root)
row2_col6 = Entry(root)
row2_col7 = Entry(root)
row2_col8 = Entry(root)
row2_col9 = Entry(root)

# row 3
row3_col1 = Entry(root)
row3_col2 = Entry(root)
row3_col3 = Entry(root)
row3_col4 = Entry(root)
row3_col5 = Entry(root)
row3_col6 = Entry(root)
row3_col7 = Entry(root)
row3_col8 = Entry(root)
row3_col9 = Entry(root)

# row 4
row4_col1 = Entry(root)
row4_col2 = Entry(root)
row4_col3 = Entry(root)
row4_col4 = Entry(root)
row4_col5 = Entry(root)
row4_col6 = Entry(root)
row4_col7 = Entry(root)
row4_col8 = Entry(root)
row4_col9 = Entry(root)

# row 5
row5_col1 = Entry(root)
row5_col2 = Entry(root)
row5_col3 = Entry(root)
row5_col4 = Entry(root)
row5_col5 = Entry(root)
row5_col6 = Entry(root)
row5_col7 = Entry(root)
row5_col8 = Entry(root)
row5_col9 = Entry(root)

# row 6
row6_col1 = Entry(root)
row6_col2 = Entry(root)
row6_col3 = Entry(root)
row6_col4 = Entry(root)
row6_col5 = Entry(root)
row6_col6 = Entry(root)
row6_col7 = Entry(root)
row6_col8 = Entry(root)
row6_col9 = Entry(root)

# row 7
row7_col1 = Entry(root)
row7_col2 = Entry(root)
row7_col3 = Entry(root)
row7_col4 = Entry(root)
row7_col5 = Entry(root)
row7_col6 = Entry(root)
row7_col7 = Entry(root)
row7_col8 = Entry(root)
row7_col9 = Entry(root)

# row 8
row8_col1 = Entry(root)
row8_col2 = Entry(root)
row8_col3 = Entry(root)
row8_col4 = Entry(root)
row8_col5 = Entry(root)
row8_col6 = Entry(root)
row8_col7 = Entry(root)
row8_col8 = Entry(root)
row8_col9 = Entry(root)

# row 9
row9_col1 = Entry(root)
row9_col2 = Entry(root)
row9_col3 = Entry(root)
row9_col4 = Entry(root)
row9_col5 = Entry(root)
row9_col6 = Entry(root)
row9_col7 = Entry(root)
row9_col8 = Entry(root)
row9_col9 = Entry(root)

# place puzzle entry
# row 1
row1_col1.grid(row=1, column=1)
row1_col2.grid(row=1, column=2)
row1_col3.grid(row=1, column=3)
row1_col4.grid(row=1, column=4)
row1_col5.grid(row=1, column=5)
row1_col6.grid(row=1, column=6)
row1_col7.grid(row=1, column=7)
row1_col8.grid(row=1, column=8)
row1_col9.grid(row=1, column=9)

# row 2
row2_col1.grid(row=2, column=1)
row2_col2.grid(row=2, column=2)
row2_col3.grid(row=2, column=3)
row2_col4.grid(row=2, column=4)
row2_col5.grid(row=2, column=5)
row2_col6.grid(row=2, column=6)
row2_col7.grid(row=2, column=7)
row2_col8.grid(row=2, column=8)
row2_col9.grid(row=2, column=9)

# row 3
row3_col1.grid(row=3, column=1)
row3_col2.grid(row=3, column=2)
row3_col3.grid(row=3, column=3)
row3_col4.grid(row=3, column=4)
row3_col5.grid(row=3, column=5)
row3_col6.grid(row=3, column=6)
row3_col7.grid(row=3, column=7)
row3_col8.grid(row=3, column=8)
row3_col9.grid(row=3, column=9)

# row 4
row4_col1.grid(row=4, column=1)
row4_col2.grid(row=4, column=2)
row4_col3.grid(row=4, column=3)
row4_col4.grid(row=4, column=4)
row4_col5.grid(row=4, column=5)
row4_col6.grid(row=4, column=6)
row4_col7.grid(row=4, column=7)
row4_col8.grid(row=4, column=8)
row4_col9.grid(row=4, column=9)

# row 5
row5_col1.grid(row=5, column=1)
row5_col2.grid(row=5, column=2)
row5_col3.grid(row=5, column=3)
row5_col4.grid(row=5, column=4)
row5_col5.grid(row=5, column=5)
row5_col6.grid(row=5, column=6)
row5_col7.grid(row=5, column=7)
row5_col8.grid(row=5, column=8)
row5_col9.grid(row=5, column=9)

# row 6
row6_col1.grid(row=6, column=1)
row6_col2.grid(row=6, column=2)
row6_col3.grid(row=6, column=3)
row6_col4.grid(row=6, column=4)
row6_col5.grid(row=6, column=5)
row6_col6.grid(row=6, column=6)
row6_col7.grid(row=6, column=7)
row6_col8.grid(row=6, column=8)
row6_col9.grid(row=6, column=9)

# row 7
row7_col1.grid(row=7, column=1)
row7_col2.grid(row=7, column=2)
row7_col3.grid(row=7, column=3)
row7_col4.grid(row=7, column=4)
row7_col5.grid(row=7, column=5)
row7_col6.grid(row=7, column=6)
row7_col7.grid(row=7, column=7)
row7_col8.grid(row=7, column=8)
row7_col9.grid(row=7, column=9)

# row 8
row8_col1.grid(row=8, column=1)
row8_col2.grid(row=8, column=2)
row8_col3.grid(row=8, column=3)
row8_col4.grid(row=8, column=4)
row8_col5.grid(row=8, column=5)
row8_col6.grid(row=8, column=6)
row8_col7.grid(row=8, column=7)
row8_col8.grid(row=8, column=8)
row8_col9.grid(row=8, column=9)

# row 9
row9_col1.grid(row=9, column=1)
row9_col2.grid(row=9, column=2)
row9_col3.grid(row=9, column=3)
row9_col4.grid(row=9, column=4)
row9_col5.grid(row=9, column=5)
row9_col6.grid(row=9, column=6)
row9_col7.grid(row=9, column=7)
row9_col8.grid(row=9, column=8)
row9_col9.grid(row=9, column=9)

# create a submit button
submit_btn = Button(root, text="Solve the Puzzle", command=submit, background="green")
submit_btn.grid(row=10, column=4, columnspan=3)

root.mainloop()