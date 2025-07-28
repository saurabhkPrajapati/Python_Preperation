# Problem:
#     You want to access a remote resource (e.g., a database or an API) but need to manage network communication, connection overhead, or caching locally.

# Scenario:
#     Suppose we have a service that provides information about products.
#     Accessing this service is expensive (e.g., requires a network request).
#     We can use a proxy to handle network communication and cache results to optimize performance.

from abc import ABC, abstractmethod


# Step 1: Define the Subject interface
class ProductService(ABC):
    @abstractmethod
    def get_product_details(self, product_id: int) -> dict:
        pass


# Step 2: Create the RealSubject (Remote Service)
class RealProductService(ProductService):
    def get_product_details(self, product_id: int) -> dict:
        # Simulating a remote service call
        print(f"[RealService] Fetching product details for ID {product_id} from remote server...")
        return {"id": product_id, "name": f"Product {product_id}", "price": 100 + product_id}


# Step 3: Create the Proxy
class ProductServiceProxy(ProductService):
    def __init__(self):
        self.real_service = RealProductService()
        self.cache = {}  # A local cache for product details

    def get_product_details(self, product_id: int) -> dict:
        if product_id in self.cache:
            print(f"[Proxy] Returning cached details for product ID {product_id}.")
            return self.cache[product_id]

        print(f"[Proxy] Cache miss for product ID {product_id}. Delegating to RealProductService.")
        product_details = self.real_service.get_product_details(product_id)
        self.cache[product_id] = product_details  # Cache the result
        return product_details


# Step 4: Client code
if __name__ == "__main__":
    proxy_service = ProductServiceProxy()

    # First access - Fetches from RealProductService
    print(proxy_service.get_product_details(1))
    print()

    # Second access - Returns cached result
    print(proxy_service.get_product_details(1))
    print()

    # Another product - Fetches from RealProductService
    print(proxy_service.get_product_details(2))
