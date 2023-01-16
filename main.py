# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

for i in range(nombreEtudiant):
    noteT = float(input("Note etudiant {} : ".format(i+1)))
    if noteT >= 0.0 and noteT <= 20.0:
        notes.append(noteT)
        sommeNotes += noteT
    else:
        while true: