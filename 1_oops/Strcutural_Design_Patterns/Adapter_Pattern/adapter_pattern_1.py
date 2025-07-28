# Scenario:
#     Using a European Socket with an American Plug
#     Suppose you're in Europe with an American plug device, and European sockets don't directly support it.
#     The Adapter Pattern solves this by creating a "socket adapter" that converts the European socket to work with the American plug.

# Implementation in Python
#     Target Interface: EuropeanSocket represents the European standard socket.
#     Adaptee: AmericanPlugDevice represents the incompatible American plug.
#     Adapter: SocketAdapter makes AmericanPlugDevice compatible with EuropeanSocket.

# Reusability: The adapter allows you to reuse existing code (e.g., American devices) without modification.

# Extensibility: You can create more adapters for other socket types without changing the client code


# Target interface: EuropeanSocket
class EuropeanSocket:
    def provide_power(self):
        print("Providing power through a European socket.")


# Adaptee: AmericanPlugDevice with an incompatible interface
class AmericanPlugDevice:
    def use_american_socket(self):
        print("Using power through an American socket.")


# Adapter: Converts EuropeanSocket to work with AmericanPlugDevice
class SocketAdapter(EuropeanSocket):
    def __init__(self, american_device):
        self.american_device = american_device

    def provide_power(self):
        # Adapting the European socket to the American plug
        print("Adapter converting power from European to American standard.")
        self.american_device.use_american_socket()


# Client code
def use_european_power(device):
    device.provide_power()


# Creating an American plug device
american_device = AmericanPlugDevice()

# Using an adapter to connect the American device to a European socket
adapter = SocketAdapter(american_device)
adapter.provide_power()

# Client can now use the European socket interface
use_european_power(adapter)

# Output:
# Adapter converting power from European to American standard.
# Using power through an American socket.
