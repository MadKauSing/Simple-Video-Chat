import Client;
import Server;

from multiprocessing import Process
from time import sleep



if __name__ == '__main__':
    Process(target=Server.server).start()

    sleep(5)
    Process(target=Client.client).start()

    