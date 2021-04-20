# aurpm-lite
A version of aurpm meant for slow connections and more then 1 arch install 

If you are looking for a aur package manager for a single machine use [yay](https://aur.archlinux.org/packages/yay/) or [aurpm](https://github.com/harvey298/aurpm/) (Not Lite)


# Use Case
The possible use cases of aurpm-lite is in where you have slow internet and you want to download and install the same aur package on diffrent machines,
the clients would have the client version of aurpm-lite and would send requests to the server and the server would download the aur package and provide it to the client wanting it.

This senario would mean that the packages would be downloaded by 1 machine and serve the packages to the clients speeding up the whole proccess on a slower internet connection

# The Goal
aurpm-lite is a version of aurpm with a client and a server. I would like to have the client interact with the server using a json format and the server respond with details which could include if the server can provide the package or not (such as if the package doesn't exists on the aur)
