import matplotlib.pyplot as plt

def paint_graph(history):
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend(['loss', 'val_loss'])
    plt.show()