from collections import deque


class CustomerRequest:
    def __init__(self, customer, message):
        self.customer = customer
        self.message = message

    def display(self):
        print(self.customer, ":", self.message)


def analyze_request(request):
    message = request.message.lower()

    if "urgent" in message or "not working" in message:
        return "HIGH"

    if "refund" in message or "payment" in message:
        return "MEDIUM"

    return "LOW"


def process_requests(request_queue):
    while request_queue:

        request = request_queue.popleft()

        priority = analyze_request(request)

        print("\nCustomer:", request.customer)
        print("Message:", request.message)
        print("AI Priority:", priority)

        if priority == "HIGH":
            print("Action: Immediately notify support team.")
        elif priority == "MEDIUM":
            print("Action: Create support ticket.")
        else:
            print("Action: Send automated response.")


requests = [
    CustomerRequest("Rahul", "My account is not working"),
    CustomerRequest("Priya", "I need a refund"),
    CustomerRequest("Arun", "Can you tell me your working hours?")
]

request_queue = deque()

try:
    for request in requests:
        request_queue.append(request)

    process_requests(request_queue)

except Exception as e:
    print("AI Automation Error:", e)
