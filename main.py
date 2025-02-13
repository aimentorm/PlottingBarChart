# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as mplt
fig, ax=mplt.subplots()
fruits=['Apple', 'Mango', 'Guava', 'Orange']
counts=[45,120,80,40]
bar_labels=['red','green','dark_cyan','orange']
#bar_colors=['tab:red', 'tab:green', 'tab:#2e9e98','tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=('red','green','#2e9e98','orange'))

ax.set_ylabel('Fruit Supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit Color')
mplt.show()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
